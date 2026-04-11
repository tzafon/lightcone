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
    ...
"""

import os
import time
from pathlib import Path
from io import BytesIO

import httpx
from PIL import Image, ImageDraw
from tzafon import Lightcone
from _cua import get_computer_calls, get_messages, format_action, is_terminal_action, DONE_TOOL

client = Lightcone()

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "desktop",
}

OUTPUT_DIR = Path(os.getenv("LIGHTCONE_OUTPUT_DIR", "steps"))


def annotate_screenshot(screenshot_url, action_dict, step):
    """Download a screenshot and draw Northstar's chosen action on it."""
    img_data = httpx.get(screenshot_url).content
    img = Image.open(BytesIO(img_data))
    draw = ImageDraw.Draw(img)

    action_type = action_dict.get("type", "")

    if action_type in ("click", "double_click", "triple_click", "right_click") and action_dict.get("x") is not None:
        px, py = action_dict["x"], action_dict["y"]
        r = 18
        draw.ellipse((px - r, py - r, px + r, py + r), fill="red", outline="darkred", width=3)
        draw.line((px - r, py, px + r, py), fill="white", width=2)
        draw.line((px, py - r, px, py + r), fill="white", width=2)

    elif action_type == "type" and action_dict.get("text"):
        draw.rectangle((0, 0, img.width, 40), fill=(0, 0, 0, 180))
        draw.text((10, 8), f'type: "{action_dict["text"]}"', fill="yellow")

    elif action_type in ("key", "keypress") and action_dict.get("keys"):
        draw.rectangle((0, 0, img.width, 40), fill=(0, 0, 0, 180))
        draw.text((10, 8), f"key: {'+'.join(action_dict['keys'])}", fill="cyan")

    elif action_type == "scroll" and action_dict.get("x") is not None:
        px, py = action_dict["x"], action_dict["y"]
        direction = "down" if (action_dict.get("scroll_y") or 0) > 0 else "up"
        draw.text((px - 10, py - 10), direction, fill="orange")

    elif action_type == "navigate" and action_dict.get("url"):
        draw.rectangle((0, 0, img.width, 40), fill=(0, 0, 0, 180))
        draw.text((10, 8), f"navigate: {action_dict['url']}", fill="lime")

    label = f"Step {step}: {action_type}"
    draw.rectangle((0, img.height - 32, len(label) * 8 + 20, img.height), fill=(0, 0, 0, 200))
    draw.text((10, img.height - 26), label, fill="white")

    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / f"step-{step:02d}-{action_type}.png"
    img.save(path)
    return path


with client.computer.create(kind="desktop") as computer:
    screenshot_url = computer.get_screenshot_url(computer.screenshot())

    items = [
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Open the terminal, run 'uname -a', and tell me what operating system this is"},
                {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
            ],
        }
    ]

    step = 0
    for step in range(1, 21):
        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            tools=[TOOL, DONE_TOOL],
            input=items,
        )
        items.extend(response.output or [])

        calls, call_ids = get_computer_calls(response.output, TOOL)
        if not calls:
            break

        if any(is_terminal_action(c) for c in calls):
            print(f"[{step}] {format_action(calls[0])}")
            break

        # Annotate BEFORE executing — shows what Northstar decided to do.
        for c in calls:
            path = annotate_screenshot(screenshot_url, c, step)
            print(f"[{step}] {format_action(c):>30}  ->  {path}")

        computer.batch(calls)
        time.sleep(1)

        screenshot_url = computer.get_screenshot_url(computer.screenshot())
        for call_id in call_ids:
            items.append({
                "type": "computer_call_output",
                "call_id": call_id,
                "output": {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
            })

    # Save final state
    final_data = httpx.get(screenshot_url).content
    final_img = Image.open(BytesIO(final_data))
    OUTPUT_DIR.mkdir(exist_ok=True)
    final_path = OUTPUT_DIR / f"step-{step:02d}-final.png"
    final_img.save(final_path)
    print(f"\nFinal state  ->  {final_path}")

    for text in get_messages(response.output):
        print(f"\nNorthstar: {text}")

    print(f"\nAll steps saved to {OUTPUT_DIR}/")
