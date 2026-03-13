"""Run a task with the reusable harness.

Usage:
    export TZAFON_API_KEY=...
    python -m examples.harness.simple
"""

from __future__ import annotations

import os

from tzafon import Lightcone

from .runner import ActionEvent, CuaRunner, MessageEvent, RunConfig

TASK = "Go to wikipedia.org and search for 'Alan Turing'"


def render_action(event: ActionEvent) -> None:
    action = event.action
    label = action.type
    if getattr(action, "x", None) is not None:
        label += f" @ ({action.x}, {action.y})"
    if getattr(action, "text", None):
        label += f" '{action.text}'"
    print(f"[{event.step}] {label}")


def render_message(event: MessageEvent) -> None:
    print(f"  model: {event.text}")


def main() -> None:
    client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])
    runner = CuaRunner(
        client,
        config=RunConfig(
            model="tzafon.northstar-cua-fast",
            kind="browser",
            environment="browser",
            max_steps=50,
            trace_path="runs/simple.jsonl",
        ),
        on_action=render_action,
        on_message=render_message,
    )
    result = runner.run(TASK)
    print(f"\nstatus={result.status} steps={result.steps}")
    if result.final_message:
        print(result.final_message)
    if result.trace_path:
        print(f"trace={result.trace_path}")


if __name__ == "__main__":
    main()
