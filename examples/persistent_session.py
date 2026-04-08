"""CUA loop with a persistent session for authenticated workflows.

Persistent sessions save cookies and storage state across reconnects,
so you can log in once and run multiple tasks without re-authenticating.
"""

import json
import os
import sys
from tzafon import Lightcone
from tzafon.lib.computer_session import ComputerSession

client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "browser",
}


def _px(coord, dim):
    """Convert a 0–1000 model coordinate to a pixel coordinate."""
    return int(coord / 1000 * dim)


def execute_action(computer, action):
    """Execute a model action on the computer session."""
    w, h = TOOL["display_width"], TOOL["display_height"]
    t = action.type
    if t == "click":
        computer.click(_px(action.x, w), _px(action.y, h))
    elif t == "double_click":
        computer.double_click(_px(action.x, w), _px(action.y, h))
    elif t == "triple_click":
        computer.click(_px(action.x, w), _px(action.y, h))
        computer.click(_px(action.x, w), _px(action.y, h))
        computer.click(_px(action.x, w), _px(action.y, h))
    elif t == "right_click":
        computer.right_click(_px(action.x, w), _px(action.y, h))
    elif t == "type":
        computer.type(action.text)
    elif t in ("key", "keypress"):
        computer.hotkey(action.keys)
    elif t == "key_down":
        computer.key_down(action.keys[0])
    elif t == "key_up":
        computer.key_up(action.keys[0])
    elif t == "scroll":
        computer.scroll(
            dx=action.scroll_x or 0,
            dy=action.scroll_y or 0,
            x=_px(action.x or 0, w),
            y=_px(action.y or 0, h),
        )
    elif t == "hscroll":
        computer.scroll(
            dx=action.scroll_x or 0,
            dy=0,
            x=_px(action.x or 0, w),
            y=_px(action.y or 0, h),
        )
    elif t == "navigate":
        computer.navigate(action.url)
    elif t == "drag":
        computer.drag(
            _px(action.x, w), _px(action.y, h), _px(action.end_x, w), _px(action.end_y, h)
        )
    elif t == "wait":
        computer.wait(2)


def run_task(computer, task, start_url=None, max_steps=50):
    """Run a single CUA task on an existing computer session."""
    if start_url:
        computer.navigate(start_url)
        computer.wait(2)

    screenshot_url = computer.get_screenshot_url(computer.screenshot())
    response = client.responses.create(
        model="tzafon.northstar-cua-fast",
        tools=[TOOL],
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": task},
                    {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
                ],
            }
        ],
    )

    for step in range(max_steps):
        computer_call = next(
            (o for o in (response.output or []) if o.type == "computer_call"), None
        )
        if not computer_call:
            break

        action = computer_call.action
        print(f"  [{step + 1}] {action.type}")

        if action.type in ("terminate", "done", "answer"):
            print(f"  Done: {action.result or action.text or action.status}")
            return

        execute_action(computer, action)
        computer.wait(1)

        screenshot_url = computer.get_screenshot_url(computer.screenshot())
        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            previous_response_id=response.id,
            tools=[TOOL],
            input=[
                {
                    "type": "computer_call_output",
                    "call_id": computer_call.call_id,
                    "output": {
                        "type": "input_image",
                        "image_url": screenshot_url,
                        "detail": "auto",
                    },
                }
            ],
        )


# Reconnect to an existing session, or create a new persistent one.
session_id = sys.argv[1] if len(sys.argv) > 1 else None

if session_id:
    print(f"Reconnecting to session {session_id}")
    computer = ComputerSession(client, session_id)
else:
    computer = client.computer.create(kind="browser", persistent=True)
    print(f"Created persistent session: {computer.id}")
    print(f"  Re-run with: python {sys.argv[0]} {computer.id}")

_tasks_env = os.getenv("LIGHTCONE_PERSISTENT_TASKS_JSON")
tasks = (
    json.loads(_tasks_env)
    if _tasks_env
    else [
        {
            "label": "Task 1: Log in",
            "task": "Log in with username 'demo' and password 'demo123'",
            "start_url": "https://example.com/login",
        },
        {
            "label": "Task 2: Export report",
            "task": "Go to the dashboard and export the monthly report",
        },
        {
            "label": "Task 3: Update settings",
            "task": "Navigate to settings and update notification preferences",
        },
    ]
)

for entry in tasks[: int(os.getenv("LIGHTCONE_MAX_TASKS", str(len(tasks))))]:
    print(f"\n{entry['label']}")
    run_task(
        computer,
        entry["task"],
        start_url=entry.get("start_url"),
        max_steps=entry.get("max_steps", 50),
    )
