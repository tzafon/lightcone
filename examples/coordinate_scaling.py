"""
Demonstrate coordinate denormalization: Northstar outputs coordinates in a
0–1000 space; your code converts them to pixel coordinates before clicking.

Run:
    export TZAFON_API_KEY=...
    python examples/coordinate_scaling.py

Output:
    steps/coordinate-scaling/coordinates-before.png     (original screenshot)
    steps/coordinate-scaling/coordinates-annotated.png  (crosshair overlay)
    steps/coordinate-scaling/coordinates-after.png      (after clicking)
"""

import io
import os
from pathlib import Path

import urllib.request
from PIL import Image, ImageDraw
from tzafon import Lightcone
from _cua import get_first_computer_call, DONE_TOOL

client = Lightcone()

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "desktop",
}

OUTPUT_DIR = Path(os.getenv("LIGHTCONE_COORDINATE_OUTPUT_DIR", "steps/coordinate-scaling"))


def annotate(image_bytes, pixel_x, pixel_y, output_path):
    """Draw a red crosshair on the screenshot to visualize the click target."""
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    draw = ImageDraw.Draw(img)
    r = 15
    draw.ellipse((pixel_x - r, pixel_y - r, pixel_x + r, pixel_y + r), outline="red", width=3)
    draw.line((pixel_x - r, pixel_y, pixel_x + r, pixel_y), fill="red", width=2)
    draw.line((pixel_x, pixel_y - r, pixel_x, pixel_y + r), fill="red", width=2)
    label = f"pixel=({pixel_x},{pixel_y})"
    draw.text((pixel_x + r + 5, pixel_y - 10), label, fill="red")
    img.save(output_path)
    print(f"Saved: {output_path}")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with client.computer.create(kind="desktop") as computer:
        computer.navigate("https://en.wikipedia.org/wiki/Ada_Lovelace")
        computer.wait(4)

        result = computer.screenshot()
        screenshot_url = computer.get_screenshot_url(result)

        with urllib.request.urlopen(screenshot_url) as resp:
            screenshot_bytes = resp.read()

        before_path = OUTPUT_DIR / "coordinates-before.png"
        Image.open(io.BytesIO(screenshot_bytes)).save(before_path)
        print(f"Saved: {before_path}")

        # Ask the model where to click. Coordinates come back in 0-1000 space.
        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            tools=[TOOL, DONE_TOOL],
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": "Click the search bar."},
                        {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
                    ],
                }
            ],
        )

        # get_first_computer_call returns a normalized dict with pixel coordinates
        action, call_id = get_first_computer_call(response.output, TOOL)
        if not action:
            print("No computer_call in response.")
            return

        pixel_x = action.get("x", 0)
        pixel_y = action.get("y", 0)
        print(f"Pixel coords: ({pixel_x}, {pixel_y})  [viewport {TOOL['display_width']}x{TOOL['display_height']}]")

        annotate(screenshot_bytes, pixel_x, pixel_y, OUTPUT_DIR / "coordinates-annotated.png")

        computer.click(pixel_x, pixel_y)
        computer.wait(2)

        after_result = computer.screenshot()
        after_url = computer.get_screenshot_url(after_result)
        with urllib.request.urlopen(after_url) as resp:
            after_bytes = resp.read()
        after_path = OUTPUT_DIR / "coordinates-after.png"
        Image.open(io.BytesIO(after_bytes)).save(after_path)
        print(f"Saved: {after_path}")

    print("Done!")


if __name__ == "__main__":
    main()
