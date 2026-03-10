"""CUA loop with a persistent session for authenticated workflows.

Persistent sessions save cookies and storage state across reconnects,
so you can log in once and run multiple tasks without re-authenticating.
"""

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


def execute_action(computer, action):
    """Execute a model action on the computer session."""
    t = action.type
    if t == "click":
        computer.click(action.x, action.y)
    elif t == "double_click":
        computer.double_click(action.x, action.y)
    elif t == "right_click":
        computer.right_click(action.x, action.y)
    elif t == "type":
        computer.type(action.text)
    elif t in ("key", "keypress"):
        computer.hotkey(action.keys)
    elif t == "scroll":
        computer.scroll(
            dx=action.scroll_x or 0,
            dy=action.scroll_y or 0,
            x=action.x or 0,
            y=action.y or 0,
        )
    elif t == "navigate":
        computer.navigate(action.url)
    elif t == "drag":
        computer.drag(action.x, action.y, action.end_x, action.end_y)
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
        instructions=task,
        tools=[TOOL],
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text", "text": task},
                {"type": "input_image", "image_url": screenshot_url},
            ],
        }],
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
            input=[{
                "type": "computer_call_output",
                "call_id": computer_call.call_id,
                "output": {"type": "input_image", "image_url": screenshot_url},
            }],
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

# Log in once — cookies persist across tasks
print("\nTask 1: Log in")
run_task(computer, "Log in with username 'demo' and password 'demo123'",
         start_url="https://example.com/login")

# Subsequent tasks reuse the authenticated session
print("\nTask 2: Export report")
run_task(computer, "Go to the dashboard and export the monthly report")

print("\nTask 3: Update settings")
run_task(computer, "Navigate to settings and update notification preferences")
