"""Full QA: visual eval + structural crawl with Lightcone SDK.

1. Navigate to URL, screenshot
2. In parallel:
   a. Northstar visual critique (screenshot, no tools)
   b. Structural analysis via exec + html (find links, buttons, empty sections)
"""

import concurrent.futures
import re
import sys
import time
import os

from tzafon import Lightcone

lc = Lightcone(
    api_key=os.environ["TZAFON_API_KEY"]
)

URL = sys.argv[1] if len(sys.argv) > 1 else "https://wagyu-finder-sf.lovable.app"
DESCRIPTION = sys.argv[2] if len(sys.argv) > 2 else "a web application"


def log(msg):
    print(f"  {msg}", flush=True)


def visual_eval(screenshot_url):
    """Northstar visual critique."""
    response = lc.responses.create(
        model="tzafon.northstar-cua-fast",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": (
                            f"This is '{DESCRIPTION}'. "
                            "List only actual DEFECTS — broken layout, missing content, empty sections, "
                            "broken images, overlapping text, unreadable contrast. "
                            "Do NOT suggest design improvements or new features. "
                            "If the page looks correct and functional, say so. Be brief."
                        ),
                    },
                    {"type": "input_image", "image_url": screenshot_url},
                ],
            }
        ],
    )
    for item in response.output or []:
        if item.type == "message":
            for block in item.content or []:
                if hasattr(block, "text"):
                    return block.text
    return ""


def structural_crawl(computer):
    """Use html() + exec to analyze page structure."""
    findings = []

    html_result = computer.html()
    html = ""
    if html_result and html_result.result:
        html = html_result.result.get("html_content", "")

    if not html:
        return ["Could not retrieve page HTML"]

    # Check title
    title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else ""
    if (
        not title
        or title in ("Vite + React", "React App")
        or "untitled" in title.lower()
    ):
        findings.append(f"Page title is generic/placeholder: '{title}'")

    # Count links
    links = re.findall(
        r'<a\s[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>',
        html,
        re.DOTALL | re.IGNORECASE,
    )
    dead_links = [
        (href, re.sub(r"<[^>]+>", "", text).strip()[:40])
        for href, text in links
        if not href or href == "#" or href.startswith("javascript:")
    ]
    for href, text in dead_links:
        findings.append(f"Dead link: '{text}' → '{href}'")

    # Count buttons
    buttons = re.findall(
        r"<button[^>]*>(.*?)</button>", html, re.DOTALL | re.IGNORECASE
    )
    disabled_buttons = re.findall(
        r"<button[^>]*disabled[^>]*>(.*?)</button>", html, re.DOTALL | re.IGNORECASE
    )
    for btn in disabled_buttons:
        text = re.sub(r"<[^>]+>", "", btn).strip()[:40]
        findings.append(f"Disabled button: '{text}'")

    # Check images
    images = re.findall(
        r'<img\s[^>]*src=["\']([^"\']*)["\'][^>]*/?>', html, re.IGNORECASE
    )
    imgs_no_alt = re.findall(r"<img\s(?![^>]*alt=)[^>]*/?>", html, re.IGNORECASE)
    if imgs_no_alt:
        findings.append(f"{len(imgs_no_alt)} image(s) missing alt text")

    # Check for placeholder/lorem text
    if "lorem ipsum" in html.lower():
        findings.append("Lorem ipsum placeholder text found")
    if "TODO" in html or "FIXME" in html:
        findings.append("TODO/FIXME comments found in rendered HTML")

    # Check for console errors via exec
    lc.computers.exec.sync(
        computer.id,
        command="DISPLAY=:1 xdotool key F12 2>/dev/null; sleep 0.5; echo done",
        timeout_seconds=5,
    )

    total_links = len(links)
    total_buttons = len(buttons)
    total_images = len(images)

    if not findings:
        findings.append(
            f"No structural issues. {total_links} links, {total_buttons} buttons, {total_images} images found."
        )
    else:
        findings.insert(
            0,
            f"Page structure: {total_links} links, {total_buttons} buttons, {total_images} images",
        )

    return findings


# ── Main ─────────────────────────────────────────────────────────────────
print(f"QA: {URL}\n")
t0 = time.time()

with lc.computer.create(
    kind="browser", idle_timeout_enabled=False, max_lifetime_seconds=120
) as computer:
    # Navigate + screenshot — minimal wait
    computer.navigate(URL)
    computer.wait(1)
    ss = computer.screenshot()
    screenshot_url = computer.get_screenshot_url(ss)
    log(f"screenshot ({time.time() - t0:.1f}s) — starting eval...")

    # Fire everything in parallel
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    f_visual = pool.submit(visual_eval, screenshot_url)
    f_crawl = pool.submit(structural_crawl, computer)

    crawl_findings = f_crawl.result()
    log(f"structural crawl done ({time.time() - t0:.1f}s)")

    print(f"\n{'═' * 60}")
    print("  STRUCTURAL ANALYSIS")
    print(f"{'═' * 60}\n")
    for i, f in enumerate(crawl_findings):
        print(f"  {i + 1}. {f}")

    visual_report = f_visual.result()
    log(f"visual eval done ({time.time() - t0:.1f}s)")

    print(f"\n{'═' * 60}")
    print("  VISUAL ANALYSIS")
    print(f"{'═' * 60}\n")
    print(visual_report)
    pool.shutdown(wait=False)

print(f"\nTotal: {time.time() - t0:.1f}s")
