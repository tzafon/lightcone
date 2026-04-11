"""Competitor research — gather structured data from any website.

With Playwright/Selenium, you'd need custom selectors for every
site, and they'd break whenever the site redesigns. With Lightcone, Northstar
just reads the screen like a human would.

Demonstrates the two-phase pattern:
  Phase 1 (explore): CUA loop WITH tools — Northstar scrolls, dismisses popups, etc.
  Phase 2 (extract): Request WITHOUT tools — forces a text/JSON response.

Usage:
    export TZAFON_API_KEY=your-key
    python competitor_research.py
"""

import json
import os
import time
from tzafon import Lightcone
from _cua import get_computer_calls, get_messages, format_action, is_terminal_action, DONE_TOOL

client = Lightcone()

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "desktop",
}

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


def research_page(computer, url, prompt, max_explore_steps=10):
    """Navigate to a URL, let Northstar explore, then extract structured data."""
    computer.navigate(url)
    computer.wait(3)

    # --- Phase 1: Explore with CUA loop ---
    screenshot_url = computer.get_screenshot_url(computer.screenshot())
    items = [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Scroll down slowly. Dismiss any popups or cookie banners. "
                            "Stop when you can see transaction fees or per-payment pricing.",
                },
                {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
            ],
        }
    ]

    for step in range(max_explore_steps):
        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            tools=[TOOL, DONE_TOOL],
            input=items,
        )
        items.extend(response.output or [])

        calls, call_ids = get_computer_calls(response.output, TOOL)
        if not calls or any(is_terminal_action(c) for c in calls):
            break

        for c in calls:
            print(f"    [{step + 1}] {format_action(c)}")

        computer.batch(calls)
        time.sleep(1)

        screenshot_url = computer.get_screenshot_url(computer.screenshot())
        for call_id in call_ids:
            items.append({
                "type": "computer_call_output",
                "call_id": call_id,
                "output": {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
            })

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
    )

    texts = get_messages(extraction.output)
    return texts[0] if texts else None


def main():
    print("=" * 60)
    print("  Competitor Pricing Research")
    print("  No selectors. No scraping. Just vision.")
    print("=" * 60)

    results = []

    with client.computer.create(kind="desktop") as computer:
        for company in COMPANIES:
            print(f"\n--- Researching {company['name']} ---")
            print(f"    URL: {company['url']}")

            raw = research_page(computer, company["url"], EXTRACT_PROMPT)

            if raw:
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

    print("\n" + "=" * 60)
    print("  RESULTS")
    print("=" * 60)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
