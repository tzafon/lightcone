"""Simple CUA loop — screenshot, think, act, repeat."""

import os
from tzafon import Lightcone

client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "browser",
}
TASK = "Go to wikipedia.org and search for 'Alan Turing'"
MAX_STEPS = 50


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


with client.computer.create(kind="browser") as computer:
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
        label = action.type
        if action.x is not None:
            label += f" @ ({action.x}, {action.y})"
        if action.text:
            label += f" '{action.text}'"
        print(f"[{step + 1}] {label}")

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

    for item in response.output or []:
        if item.type == "message":
            for block in item.content or []:
                if block.text:
                    print(block.text)
