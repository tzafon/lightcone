"""Screenshot-only observer — no actions, just watching and describing.

Takes periodic screenshots of a page and asks the model what it sees.
Useful for dashboard monitoring, visual regression detection, or
watching a long-running process.
"""

import os
import time
from datetime import datetime
from tzafon import Lightcone

client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

URL = "https://example.com/dashboard"
INTERVAL_SECONDS = 30
MAX_CHECKS = 100
PROMPT = (
    "Describe what you see on this screen. Note any errors, warnings, "
    "unusual values, or changes from what you'd expect on a healthy dashboard. "
    "Be concise — one paragraph."
)


with client.computer.create(kind="browser") as computer:
    computer.navigate(URL)
    computer.wait(3)

    previous_description = None

    for i in range(MAX_CHECKS):
        screenshot_url = computer.get_screenshot_url(computer.screenshot())

        prompt = PROMPT
        if previous_description:
            prompt += f"\n\nPrevious observation: {previous_description}"
            prompt += "\n\nFlag anything that changed."

        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            input=[{
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {"type": "input_image", "image_url": screenshot_url},
                ],
            }],
        )

        # Extract the model's description (it may come as a message or reasoning).
        description = ""
        for item in response.output or []:
            if item.type == "message":
                for block in item.content or []:
                    if block.text:
                        description += block.text

        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Check {i + 1}/{MAX_CHECKS}")
        print(f"  {description or '(no description)'}")
        print()

        previous_description = description

        if i < MAX_CHECKS - 1:
            # Refresh the page before the next check.
            computer.navigate(URL)
            computer.wait(2)
            time.sleep(INTERVAL_SECONDS)
