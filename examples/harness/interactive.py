"""Human-in-the-loop example built on the reusable harness.

Usage:
    export TZAFON_API_KEY=...
    python -m examples.harness.interactive
"""

from __future__ import annotations

import os

from tzafon import Lightcone

from .runner import ActionDecision, ActionEvent, CuaRunner, RunConfig

TASK = "Log in to https://example.com/dashboard"
PAUSE_ACTIONS = {"wait"}


def maybe_intervene(event: ActionEvent) -> ActionDecision | None:
    action = event.action
    if action.type not in PAUSE_ACTIONS:
        return None

    print(f"\n--- pause at step {event.step}: {action.type} ---")
    print("Options:")
    print("  [Enter]          Let Northstar continue")
    print("  type <text>      Type into the active field")
    print("  click <x> <y>    Click coordinates")
    print("  go <url>         Navigate to a URL")
    print("  q                Stop the run")
    command = input("> ").strip()

    if not command:
        return None
    if command.lower() == "q":
        return ActionDecision(
            continue_run=False,
            result_message="Stopped by user.",
        )
    if command.lower().startswith("type "):
        event.computer.type(command[5:])
        return ActionDecision(
            execute_action=False,
            message=(f"The user manually performed: {command}. Continue with the original task."),
        )
    if command.lower().startswith("click "):
        parts = command.split()
        if len(parts) == 3:
            event.computer.click(float(parts[1]), float(parts[2]))
            return ActionDecision(
                execute_action=False,
                message=(
                    f"The user manually performed: {command}. Continue with the original task."
                ),
            )
    if command.lower().startswith("go "):
        event.computer.navigate(command[3:])
        return ActionDecision(
            execute_action=False,
            message=(f"The user manually performed: {command}. Continue with the original task."),
        )
    return ActionDecision(
        execute_action=False,
        message=f"The user says: {command}. Continue with the original task.",
    )


def main() -> None:
    client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])
    runner = CuaRunner(
        client,
        config=RunConfig(
            model="tzafon.northstar-cua-fast",
            kind="browser",
            max_steps=75,
            trace_path="runs/interactive.jsonl",
        ),
        before_action=maybe_intervene,
    )
    result = runner.run(TASK)
    print(f"\nstatus={result.status} steps={result.steps}")
    if result.final_message:
        print(result.final_message)
    if result.trace_path:
        print(f"trace={result.trace_path}")


if __name__ == "__main__":
    main()
