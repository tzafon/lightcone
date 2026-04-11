"""Screenshot-only observer — no actions, just watching and describing.

Takes periodic screenshots of a page and asks the model what it sees.
Useful for dashboard monitoring, visual regression detection, or
watching a long-running process.
"""

import os
import time
from datetime import datetime
from tzafon import Lightcone
from _cua import get_messages

client = Lightcone()

URL = os.getenv("LIGHTCONE_URL", "https://example.com/dashboard")


with client.computer.create(kind="desktop") as computer:
    computer.navigate(URL)
    computer.wait(3)

    previous_description = None

    for i in range(100):
        screenshot_url = computer.get_screenshot_url(computer.screenshot())

        prompt = (
            "Describe what you see on this screen. Note any errors, warnings, "
            "unusual values, or changes from what you'd expect on a healthy dashboard. "
            "Be concise — one paragraph."
        )
        if previous_description:
            prompt += f"\n\nPrevious observation: {previous_description}"
            prompt += "\n\nFlag anything that changed."

        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
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

        descriptions = get_messages(response.output)
        description = " ".join(descriptions)

        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Check {i + 1}")
        print(f"  {description or '(no description)'}")
        print()

        previous_description = description

        if i < 99:
            computer.navigate(URL)
            computer.wait(2)
            time.sleep(30)
