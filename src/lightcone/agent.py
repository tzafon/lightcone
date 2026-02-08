"""CUAAgent — the computer-use agent loop with context management."""

from __future__ import annotations

import base64
import json
import logging
import time
from datetime import datetime
from io import BytesIO
from pathlib import Path
from urllib.parse import urlparse
from typing import Any, Callable, Dict, List, Optional, Tuple

import requests
from PIL import Image, UnidentifiedImageError

from lightcone.actions import execute_action
from lightcone.clients import build_computer_client, build_llm_client, resolve_api_key
from lightcone.config import Settings, get_settings
from lightcone.images import decode_data_url, ensure_data_url, process_image
from lightcone.models import resolve_model
from lightcone.parsing import parse_action_description, parse_tool_call
from lightcone.prompts import build_system_prompt

logger = logging.getLogger("lightcone.agent")

EventHandler = Callable[[Dict[str, Any]], None]

_SCREENSHOT_ROOT = Path(__file__).resolve().parents[2] / "screenshots"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _fetch_screenshot_bytes(url: str) -> Optional[bytes]:
    """Download screenshot bytes from a URL or data-URL."""
    try:
        if not url:
            return None
        if url.startswith("data:"):
            data_bytes = decode_data_url(url)
            if data_bytes:
                return data_bytes
            payload = url[5:].strip()
            if payload:
                try:
                    return base64.b64decode(payload)
                except Exception:
                    return None
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.content
    except Exception as exc:
        logger.warning("Failed to download screenshot bytes: %s", exc)
        return None


def _infer_image_extension(image_bytes: bytes) -> str:
    try:
        img = Image.open(BytesIO(image_bytes))
        fmt = (img.format or "PNG").lower()
    except (UnidentifiedImageError, OSError, ValueError):
        return "jpg"
    return {"jpeg": "jpg", "jpg": "jpg", "png": "png", "gif": "gif", "webp": "webp"}.get(
        fmt, "png"
    )


def _get_image_size(image_bytes: bytes) -> Tuple[int, int]:
    img = Image.open(BytesIO(image_bytes))
    return img.size


# ---------------------------------------------------------------------------
# Message building (pure Python — replaces Rust build_messages)
# ---------------------------------------------------------------------------


def _build_messages(
    system_prompt: str,
    instruction: str,
    current_screenshot_url: str,
    history_responses: List[str],
    history_screenshots: List[str],
    all_actions: List[str],
    max_history_turns: int,
) -> List[Dict[str, Any]]:
    """Build the multi-turn message list with sliding-window history."""
    messages: List[Dict[str, Any]] = [
        {"role": "system", "content": [{"type": "text", "text": system_prompt}]},
    ]

    # Determine which past actions fall outside the history window.
    history_start_idx = max(0, len(all_actions) - max_history_turns)
    previous_actions: List[str] = []
    for i in range(history_start_idx):
        if i < len(all_actions):
            previous_actions.append(f"Step {i + 1}: {all_actions[i]}")
    previous_actions_str = "\n".join(previous_actions) if previous_actions else "None"

    # Add history turns (screenshot + response pairs).
    history_len = min(max_history_turns, len(history_responses))
    if history_len > 0:
        hist_responses = history_responses[-history_len:]
        hs_len = len(history_screenshots)
        start = max(0, hs_len - history_len - 1)
        end = max(0, hs_len - 1)
        hist_screenshots = history_screenshots[start:end] if start < end else []

        for i, resp in enumerate(hist_responses):
            if i < len(hist_screenshots):
                content: List[Dict[str, Any]] = [
                    {"type": "image_url", "image_url": {"url": hist_screenshots[i]}},
                ]
                if i == 0:
                    content.append({
                        "type": "text",
                        "text": (
                            "\nPlease generate the next move according to the UI screenshot, "
                            f"instruction and previous actions.\n\nInstruction: {instruction}"
                            f"\n\nPrevious actions:\n{previous_actions_str}"
                        ),
                    })
                messages.append({"role": "user", "content": content})
            messages.append({
                "role": "assistant",
                "content": [{"type": "text", "text": resp}],
            })

    # Current turn.
    current_content: List[Dict[str, Any]] = [
        {"type": "image_url", "image_url": {"url": current_screenshot_url}},
    ]
    if history_len == 0:
        current_content.append({
            "type": "text",
            "text": (
                "\nPlease generate the next move according to the UI screenshot, "
                f"instruction and previous actions.\n\nInstruction: {instruction}"
                f"\n\nPrevious actions:\n{previous_actions_str}"
            ),
        })
    messages.append({"role": "user", "content": current_content})

    return messages


# ---------------------------------------------------------------------------
# LLM call with retry + context management
# ---------------------------------------------------------------------------


def _is_context_error(error: Exception) -> bool:
    error_str = str(error).lower()
    return any(
        needle in error_str
        for needle in ("too large", "context_length_exceeded", "413", "maximum context")
    )


def _normalize_response_content(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: List[str] = []
        for item in content:
            if isinstance(item, dict):
                if item.get("type") == "text":
                    parts.append(item.get("text", ""))
                else:
                    parts.append(json.dumps(item, ensure_ascii=True))
            else:
                parts.append(str(item))
        return "\n".join(p for p in parts if p)
    return str(content)


def _call_llm_with_retry(
    llm_client: Any,
    *,
    instruction: str,
    current_screenshot_url: str,
    viewport_width: int,
    viewport_height: int,
    history_responses: List[str],
    history_screenshots: List[str],
    all_actions: List[str],
    current_history_n: int,
    model: str,
    temperature: float,
    top_p: float,
    max_tokens: int,
    max_retries: int,
    retry_delay_s: float,
    timeout_s: Optional[float] = None,
    prompt_profile: str | None = None,
) -> Tuple[Optional[str], int]:
    """Call the LLM with retry logic and automatic history shrinking.

    Returns ``(response_text, final_history_n)``.
    """
    system_prompt = build_system_prompt(viewport_width, viewport_height, profile=prompt_profile)

    messages = _build_messages(
        system_prompt,
        instruction,
        current_screenshot_url,
        history_responses,
        history_screenshots,
        all_actions,
        current_history_n,
    )

    for attempt in range(max_retries):
        try:
            kwargs: Dict[str, Any] = {
                "model": model,
                "messages": messages,
                "temperature": temperature,
                "top_p": top_p,
                "max_tokens": max_tokens,
            }
            if timeout_s is not None:
                kwargs["timeout"] = timeout_s

            response = llm_client.chat.completions.create(**kwargs)
            text = _normalize_response_content(response.choices[0].message.content)
            return text, current_history_n

        except Exception as exc:
            logger.warning("LLM call failed (attempt %d): %s", attempt + 1, exc)

            if _is_context_error(exc) and current_history_n > 0:
                current_history_n = max(0, current_history_n - 1)
                logger.info("Context too large, reducing history to %d", current_history_n)
                messages = _build_messages(
                    system_prompt,
                    instruction,
                    current_screenshot_url,
                    history_responses,
                    history_screenshots,
                    all_actions,
                    current_history_n,
                )
            else:
                time.sleep(retry_delay_s * (attempt + 1))

    return None, current_history_n


# ---------------------------------------------------------------------------
# CUAAgent
# ---------------------------------------------------------------------------


class CUAAgent:
    """Computer Use Agent with structured tool-call prompting.

    Features:
    - Sliding-window history to prevent context overflow
    - Retry with exponential backoff
    - Automatic history reduction on context-length errors
    """

    def __init__(
        self,
        *,
        max_steps: int | None = None,
        max_history_turns: int | None = None,
        temperature: float | None = None,
        top_p: float | None = None,
        max_tokens: int | None = None,
        model: str | None = None,
        llm_timeout_s: float | None = None,
        max_retries: int | None = None,
        retry_delay: float | None = None,
        viewport_width: int = 1280,
        viewport_height: int = 720,
        api_key: str | None = None,
        llm_client: Any | None = None,
        computer_client: Any | None = None,
        settings_override: Settings | None = None,
        event_handler: EventHandler | None = None,
        prompt_profile: str | None = None,
    ):
        s = settings_override or get_settings()
        self.settings = s
        self.max_steps = max_steps if max_steps is not None else s.max_steps
        self.max_history_turns = max_history_turns if max_history_turns is not None else s.max_history_turns
        self.temperature = temperature if temperature is not None else s.llm_temperature
        self.top_p = top_p if top_p is not None else s.llm_top_p
        self.max_tokens = max_tokens if max_tokens is not None else s.llm_max_tokens
        self.model = model if model is not None else s.llm_model
        self.llm_timeout_s = llm_timeout_s if llm_timeout_s is not None else s.llm_timeout_s
        self.max_retries = max_retries if max_retries is not None else s.llm_max_retries
        self.retry_delay = retry_delay if retry_delay is not None else s.llm_retry_delay_s
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self._event_handler = event_handler
        self.prompt_profile = prompt_profile or s.prompt_profile

        # Build clients if not injected.
        self._llm_client = llm_client
        self._computer_client = computer_client
        if self._llm_client is None or self._computer_client is None:
            key = resolve_api_key(api_key, s)
            if self._llm_client is None:
                self._llm_client = build_llm_client(key, s)
            if self._computer_client is None:
                self._computer_client = build_computer_client(key, s)
            self.model = resolve_model(self.model, api_key=key, base_url=s.llm_base_url)

        # Per-run state
        self.actions: List[str] = []
        self.responses: List[str] = []
        self.screenshot_urls: List[str] = []
        self.action_payloads: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def reset(self) -> None:
        """Clear per-run state."""
        self.actions.clear()
        self.responses.clear()
        self.screenshot_urls.clear()
        self.action_payloads.clear()

    def run(
        self,
        task: str,
        start_url: str = "",
        task_id: str | None = None,
        event_handler: EventHandler | None = None,
        prompt_profile: str | None = None,
    ) -> Tuple[str, Optional[str]]:
        """Run the agent loop.  Returns ``(status, result)``."""
        self.reset()
        handler = event_handler or self._event_handler

        def emit(event_type: str, **payload: Any) -> None:
            if handler is None:
                return
            event: Dict[str, Any] = {"type": event_type, **payload}
            if task_id:
                event["task_id"] = task_id
            handler(event)

        instruction = task.strip()
        start_url = start_url.strip()

        # Auto-detect bare URLs as start_url.
        if not start_url:
            parsed = urlparse(instruction)
            if parsed.scheme in ("http", "https") and parsed.netloc:
                start_url = instruction
                instruction = ""
        elif instruction == start_url:
            instruction = ""
        if start_url and not instruction:
            instruction = "Continue from the opened page."

        profile = prompt_profile or self.prompt_profile

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        screenshots_dir = _SCREENSHOT_ROOT / timestamp
        screenshots_dir.mkdir(parents=True, exist_ok=True)

        logger.info("Starting agent — task: %s", instruction[:100])

        with self._computer_client.create(kind="desktop") as computer:
            computer.set_viewport(self.viewport_width, self.viewport_height)
            computer.wait(2)

            if start_url:
                try:
                    computer.navigate(start_url)
                    computer.wait(2)
                except Exception as exc:
                    logger.warning("Failed to navigate to start URL: %s", exc)

            emit("started", computer_id=getattr(computer, "id", None), max_steps=self.max_steps)

            vw, vh = self.viewport_width, self.viewport_height
            current_history_n = self.max_history_turns

            for step in range(self.max_steps):
                logger.info("Step %d/%d", step + 1, self.max_steps)

                # 1. Screenshot
                screenshot = computer.screenshot()
                try:
                    screenshot_url = computer.get_screenshot_url(screenshot)
                    if not screenshot_url:
                        raise KeyError("screenshot_url missing")
                    screenshot_url = ensure_data_url(screenshot_url)
                except (TypeError, KeyError) as exc:
                    logger.error("Error getting screenshot: %s", exc)
                    emit("error", step=step, error=f"Failed to get screenshot: {exc}")
                    continue

                emit("screenshot", step=step, screenshot_url=screenshot_url)

                screenshot_bytes = _fetch_screenshot_bytes(screenshot_url)
                if not screenshot_bytes:
                    logger.error("Failed to download screenshot bytes")
                    emit("error", step=step, error="Failed to download screenshot bytes")
                    continue

                # Save to disk
                ext = _infer_image_extension(screenshot_bytes)
                img_path = screenshots_dir / f"{step}.{ext}"
                img_path.write_bytes(screenshot_bytes)

                # Detect effective viewport from screenshot dimensions.
                eff_w, eff_h = vw, vh
                try:
                    img_w, img_h = _get_image_size(screenshot_bytes)
                    if (img_w, img_h) != (vw, vh):
                        logger.warning(
                            "Screenshot %dx%d != viewport %dx%d; using screenshot size",
                            img_w, img_h, vw, vh,
                        )
                        eff_w, eff_h = img_w, img_h
                except Exception:
                    pass

                # 2. Process image for model input (Rust pipeline)
                processed_b64, *_ = process_image(screenshot_bytes, factor=32)
                data_url = f"data:image/png;base64,{processed_b64}"
                self.screenshot_urls.append(data_url)

                # 3. Call LLM
                emit("thinking", step=step)
                response_text, current_history_n = _call_llm_with_retry(
                    self._llm_client,
                    instruction=instruction,
                    current_screenshot_url=data_url,
                    viewport_width=vw,
                    viewport_height=vh,
                    history_responses=self.responses,
                    history_screenshots=self.screenshot_urls,
                    all_actions=self.actions,
                    current_history_n=current_history_n,
                    model=self.model,
                    temperature=self.temperature,
                    top_p=self.top_p,
                    max_tokens=self.max_tokens,
                    max_retries=self.max_retries,
                    retry_delay_s=self.retry_delay,
                    timeout_s=self.llm_timeout_s,
                    prompt_profile=profile,
                )
                response_text = _normalize_response_content(response_text)

                if not response_text:
                    logger.error("LLM call failed after retries")
                    emit("error", step=step, error="LLM call failed after retries")
                    continue

                # 4. Parse response
                action_desc = parse_action_description(response_text)
                action = parse_tool_call(response_text)

                emit("action", step=step, action=action, description=action_desc)
                logger.info("Action: %s", action_desc or "N/A")

                if not action:
                    logger.warning("Failed to parse action from response")
                    self.responses.append(response_text)
                    self.actions.append("Failed to parse")
                    continue

                self.responses.append(response_text)
                self.actions.append(action_desc or str(action.get("action", "unknown")))
                self.action_payloads.append(action)

                # 5. Execute action
                should_continue, status, result = execute_action(
                    computer, action, eff_w, eff_h,
                )

                emit("executed", step=step)
                if not should_continue:
                    event_type = "completed" if status == "success" else "failed"
                    emit(event_type, step=step, result=result)
                    return status or "success", result

                if step >= self.max_steps - 1:
                    logger.warning("Reached maximum steps (%d)", self.max_steps)
                    emit("max_steps", step=self.max_steps)
                    return "max_steps", None

                computer.wait(2)

        emit("max_steps", step=self.max_steps)
        return "max_steps", None
