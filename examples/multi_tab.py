"""Multi-tab comparison — open several sites, gather info, compare.

Opens each URL in its own tab, asks the model to extract a value from each,
then prints a summary. Useful for price comparison, competitive analysis,
or any task that needs cross-site data.
"""

import os
from tzafon import Lightcone

client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "browser",
}

URLS = [
    "https://example.com/product-a",
    "https://example.com/product-b",
    "https://example.com/product-c",
]
EXTRACT_PROMPT = "Look at this page and tell me the product name and price. Reply with just: <name> — $<price>"
COMPARE_PROMPT = "Here are the results:\n{results}\n\nWhich is the cheapest? Reply in one sentence."


def ask_model_about_screenshot(screenshot_url, prompt):
    """One-shot: send a screenshot + question, get a text answer."""
    response = client.responses.create(
        model="tzafon.northstar-cua-fast",
        tools=[TOOL],
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": screenshot_url},
            ],
        }],
    )
    for item in response.output or []:
        if item.type == "message":
            for block in item.content or []:
                if block.text:
                    return block.text
    return "(no response)"


with client.computer.create(kind="browser") as computer:
    results = []

    for i, url in enumerate(URLS):
        if i == 0:
            # First URL: navigate in the initial tab.
            computer.navigate(url)
        else:
            # Subsequent URLs: open a new tab.
            client.computers.tabs.create(computer.id, url=url)

        computer.wait(3)
        screenshot_url = computer.get_screenshot_url(computer.screenshot())

        answer = ask_model_about_screenshot(screenshot_url, EXTRACT_PROMPT)
        print(f"Tab {i + 1} ({url}): {answer}")
        results.append(answer)

    # Compare results.
    summary = COMPARE_PROMPT.format(results="\n".join(f"- {r}" for r in results))

    # Take a final screenshot (doesn't matter which tab) for context.
    screenshot_url = computer.get_screenshot_url(computer.screenshot())
    verdict = ask_model_about_screenshot(screenshot_url, summary)
    print(f"\nVerdict: {verdict}")
