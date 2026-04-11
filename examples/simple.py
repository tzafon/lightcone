"""Simple CUA loop — screenshot, think, act, repeat."""

import json
import os
import time
from tzafon import Lightcone
from _cua import get_computer_calls, is_done, print_messages, format_action, DONE_TOOL

client = Lightcone()

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "desktop",
}


with client.computer.create(kind="desktop") as computer:
    screenshot_url = computer.get_screenshot_url(computer.screenshot())

    items = [
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Go to wikipedia.org and search for 'Alan Turing'"},
                {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
            ],
        }
    ]

    for step in range(50):
        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            tools=[TOOL, DONE_TOOL],
            input=items,
        )

        items.extend(response.output or [])
        print_messages(response.output)

        if is_done(response.output):
            print(f"[{step + 1}] Task complete")
            break

        calls, call_ids = get_computer_calls(response.output, TOOL)
        if not calls:
            break

        for c in calls:
            print(f"[{step + 1}] {format_action(c)}")

        computer.batch(calls)
        time.sleep(1)

        screenshot_url = computer.get_screenshot_url(computer.screenshot())
        print(f"[{step + 1}] Screenshot URL: {screenshot_url}")
        for call_id in call_ids:
            items.append({
                "type": "computer_call_output",
                "call_id": call_id,
                "output": {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
            })

    print(f"Final state: {screenshot_url}")
