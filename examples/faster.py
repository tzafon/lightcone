"""CUA loop timing test for northstar-cua-faster-1.6

Usage:
    uv run examples/faster.py                                  # northstar-cua-faster-1.6
"""

import sys
import time
from tzafon import Lightcone
from _cua import get_computer_calls, is_done, format_action, DONE_TOOL

MODEL = sys.argv[1] if len(sys.argv) > 1 else "tzafon.northstar-cua-faster-1.6"

client = Lightcone()

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "desktop",
}

TASK = "Go to wikipedia.org and search for 'Alan Turing', then scroll to the bottom of the page and tell me what you see"


with client.computer.create(kind="desktop") as computer:
    screenshot_url = computer.get_screenshot_url(computer.screenshot())

    items = [
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": TASK},
                {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
            ],
        }
    ]

    timings = []

    for step in range(13):
        turn_start = time.perf_counter()

        t0 = time.perf_counter()
        response = client.responses.create(
            instructions="For full-page scrolling, prefer key('End')/key('Home')/key('PageDown')/key('PageUp') over repeated scroll actions.",
            model=MODEL,
            tools=[TOOL, DONE_TOOL],
            input=items,
        )
        t_model = time.perf_counter() - t0

        items.extend(response.output or [])
        print(f"[{step + 1}] {response.output}")

        if is_done(response.output):
            print(f"[{step + 1}] Task complete")
            timings.append({"step": step + 1, "model": t_model, "batch": 0.0, "screenshot": 0.0, "total": time.perf_counter() - turn_start})
            break

        calls, call_ids = get_computer_calls(response.output, TOOL)
        if not calls:
            t0 = time.perf_counter()
            screenshot_url = computer.get_screenshot_url(computer.screenshot())
            t_screenshot = time.perf_counter() - t0
            items.append({
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "Continue with the task."},
                    {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
                ],
            })
            t_total = time.perf_counter() - turn_start
            timings.append({"step": step + 1, "model": t_model, "batch": 0.0, "screenshot": t_screenshot, "total": t_total})
            print(f"[{step + 1}] no calls — nudging with fresh screenshot  model={t_model:.2f}s  screenshot={t_screenshot:.2f}s  total={t_total:.2f}s")
            continue

        for c in calls:
            print(f"[{step + 1}] {format_action(c)}")

        t0 = time.perf_counter()
        computer.batch(calls)
        t_batch = time.perf_counter() - t0
        time.sleep(1)

        t0 = time.perf_counter()
        screenshot_url = computer.get_screenshot_url(computer.screenshot())
        t_screenshot = time.perf_counter() - t0
        for call_id in call_ids:
            items.append({
                "type": "computer_call_output",
                "call_id": call_id,
                "output": {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
            })

        t_total = time.perf_counter() - turn_start
        timings.append({"step": step + 1, "model": t_model, "batch": t_batch, "screenshot": t_screenshot, "total": t_total})
        print(f"[{step + 1}] timing  model={t_model:.2f}s  batch={t_batch:.2f}s  screenshot={t_screenshot:.2f}s  total={t_total:.2f}s")

    print(f"Final state: {screenshot_url}")

    print(f"\n=== Turn timing summary — {MODEL} ===")
    print(f"{'step':>4}  {'model':>7}  {'batch':>7}  {'shot':>7}  {'total':>7}")
    for t in timings:
        print(f"{t['step']:>4}  {t['model']:>7.2f}  {t['batch']:>7.2f}  {t['screenshot']:>7.2f}  {t['total']:>7.2f}")
    if timings:
        n = len(timings)
        avg = lambda k: sum(t[k] for t in timings) / n
        print(f"{'avg':>4}  {avg('model'):>7.2f}  {avg('batch'):>7.2f}  {avg('screenshot'):>7.2f}  {avg('total'):>7.2f}  (n={n})")
