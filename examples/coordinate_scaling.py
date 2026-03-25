"""
Run the coordinate scaling example and save before/after screenshots.
"""

from tzafon import Lightcone
from PIL import Image, ImageDraw, ImageFont
import base64
import json
import io

SYSTEM_PROMPT = """\
You are controlling a computer via screenshots and actions.

Screen information:
- Viewport size: {viewport_width}x{viewport_height} pixels.
- Coordinates range from (0,0) at the top-left to (999,999) at the bottom-right.
- All coordinate values must be integers between 0 and 999 inclusive.

When you want to click on something:
- Look at the screenshot to find the element.
- Return the coordinates in the 0-999 range. They will be scaled to actual pixels.
- Click elements in their CENTER, not on edges.

Respond with JSON: {{"action": "click", "coordinate": [x, y], "reason": "..."}}
"""


def scale_coordinates(model_x, model_y, viewport_width, viewport_height):
    x = int(model_x * (viewport_width - 1) / 999)
    y = int(model_y * (viewport_height - 1) / 999)
    return x, y


def annotate_screenshot(image_bytes, pixel_x, pixel_y, model_x, model_y, output_path):
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
    VIEWPORT_WIDTH = 1280
    VIEWPORT_HEIGHT = 720

    client = Lightcone()
    output_dir = "src/assets"

    with client.computer.create(kind="browser") as computer:
        computer.navigate("https://en.wikipedia.org/wiki/Ada_Lovelace")
        computer.wait(4)

        # Take screenshot as URL (for the API) and also download for annotation
        result = computer.screenshot()
        screenshot_url = computer.get_screenshot_url(result)
        print(f"Screenshot URL: {screenshot_url}")

        # Download the screenshot for local annotation
        import urllib.request
        with urllib.request.urlopen(screenshot_url) as resp:
            screenshot_bytes = resp.read()

        # Save the "before" screenshot
        Image.open(io.BytesIO(screenshot_bytes)).save(f"{output_dir}/coordinates-before.png")
        print(f"Saved: {output_dir}/coordinates-before.png")

        # Ask the model where to click
        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            instructions=SYSTEM_PROMPT.format(
                viewport_width=VIEWPORT_WIDTH,
                viewport_height=VIEWPORT_HEIGHT,
            ),
            input=[{
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "Click the search bar."},
                    {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
                ],
            }],
        )

        # Parse response
        reply = None
        for item in response.output:
            print(f"  output item: type={item.type}")
            if item.type == "message":
                text = item.content[0].text
                print(f"  raw text: {text}")
                try:
                    reply = json.loads(text)
                except json.JSONDecodeError:
                    # Try to extract JSON from the text
                    import re
                    m = re.search(r'\{.*\}', text, re.DOTALL)
                    if m:
                        reply = json.loads(m.group())
            elif item.type == "computer_call":
                action = item.action
                print(f"  computer_call: type={action.type} x={getattr(action, 'x', None)} y={getattr(action, 'y', None)}")
                # If we got a computer_call, use those coordinates directly
                # (they're already scaled by the Responses API)
                reply = {"coordinate": [getattr(action, 'x', 500), getattr(action, 'y', 500)], "reason": f"computer_call: {action.type}", "prescaled": True}

        if not reply:
            print("No response from model!")
            return

        if reply.get("prescaled"):
            # Responses API already scaled these
            pixel_x, pixel_y = reply["coordinate"]
            # Back-calculate model coords for the annotation
            model_x = round(pixel_x * 999 / (VIEWPORT_WIDTH - 1))
            model_y = round(pixel_y * 999 / (VIEWPORT_HEIGHT - 1))
        else:
            model_x, model_y = reply["coordinate"]
            pixel_x, pixel_y = scale_coordinates(model_x, model_y, VIEWPORT_WIDTH, VIEWPORT_HEIGHT)

        print(f"Model coords: ({model_x}, {model_y})")
        print(f"Pixel coords: ({pixel_x}, {pixel_y})")

        # Save annotated "before" with crosshair
        annotate_screenshot(
            screenshot_bytes, pixel_x, pixel_y, model_x, model_y,
            f"{output_dir}/coordinates-annotated.png",
        )

        # Click it
        computer.click(pixel_x, pixel_y)
        computer.wait(2)

        # Take after screenshot
        after_result = computer.screenshot()
        after_url = computer.get_screenshot_url(after_result)
        with urllib.request.urlopen(after_url) as resp:
            after_bytes = resp.read()
        Image.open(io.BytesIO(after_bytes)).save(f"{output_dir}/coordinates-after.png")
        print(f"Saved: {output_dir}/coordinates-after.png")

    print("Done!")


if __name__ == "__main__":
    main()
