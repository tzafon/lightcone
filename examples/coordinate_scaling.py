"""
Demonstrate coordinate denormalization: Northstar outputs coordinates in a
0–1000 space; your code converts them to pixel coordinates before clicking.

Run:
    export TZAFON_API_KEY=...
    python examples/coordinate_scaling.py

Output:
    steps/coordinate-scaling-smoke/coordinates-before.png   (original screenshot)
    steps/coordinate-scaling-smoke/coordinates-annotated.png (crosshair overlay)
    steps/coordinate-scaling-smoke/coordinates-after.png    (after clicking)
"""

import io
import os
from pathlib import Path

import urllib.request
from PIL import Image, ImageDraw
from tzafon import Lightcone

client = Lightcone()

TOOL = {
    "type": "computer_use",
    "display_width": int(os.getenv("LIGHTCONE_VIEWPORT_WIDTH", "1280")),
    "display_height": int(os.getenv("LIGHTCONE_VIEWPORT_HEIGHT", "720")),
    "environment": "browser",
}

OUTPUT_DIR = Path(os.getenv("LIGHTCONE_COORDINATE_OUTPUT_DIR", "steps/coordinate-scaling"))


def _px(coord, dim):
    """Convert a 0–1000 model coordinate to a pixel coordinate."""
    return int(coord / 1000 * dim)


def annotate(image_bytes, model_x, model_y, pixel_x, pixel_y, output_path):
    """Draw a red crosshair on the screenshot to visualize the click target."""
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    draw = ImageDraw.Draw(img)
    r = 15
    draw.ellipse((pixel_x - r, pixel_y - r, pixel_x + r, pixel_y + r), outline="red", width=3)
    draw.line((pixel_x - r, pixel_y, pixel_x + r, pixel_y), fill="red", width=2)
    draw.line((pixel_x, pixel_y - r, pixel_x, pixel_y + r), fill="red", width=2)
    label = f"model=({model_x},{model_y}) pixel=({pixel_x},{pixel_y})"
    draw.text((pixel_x + r + 5, pixel_y - 10), label, fill="red")
    img.save(output_path)
    print(f"Saved: {output_path}")


def main():
    w, h = TOOL["display_width"], TOOL["display_height"]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with client.computer.create(kind="browser") as computer:
        computer.navigate(
            os.getenv("LIGHTCONE_START_URL", "https://en.wikipedia.org/wiki/Ada_Lovelace")
        )
        computer.wait(4)

        result = computer.screenshot()
        screenshot_url = computer.get_screenshot_url(result)

        with urllib.request.urlopen(screenshot_url) as resp:
            screenshot_bytes = resp.read()

        before_path = OUTPUT_DIR / "coordinates-before.png"
        Image.open(io.BytesIO(screenshot_bytes)).save(before_path)
        print(f"Saved: {before_path}")

        # Ask the model where to click. Coordinates come back in 0–1000 space.
        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            tools=[TOOL],
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": os.getenv("LIGHTCONE_COORDINATE_TASK", "Click the search bar."),
                        },
                        {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
                    ],
                }
            ],
        )

        computer_call = next(
            (item for item in (response.output or []) if item.type == "computer_call"), None
        )
        if not computer_call:
            print("No computer_call in response.")
            return

        action = computer_call.action
        model_x, model_y = action.x, action.y

        # Denormalize: 0–1000 model space → pixel coordinates.
        pixel_x = _px(model_x, w)
        pixel_y = _px(model_y, h)

        print(f"Model coords: ({model_x}, {model_y})")
        print(f"Pixel coords: ({pixel_x}, {pixel_y})  [viewport {w}×{h}]")

        annotate(
            screenshot_bytes,
            model_x,
            model_y,
            pixel_x,
            pixel_y,
            OUTPUT_DIR / "coordinates-annotated.png",
        )

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
