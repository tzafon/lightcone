"""Reusable harness for Lightcone computer-use loops."""

from __future__ import annotations

from contextlib import nullcontext
from dataclasses import asdict, dataclass, field, is_dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any, Callable

TERMINAL_ACTION_TYPES = frozenset({"terminate", "done", "answer"})


@dataclass(slots=True)
class RunConfig:
    model: str
    kind: str = "browser"
    environment: str = "browser"
    display_width: int = 1280
    display_height: int = 720
    max_steps: int = 50
    step_delay_seconds: float = 1.0
    wait_action_seconds: float = 2.0
    initial_navigation_delay_seconds: float = 2.0
    trace_path: str | None = None
    print_progress: bool = False
    persistent: bool = False
    computer_kwargs: dict[str, Any] = field(default_factory=dict)
    response_kwargs: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RunResult:
    status: str
    steps: int
    computer_id: str | None = None
    response_id: str | None = None
    final_message: str | None = None
    last_screenshot_url: str | None = None
    trace_path: str | None = None


@dataclass(slots=True)
class MessageEvent:
    step: int
    text: str
    response: Any
    computer_id: str


@dataclass(slots=True)
class ActionEvent:
    step: int
    action: Any
    response: Any
    computer: Any
    computer_id: str
    screenshot_url: str | None


@dataclass(slots=True)
class ActionDecision:
    execute_action: bool = True
    continue_run: bool = True
    message: str | None = None
    wait_seconds: float | None = None
    result_message: str | None = None


class TraceWriter:
    """Append structured runner events to a JSONL file."""

    def __init__(self, path: str) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, event: str, payload: dict[str, Any]) -> None:
        record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event": event,
            **payload,
        }
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, default=_json_default))
            handle.write("\n")


def _json_default(value: Any) -> Any:
    if is_dataclass(value):
        return asdict(value)
    if hasattr(value, "to_dict"):
        return value.to_dict()
    if hasattr(value, "model_dump"):
        return value.model_dump()
    if isinstance(value, Path):
        return str(value)
    if hasattr(value, "__dict__"):
        return value.__dict__
    return repr(value)


class CuaRunner:
    """Drive a screenshot-think-act loop around Lightcone's Responses API."""

    def __init__(
        self,
        client: Any,
        *,
        config: RunConfig,
        on_action: Callable[[ActionEvent], None] | None = None,
        on_message: Callable[[MessageEvent], None] | None = None,
        before_action: Callable[[ActionEvent], ActionDecision | None] | None = None,
        action_executor: Callable[[Any, Any], None] | None = None,
    ) -> None:
        self.client = client
        self.config = config
        self.on_action = on_action
        self.on_message = on_message
        self.before_action = before_action
        self.action_executor = action_executor or self._default_execute_action
        self.trace_writer = TraceWriter(config.trace_path) if config.trace_path else None

    def run(
        self,
        instruction: str,
        *,
        start_url: str | None = None,
        computer: Any | None = None,
    ) -> RunResult:
        context = nullcontext(computer) if computer is not None else self.client.computer.create(
            kind=self.config.kind,
            persistent=self.config.persistent,
            **self.config.computer_kwargs,
        )

        with context as session:
            computer_id = getattr(session, "id", None)
            self._log(
                f"starting run kind={self.config.kind} computer_id={computer_id}",
            )
            self._trace(
                "run_started",
                {
                    "instruction": instruction,
                    "computer_id": computer_id,
                    "config": self.config,
                    "start_url": start_url,
                },
            )

            if start_url:
                self._log(f"navigate start_url={start_url}")
                session.navigate(start_url)
                session.wait(self.config.initial_navigation_delay_seconds)

            screenshot_url = self._capture_screenshot(session)
            response = self._create_initial_response(instruction, screenshot_url)

            for step in range(1, self.config.max_steps + 1):
                self._emit_messages(step, response, computer_id)
                computer_call = self._find_computer_call(response)
                if computer_call is None:
                    final_message = self._collect_message_text(response)
                    result = RunResult(
                        status="completed_no_action",
                        steps=step - 1,
                        computer_id=computer_id,
                        response_id=getattr(response, "id", None),
                        final_message=final_message,
                        last_screenshot_url=screenshot_url,
                        trace_path=self.config.trace_path,
                    )
                    self._log(
                        f"completed status={result.status} steps={result.steps}",
                    )
                    self._trace("run_completed", result)
                    return result

                action = computer_call.action
                event = ActionEvent(
                    step=step,
                    action=action,
                    response=response,
                    computer=session,
                    computer_id=computer_id,
                    screenshot_url=screenshot_url,
                )
                if self.on_action is not None:
                    self.on_action(event)
                self._log(
                    f"[{step}] action={action.type}{self._format_action_details(action)}",
                )

                decision = (
                    self.before_action(event) if self.before_action is not None else None
                ) or ActionDecision()
                self._trace(
                    "action_selected",
                    {
                        "step": step,
                        "computer_id": computer_id,
                        "response_id": getattr(response, "id", None),
                        "action": action,
                        "decision": decision,
                    },
                )

                if not decision.continue_run:
                    result = RunResult(
                        status="stopped",
                        steps=step - 1,
                        computer_id=computer_id,
                        response_id=getattr(response, "id", None),
                        final_message=decision.result_message or "Stopped by hook.",
                        last_screenshot_url=screenshot_url,
                        trace_path=self.config.trace_path,
                    )
                    self._log(
                        f"stopped status={result.status} steps={result.steps}",
                    )
                    self._trace("run_completed", result)
                    return result

                if action.type in TERMINAL_ACTION_TYPES:
                    final_message = (
                        decision.result_message
                        or getattr(action, "result", None)
                        or getattr(action, "text", None)
                        or getattr(action, "status", None)
                        or self._collect_message_text(response)
                    )
                    result = RunResult(
                        status="completed",
                        steps=step,
                        computer_id=computer_id,
                        response_id=getattr(response, "id", None),
                        final_message=final_message,
                        last_screenshot_url=screenshot_url,
                        trace_path=self.config.trace_path,
                    )
                    self._log(
                        f"completed status={result.status} steps={result.steps}",
                    )
                    self._trace("run_completed", result)
                    return result

                if decision.execute_action:
                    self.action_executor(session, action)
                else:
                    self._log(f"[{step}] action skipped by hook")

                wait_seconds = decision.wait_seconds
                if wait_seconds is None:
                    wait_seconds = self.config.step_delay_seconds
                if wait_seconds > 0:
                    self._log(f"[{step}] wait={wait_seconds}s")
                    session.wait(wait_seconds)

                screenshot_url = self._capture_screenshot(session)
                response = self._create_follow_up_response(
                    response_id=response.id,
                    call_id=computer_call.call_id,
                    screenshot_url=screenshot_url,
                    message=decision.message,
                )

            result = RunResult(
                status="max_steps_exceeded",
                steps=self.config.max_steps,
                computer_id=computer_id,
                response_id=getattr(response, "id", None),
                final_message=self._collect_message_text(response),
                last_screenshot_url=screenshot_url,
                trace_path=self.config.trace_path,
            )
            self._log(
                f"completed status={result.status} steps={result.steps}",
            )
            self._trace("run_completed", result)
            return result

    def _tool(self) -> dict[str, Any]:
        return {
            "type": "computer_use",
            "display_width": self.config.display_width,
            "display_height": self.config.display_height,
            "environment": self.config.environment,
        }

    def _capture_screenshot(self, computer: Any) -> str | None:
        result = computer.screenshot()
        screenshot_url = computer.get_screenshot_url(result)
        self._trace(
            "screenshot_captured",
            {
                "computer_id": getattr(computer, "id", None),
                "screenshot_url": screenshot_url,
            },
        )
        return screenshot_url

    def _create_initial_response(self, instruction: str, screenshot_url: str | None) -> Any:
        return self.client.responses.create(
            model=self.config.model,
            tools=[self._tool()],
            input=[{
                "role": "user",
                "content": [
                    {"type": "input_text", "text": instruction},
                    {"type": "input_image", "image_url": screenshot_url},
                ],
            }],
            **self.config.response_kwargs,
        )

    def _create_follow_up_response(
        self,
        *,
        response_id: str,
        call_id: str,
        screenshot_url: str | None,
        message: str | None,
    ) -> Any:
        payload: list[dict[str, Any]] = [{
            "type": "computer_call_output",
            "call_id": call_id,
            "output": {"type": "input_image", "image_url": screenshot_url},
        }]
        if message:
            payload.append({
                "role": "user",
                "content": [{"type": "input_text", "text": message}],
            })
        return self.client.responses.create(
            model=self.config.model,
            previous_response_id=response_id,
            tools=[self._tool()],
            input=payload,
            **self.config.response_kwargs,
        )

    def _emit_messages(self, step: int, response: Any, computer_id: str) -> None:
        for item in getattr(response, "output", None) or []:
            if item.type != "message":
                continue
            for block in item.content or []:
                if not getattr(block, "text", None):
                    continue
                event = MessageEvent(
                    step=step,
                    text=block.text,
                    response=response,
                    computer_id=computer_id,
                )
                self._trace(
                    "message_received",
                    {
                        "step": step,
                        "computer_id": computer_id,
                        "response_id": getattr(response, "id", None),
                        "text": block.text,
                    },
                )
                if self.on_message is not None:
                    self.on_message(event)
                self._log(f"[{step}] model={block.text}")

    @staticmethod
    def _find_computer_call(response: Any) -> Any | None:
        for item in getattr(response, "output", None) or []:
            if item.type == "computer_call":
                return item
        return None

    @staticmethod
    def _collect_message_text(response: Any) -> str | None:
        chunks: list[str] = []
        for item in getattr(response, "output", None) or []:
            if item.type != "message":
                continue
            for block in item.content or []:
                if getattr(block, "text", None):
                    chunks.append(block.text)
        if not chunks:
            return None
        return "\n".join(chunks)

    def _default_execute_action(self, computer: Any, action: Any) -> None:
        action_type = action.type
        if action_type == "click":
            computer.click(action.x, action.y)
        elif action_type == "double_click":
            computer.double_click(action.x, action.y)
        elif action_type == "triple_click":
            computer.click(action.x, action.y)
            computer.click(action.x, action.y)
            computer.click(action.x, action.y)
        elif action_type == "right_click":
            computer.right_click(action.x, action.y)
        elif action_type == "type":
            computer.type(action.text)
        elif action_type in ("key", "keypress"):
            computer.hotkey(action.keys)
        elif action_type == "key_down":
            computer.key_down(action.keys[0])
        elif action_type == "key_up":
            computer.key_up(action.keys[0])
        elif action_type == "scroll":
            computer.scroll(
                dx=action.scroll_x or 0,
                dy=action.scroll_y or 0,
                x=action.x or 0,
                y=action.y or 0,
            )
        elif action_type == "hscroll":
            computer.scroll(
                dx=action.scroll_x or 0,
                dy=0,
                x=action.x or 0,
                y=action.y or 0,
            )
        elif action_type == "navigate":
            computer.navigate(action.url)
        elif action_type == "drag":
            computer.drag(action.x, action.y, action.end_x, action.end_y)
        elif action_type == "wait":
            computer.wait(self.config.wait_action_seconds)
        else:
            raise ValueError(f"Unsupported action type: {action_type}")

    def _log(self, message: str) -> None:
        if self.config.print_progress:
            print(f"[cua] {message}", flush=True)

    @staticmethod
    def _format_action_details(action: Any) -> str:
        details: list[str] = []
        if getattr(action, "x", None) is not None and getattr(action, "y", None) is not None:
            details.append(f"x={action.x} y={action.y}")
        if getattr(action, "end_x", None) is not None and getattr(action, "end_y", None) is not None:
            details.append(f"end_x={action.end_x} end_y={action.end_y}")
        if getattr(action, "url", None):
            details.append(f"url={action.url}")
        if getattr(action, "text", None):
            details.append(f"text={action.text!r}")
        if not details:
            return ""
        return " " + " ".join(details)

    def _trace(self, event: str, payload: Any) -> None:
        if self.trace_writer is None:
            return
        if isinstance(payload, dict):
            data = payload
        else:
            data = {"payload": payload}
        self.trace_writer.write(event, data)
