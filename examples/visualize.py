"""Visualize Northstar's decisions — save an annotated screenshot at every step.

Runs a CUA loop and produces a sequence of images showing exactly where
Northstar clicked, what it typed, and how it navigated. Useful for debugging,
demos, and documentation.

Usage:
    pip install Pillow httpx
    export TZAFON_API_KEY=...
    python examples/visualize.py

Output:
    steps/step-01-click.png
    steps/step-02-type.png
    steps/step-03-click.png
    ...
"""

import os
from pathlib import Path

import httpx
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from tzafon import Lightcone

client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "desktop",
}
TASK = "Open the terminal, run 'uname -a', and tell me what operating system this is"
MAX_STEPS = 20
OUTPUT_DIR = Path("steps")


def annotate_screenshot(screenshot_url: str, action, step: int) -> Path:
    """Download a screenshot and draw Northstar's chosen action on it."""
    img_data = httpx.get(screenshot_url).content
    img = Image.open(BytesIO(img_data))
    draw = ImageDraw.Draw(img)

    # Scale from display coordinates to actual image pixels
    scale_x = img.width / 1280
    scale_y = img.height / 720

    # Draw the action
    if action.type in ("click", "double_click", "triple_click", "right_click") and action.x is not None:
        px, py = int(action.x * scale_x), int(action.y * scale_y)
        r = 18
        # Red crosshair
        draw.ellipse((px - r, py - r, px + r, py + r), fill="red", outline="darkred", width=3)
        draw.line((px - r, py, px + r, py), fill="white", width=2)
        draw.line((px, py - r, px, py + r), fill="white", width=2)

    elif action.type == "type" and action.text:
        # Yellow text banner at the top
        draw.rectangle((0, 0, img.width, 40), fill=(0, 0, 0, 180))
        draw.text((10, 8), f'type: "{action.text}"', fill="yellow")

    elif action.type in ("key", "keypress") and action.keys:
        draw.rectangle((0, 0, img.width, 40), fill=(0, 0, 0, 180))
        draw.text((10, 8), f"key: {'+'.join(action.keys)}", fill="cyan")

    elif action.type == "scroll" and action.x is not None:
        px, py = int(action.x * scale_x), int(action.y * scale_y)
        direction = "↓" if (action.scroll_y or 0) > 0 else "↑"
        draw.text((px - 10, py - 10), direction, fill="orange")

    elif action.type == "navigate" and action.url:
        draw.rectangle((0, 0, img.width, 40), fill=(0, 0, 0, 180))
        draw.text((10, 8), f"navigate: {action.url}", fill="lime")

    # Step label in bottom-left
    label = f"Step {step}: {action.type}"
    draw.rectangle((0, img.height - 32, len(label) * 8 + 20, img.height), fill=(0, 0, 0, 200))
    draw.text((10, img.height - 26), label, fill="white")

    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / f"step-{step:02d}-{action.type}.png"
    img.save(path)
    return path


def execute_action(computer, action):
    """Execute a model action on the computer."""
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


with client.computer.create(kind="desktop") as computer:
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

    for step in range(1, MAX_STEPS + 1):
        computer_call = next(
            (o for o in (response.output or []) if o.type == "computer_call"), None
        )
        if not computer_call:
            break

        action = computer_call.action

        if action.type in ("terminate", "done", "answer"):
            print(f"[{step}] {action.type}: {action.result or action.text}")
            break

        # Annotate the screenshot BEFORE executing the action —
        # this shows what Northstar is looking at and what it decided to do.
        path = annotate_screenshot(screenshot_url, action, step)
        print(f"[{step}] {action.type:>12}  →  {path}")

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

    # Save the final state too
    final_data = httpx.get(screenshot_url).content
    final_img = Image.open(BytesIO(final_data))
    OUTPUT_DIR.mkdir(exist_ok=True)
    final_path = OUTPUT_DIR / f"step-{step:02d}-final.png"
    final_img.save(final_path)
    print(f"\nFinal state  →  {final_path}")

    # Print any text response from Northstar
    for item in response.output or []:
        if item.type == "message":
            for block in item.content or []:
                if block.text:
                    print(f"\nNorthstar: {block.text}")

    print(f"\nAll steps saved to {OUTPUT_DIR}/")
