"""Evaluate Northstar on a real enterprise workflow.

Runs a task against a live demo app, prints each step, and reports
a pass/fail verdict with timing and step count.

Usage:
    export TZAFON_API_KEY=sk_...
    python -m examples.harness.evaluate

    # With screenshots saved:
    python -m examples.harness.evaluate --screenshots steps/

    # Custom task:
    python -m examples.harness.evaluate \
        --url "https://opensource-demo.orangehrmlive.com/" \
        --instruction "Log in with Admin/admin123, go to PIM, add employee Test Northstar"
"""

from __future__ import annotations

import argparse
import os
import time
from pathlib import Path

from tzafon import Lightcone

from .runner import ActionEvent, CuaRunner, MessageEvent, RunConfig, RunResult

# Default: OrangeHRM add employee
DEFAULT_URL = "https://opensource-demo.orangehrmlive.com/"
DEFAULT_INSTRUCTION = (
    "Log in with username 'Admin' and password 'admin123'. "
    "Navigate to PIM > Add Employee. "
    "Fill in First Name 'Test', Last Name 'Northstar'. "
    "Click Save. "
    "Verify the employee was created successfully."
)


def make_action_printer(screenshot_dir: Path | None = None):
    """Return an on_action callback that prints steps and optionally saves screenshots."""

    def print_action(event: ActionEvent) -> None:
        action = event.action
        label = action.type
        if getattr(action, "x", None) is not None:
            label += f" @ ({action.x}, {action.y})"
        if getattr(action, "text", None):
            label += f" '{action.text[:40]}'"
        if getattr(action, "url", None):
            label += f" {action.url}"

        # Print screenshot URL inline so you can click it
        if event.screenshot_url:
            print(f"  [{event.step:2d}] {label}")
            print(f"       {event.screenshot_url}")
        else:
            print(f"  [{event.step:2d}] {label}")

        # Save annotated screenshot if requested
        if screenshot_dir and event.screenshot_url:
            try:
                import httpx
                from io import BytesIO
                from PIL import Image, ImageDraw

                img_data = httpx.get(event.screenshot_url).content
                img = Image.open(BytesIO(img_data))
                draw = ImageDraw.Draw(img)

                sx = img.width / 1280
                sy = img.height / 720

                if (
                    action.type in ("click", "double_click", "triple_click", "right_click")
                    and getattr(action, "x", None) is not None
                ):
                    px, py = int(action.x * sx), int(action.y * sy)
                    r = 18
                    draw.ellipse(
                        (px - r, py - r, px + r, py + r), fill="red", outline="darkred", width=3
                    )
                    draw.line((px - r, py, px + r, py), fill="white", width=2)
                    draw.line((px, py - r, px, py + r), fill="white", width=2)
                elif action.type == "type" and getattr(action, "text", None):
                    draw.rectangle((0, 0, img.width, 36), fill=(0, 0, 0, 180))
                    draw.text((10, 8), f'type: "{action.text[:60]}"', fill="yellow")
                elif action.type in ("key", "keypress") and getattr(action, "keys", None):
                    draw.rectangle((0, 0, img.width, 36), fill=(0, 0, 0, 180))
                    draw.text((10, 8), f"key: {'+'.join(action.keys)}", fill="cyan")

                label_text = f"Step {event.step}: {action.type}"
                draw.rectangle(
                    (0, img.height - 28, len(label_text) * 8 + 16, img.height), fill=(0, 0, 0, 200)
                )
                draw.text((8, img.height - 22), label_text, fill="white")

                path = screenshot_dir / f"step-{event.step:02d}-{action.type}.png"
                img.save(path)
            except ImportError:
                pass  # Pillow/httpx not installed — skip annotation

    return print_action


def print_message(event: MessageEvent) -> None:
    print(f"  [{event.step:2d}] Northstar: {event.text[:100]}")


def evaluate(result: RunResult, max_steps: int) -> dict:
    """Score a run and return a verdict."""
    completed = result.status in ("completed", "completed_no_action")
    has_message = result.final_message is not None

    if completed and has_message:
        verdict = "PASS"
    elif completed:
        verdict = "PASS (no message)"
    elif result.status == "max_steps_exceeded" and has_message:
        verdict = "PARTIAL"
    else:
        verdict = "FAIL"

    return {
        "verdict": verdict,
        "status": result.status,
        "steps": result.steps,
        "message": result.final_message,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate Northstar on a workflow")
    parser.add_argument("--url", default=DEFAULT_URL, help="Start URL")
    parser.add_argument("--instruction", default=DEFAULT_INSTRUCTION, help="Task instruction")
    parser.add_argument("--max-steps", type=int, default=25, help="Max steps")
    parser.add_argument("--kind", default="browser", help="Environment kind (browser/desktop)")
    parser.add_argument("--runs", type=int, default=1, help="Number of runs")
    parser.add_argument("--trace", default=None, help="Path to save JSONL trace")
    parser.add_argument(
        "--screenshots", default=None, help="Directory to save annotated screenshots"
    )
    args = parser.parse_args()

    client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

    screenshot_dir = None
    if args.screenshots:
        screenshot_dir = Path(args.screenshots)
        screenshot_dir.mkdir(parents=True, exist_ok=True)

    print(f"Target:      {args.url}")
    print(f"Instruction: {args.instruction[:80]}...")
    print(f"Max steps:   {args.max_steps}")
    print(f"Runs:        {args.runs}")
    if screenshot_dir:
        print(f"Screenshots: {screenshot_dir}/")
    print()

    verdicts = []

    for run_num in range(1, args.runs + 1):
        if args.runs > 1:
            print(f"--- Run {run_num}/{args.runs} ---")

        trace_path = args.trace
        if trace_path and args.runs > 1:
            trace_path = trace_path.replace(".jsonl", f"_run{run_num}.jsonl")

        run_screenshot_dir = screenshot_dir
        if run_screenshot_dir and args.runs > 1:
            run_screenshot_dir = screenshot_dir / f"run{run_num}"
            run_screenshot_dir.mkdir(parents=True, exist_ok=True)

        runner = CuaRunner(
            client,
            config=RunConfig(
                model="tzafon.northstar-cua-fast",
                kind=args.kind,
                max_steps=args.max_steps,
                print_progress=False,
                trace_path=trace_path,
            ),
            on_action=make_action_printer(run_screenshot_dir),
            on_message=print_message,
        )

        start = time.time()
        result = runner.run(args.instruction, start_url=args.url)
        elapsed = time.time() - start

        verdict = evaluate(result, args.max_steps)
        verdicts.append(verdict)

        print()
        print(f"  [{verdict['verdict']}]  {result.steps} steps in {elapsed:.1f}s")
        if result.final_message:
            print(f"  Northstar: {result.final_message[:120]}")
        if result.last_screenshot_url:
            print(f"  Final:     {result.last_screenshot_url}")
        if trace_path:
            print(f"  Trace:     {trace_path}")
        if run_screenshot_dir:
            print(f"  Screenshots: {run_screenshot_dir}/")
        print()

    # Summary
    if args.runs > 1:
        passes = sum(1 for v in verdicts if v["verdict"].startswith("PASS"))
        print("=" * 50)
        print(
            f"  {passes}/{args.runs} PASS  |  "
            f"Avg steps: {sum(v['steps'] for v in verdicts) / len(verdicts):.0f}  |  "
            f"Reliability: {passes / args.runs * 100:.0f}%"
        )
        print("=" * 50)


if __name__ == "__main__":
    main()
