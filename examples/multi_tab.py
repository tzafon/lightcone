"""Multi-tab comparison — open several sites, gather info, compare.

Opens each URL in its own tab, asks Northstar to extract a value from each,
then prints a summary. Useful for price comparison, competitive analysis,
or any task that needs cross-site data.
"""

import json
import os
from tzafon import Lightcone
from _cua import get_messages, DONE_TOOL

client = Lightcone()

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "desktop",
}

URLS = [
    "https://example.com/product-a",
    "https://example.com/product-b",
    "https://example.com/product-c",
]


def ask_model_about_screenshot(screenshot_url, prompt):
    """One-shot: send a screenshot + question, get a text answer."""
    response = client.responses.create(
        model="tzafon.northstar-cua-fast",
        tools=[TOOL, DONE_TOOL],
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
                ],
            }
        ],
    )
    texts = get_messages(response.output)
    return texts[0] if texts else "(no response)"


with client.computer.create(kind="desktop") as computer:
    results = []

    for i, url in enumerate(URLS):
        if i == 0:
            computer.navigate(url)
        else:
            client.computers.tabs.create(computer.id, url=url)

        computer.wait(3)
        screenshot_url = computer.get_screenshot_url(computer.screenshot())

        answer = ask_model_about_screenshot(
            screenshot_url,
            "Look at this page and tell me the product name and price. "
            "Reply with just: <name> — $<price>",
        )
        print(f"Tab {i + 1} ({url}): {answer}")
        results.append(answer)

    # Compare results.
    summary = (
        "Here are the results:\n"
        + "\n".join(f"- {r}" for r in results)
        + "\n\nWhich is the cheapest? Reply in one sentence."
    )
    screenshot_url = computer.get_screenshot_url(computer.screenshot())
    verdict = ask_model_about_screenshot(screenshot_url, summary)
    print(f"\nVerdict: {verdict}")
