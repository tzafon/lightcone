"""Shared CUA loop utilities for Lightcone examples.

Handles coordinate scaling, action normalization, and safe output
parsing for both typed SDK objects and raw dict fallbacks.
"""

import json
import time

from tzafon.types.response_create_response import (
    Output,
    OutputResponseComputerToolCall,
    OutputResponseFunctionToolCall,
    OutputResponseOutputMessage,
)

DONE_TOOL = {
    "type": "function",
    "name": "done",
    "description": "Call this when the task is complete.",
    "parameters": {
        "type": "object",
        "properties": {
            "message": {"type": "string", "description": "Summary of what was accomplished."},
        },
    },
}

COORD_KEYS = {
    "x": "display_width", "x1": "display_width", "x2": "display_width",
    "y": "display_height", "y1": "display_height", "y2": "display_height",
}


def normalize_action(action, tool):
    """Convert a model action to a dict with pixel-scaled coordinates."""
    d = action.model_dump() if hasattr(action, "model_dump") else dict(action)
    for key, dim in COORD_KEYS.items():
        if key in d and d[key] is not None:
            d[key] = int(d[key] / 1000 * tool[dim])
    if "keys" in d:
        keys = d["keys"]
        if isinstance(keys, str):
            d["keys"] = keys.split("+")
        elif isinstance(keys, list):
            flat = []
            for k in keys:
                try:
                    parsed = json.loads(k)
                    flat.extend(parsed if isinstance(parsed, list) else [parsed])
                except (json.JSONDecodeError, TypeError):
                    flat.append(k)
            d["keys"] = flat
    return d


def get_computer_calls(output, tool):
    """Extract all computer calls from response output, returning (actions, call_ids)."""
    calls, call_ids = [], []
    for item in output or []:
        if isinstance(item, OutputResponseComputerToolCall):
            calls.append(normalize_action(item.action, tool))
            call_ids.append(item.call_id)
        elif isinstance(item, dict) and item.get("type") == "computer_call":
            calls.append(normalize_action(item["action"], tool))
            call_ids.append(item["call_id"])
    return calls, call_ids


def get_first_computer_call(output, tool):
    """Extract the first computer call, returning (action_dict, call_id) or (None, None)."""
    calls, call_ids = get_computer_calls(output, tool)
    if calls:
        return calls[0], call_ids[0]
    return None, None


def is_done(output):
    """Check if the model signalled task completion via a 'done' function call."""
    for item in output or []:
        if isinstance(item, OutputResponseFunctionToolCall) and item.name == "done":
            return True
        if isinstance(item, dict) and item.get("type") == "function_call" and item.get("name") == "done":
            return True
    return False


def get_messages(output):
    """Extract text messages from response output."""
    texts = []
    for item in output or []:
        if isinstance(item, OutputResponseOutputMessage):
            for block in item.content or []:
                if getattr(block, "text", None):
                    texts.append(block.text)
        elif isinstance(item, dict) and item.get("type") == "message":
            for block in item.get("content") or []:
                text = block.get("text") if isinstance(block, dict) else getattr(block, "text", None)
                if text:
                    texts.append(text)
    return texts


def print_messages(output):
    """Print any text messages from the model."""
    for text in get_messages(output):
        print(text)


def format_action(action_dict):
    """Format an action dict for human-readable logging."""
    label = action_dict.get("type", "?")
    if action_dict.get("x") is not None:
        label += f" @ ({action_dict['x']}, {action_dict['y']})"
    if action_dict.get("text"):
        label += f" '{action_dict['text']}'"
    if action_dict.get("url"):
        label += f" {action_dict['url']}"
    if action_dict.get("keys"):
        label += f" {'+'.join(action_dict['keys'])}"
    return label


def is_terminal_action(action_dict):
    """Check if an action signals the loop should stop."""
    return action_dict.get("type") in ("terminate", "done", "answer")


def run_cua_loop(client, computer, tool, task, *, max_steps=50, on_step=None):
    """Run a complete CUA loop with client-side conversation history.

    Args:
        client: Lightcone client instance.
        computer: Computer session (from client.computer.create).
        tool: Tool dict (type, display_width, display_height, environment).
        task: Instruction string for Northstar.
        max_steps: Maximum number of steps.
        on_step: Optional callback(step, action_dict, screenshot_url) called each step.

    Returns:
        (items, last_screenshot_url) — the full conversation history and final screenshot.
    """
    screenshot_url = computer.get_screenshot_url(computer.screenshot())

    items = [
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": task},
                {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
            ],
        }
    ]

    for step in range(1, max_steps + 1):
        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            tools=[tool, DONE_TOOL],
            input=items,
        )

        items.extend(response.output or [])

        print_messages(response.output)

        if is_done(response.output):
            break

        calls, call_ids = get_computer_calls(response.output, tool)
        if not calls:
            break

        for c in calls:
            print(f"[{step}] {format_action(c)}")

        if any(is_terminal_action(c) for c in calls):
            break

        if on_step:
            on_step(step, calls, screenshot_url)

        computer.batch(calls)
        time.sleep(1)

        screenshot_url = computer.get_screenshot_url(computer.screenshot())
        for call_id in call_ids:
            items.append({
                "type": "computer_call_output",
                "call_id": call_id,
                "output": {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
            })

    return items, screenshot_url
