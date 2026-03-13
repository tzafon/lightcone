"""Desktop session mixing browser actions with shell commands.

Uses kind="desktop" for full OS access — Northstar can browse the web,
open a terminal, run scripts, and pipe data between them.
"""

import os
from tzafon import Lightcone

client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "desktop",
}
TASK = (
    "Open Firefox and download the CSV from https://example.com/data.csv, "
    "then open a terminal and run: python3 -c \"import csv; "
    "data=list(csv.reader(open('/tmp/data.csv'))); print(len(data), 'rows')\""
)
MAX_STEPS = 75


def execute_action(computer, action):
    """Execute a model action on the computer session."""
    t = action.type
    if t == "click":
        computer.click(action.x, action.y)
    elif t == "double_click":
        computer.double_click(action.x, action.y)
    elif t == "triple_click":
        computer.click(action.x, action.y)
        computer.click(action.x, action.y)
        computer.click(action.x, action.y)
    elif t == "right_click":
        computer.right_click(action.x, action.y)
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
            x=action.x or 0,
            y=action.y or 0,
        )
    elif t == "hscroll":
        computer.scroll(
            dx=action.scroll_x or 0,
            dy=0,
            x=action.x or 0,
            y=action.y or 0,
        )
    elif t == "navigate":
        computer.navigate(action.url)
    elif t == "drag":
        computer.drag(action.x, action.y, action.end_x, action.end_y)
    elif t == "wait":
        computer.wait(2)


with client.computer.create(kind="desktop") as computer:
    # Run a shell command directly before handing off to the CUA loop.
    # Useful for setup — install packages, seed files, set env vars.
    result = computer.debug("mkdir -p /tmp && echo 'ready'")
    print(f"Shell: {computer.get_debug_response(result)}")

    screenshot_url = computer.get_screenshot_url(computer.screenshot())

    response = client.responses.create(
        model="tzafon.northstar-cua-fast",
        tools=[TOOL],
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text", "text": TASK},
                {"type": "input_image", "image_url": screenshot_url},
            ],
        }],
    )

    for step in range(MAX_STEPS):
        computer_call = next(
            (o for o in (response.output or []) if o.type == "computer_call"), None
        )
        if not computer_call:
            break

        action = computer_call.action
        print(f"[{step + 1}] {action.type}", end="")
        if action.text:
            print(f" '{action.text}'", end="")
        print()

        if action.type in ("terminate", "done", "answer"):
            print(f"Result: {action.result or action.text or action.status}")
            break

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

    # After the CUA loop, inspect the result with a shell command.
    result = computer.debug("ls -la /tmp/*.csv 2>/dev/null || echo 'no CSV found'")
    print(f"\nShell check: {computer.get_debug_response(result)}")
