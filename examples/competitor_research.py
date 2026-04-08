"""Competitor research — gather structured data from any website.

With Playwright/Selenium, you'd need custom selectors for every
site, and they'd break whenever the site redesigns. With Lightcone, Northstar
just reads the screen like a human would..

Demonstrates the two-phase pattern:
  Phase 1 (explore): CUA loop WITH tools — Northstar scrolls, dismisses popups, etc.
  Phase 2 (extract): Request WITHOUT tools — forces a text/JSON response.

Usage:
    export TZAFON_API_KEY=your-key
    python competitor_research.py
"""

import json
import os
from tzafon import Lightcone

client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "browser",
}

# Sites with different layouts
COMPANIES = [
    {"name": "Stripe", "url": "https://stripe.com/pricing"},
    {"name": "Square", "url": "https://squareup.com/us/en/pricing"},
    {"name": "PayPal", "url": "https://www.paypal.com/us/business/accept-payments"},
]

EXTRACT_PROMPT = """Look at this pricing page and extract the following as JSON:
{
  "company": "...",
  "main_product": "...",
  "transaction_fee_percent": "...",
  "per_transaction_fee": "...",
  "monthly_fee": "...",
  "notable_features": ["...", "..."]
}
Reply with ONLY the JSON, no other text."""


def _px(coord, dim):
    """Convert a 0–1000 model coordinate to a pixel coordinate."""
    return int(coord / 1000 * dim)


def execute_action(computer, action):
    """Execute a single model action on the computer session."""
    w, h = TOOL["display_width"], TOOL["display_height"]
    t = action.type
    if t == "click":
        computer.click(_px(action.x, w), _px(action.y, h))
    elif t == "double_click":
        computer.double_click(_px(action.x, w), _px(action.y, h))
    elif t == "type":
        computer.type(action.text)
    elif t in ("key", "keypress"):
        computer.hotkey(action.keys)
    elif t == "scroll":
        computer.scroll(
            dx=action.scroll_x or 0,
            dy=action.scroll_y or 0,
            x=_px(action.x or 0, w),
            y=_px(action.y or 0, h),
        )
    elif t == "navigate":
        computer.navigate(action.url)
    elif t == "wait":
        computer.wait(2)


def extract_text_response(response):
    """Pull the text content out of a model response."""
    for item in response.output or []:
        if item.type == "message":
            for block in item.content or []:
                if block.text:
                    return block.text
    return None


def research_page(computer, url, prompt, max_explore_steps=10):
    """Navigate to a URL, let Northstar explore, then extract structured data.

    Two-phase pattern:
      Phase 1: CUA loop WITH tools — Northstar scrolls, dismisses popups,
               clicks "show more", etc. to reveal the full page content.
      Phase 2: Extraction WITHOUT tools — forces the model to respond with
               text instead of actions.
    """
    computer.navigate(url)
    computer.wait(3)

    # --- Phase 1: Explore with the CUA loop ---
    screenshot_url = computer.get_screenshot_url(computer.screenshot())
    response = client.responses.create(
        model="tzafon.northstar-cua-fast",
        tools=[TOOL],
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Scroll down slowly. Dismiss any popups or cookie banners. Stop when you can see transaction fees or per-payment pricing.",
                    },
                    {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
                ],
            }
        ],
    )

    for step in range(max_explore_steps):
        computer_call = next(
            (o for o in (response.output or []) if o.type == "computer_call"), None
        )
        if not computer_call:
            break

        action = computer_call.action
        print(f"    [{step + 1}] {action.type}", end="")
        if action.x is not None:
            print(f" @ ({action.x}, {action.y})", end="")
        print()

        if action.type == "terminate":
            break
        elif action.type == "answer":
            break
        elif action.type == "done":
            break

        execute_action(computer, action)
        computer.wait(1)

        screenshot_url = computer.get_screenshot_url(computer.screenshot())
        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            previous_response_id=response.id,
            tools=[TOOL],
            input=[
                {
                    "type": "computer_call_output",
                    "call_id": computer_call.call_id,
                    "output": {
                        "type": "input_image",
                        "image_url": screenshot_url,
                        "detail": "auto",
                    },
                }
            ],
        )

    # --- Phase 2: Extract structured data (no tools = text response) ---
    print("    [extract]")
    screenshot_url = computer.get_screenshot_url(computer.screenshot())
    extraction = client.responses.create(
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
        # No tools — forces a text response instead of actions.
    )

    return extract_text_response(extraction)


def main():
    print("=" * 60)
    print("  Competitor Pricing Research")
    print("  No selectors. No scraping. Just vision.")
    print("=" * 60)

    results = []

    with client.computer.create(kind="browser") as computer:
        for company in COMPANIES:
            print(f"\n--- Researching {company['name']} ---")
            print(f"    URL: {company['url']}")

            raw = research_page(
                computer,
                company["url"],
                EXTRACT_PROMPT,
                max_explore_steps=int(os.getenv("LIGHTCONE_MAX_EXPLORE_STEPS", "10")),
            )

            if raw:
                # Try to parse as JSON; if the model wrapped it in markdown, strip that.
                cleaned = raw.strip().removeprefix("```json").removesuffix("```").strip()
                try:
                    data = json.loads(cleaned)
                    results.append(data)
                    print(
                        f"    -> {data.get('main_product', '?')}: "
                        f"{data.get('transaction_fee_percent', '?')} + "
                        f"{data.get('per_transaction_fee', '?')}/txn"
                    )
                except json.JSONDecodeError:
                    print(f"    -> Raw response: {raw[:200]}")
                    results.append({"company": company["name"], "raw": raw})
            else:
                print("    -> No response from model")

    # Summary
    print("\n" + "=" * 60)
    print("  RESULTS")
    print("=" * 60)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
