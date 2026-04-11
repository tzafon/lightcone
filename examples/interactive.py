"""Human-in-the-loop CUA — pauses for user input on CAPTCHAs, 2FA, or ambiguity.

Northstar operates the computer but yields control to the human when it
encounters something it can't handle. The human can type instructions, press
Enter to continue, or type 'q' to quit.
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

TASK = "Log in to https://example.com/dashboard"

# For automated testing: pre-fill inputs instead of waiting for stdin.
# Set LIGHTCONE_AUTO_INPUTS_JSON='["q"]' to auto-quit after one pause.
_auto = os.getenv("LIGHTCONE_AUTO_INPUTS_JSON")
AUTO_INPUTS = json.loads(_auto) if _auto else []
FORCE_HUMAN_STEP = os.getenv("LIGHTCONE_FORCE_HUMAN_STEP", "").lower() in ("1", "true")


def ask_human(step, action_dict, messages):
    """Pause and ask the human what to do."""
    if AUTO_INPUTS:
        value = str(AUTO_INPUTS.pop(0))
        print(f"\n--- AUTO INPUT at step {step}: {value!r} ---")
        return value

    print(f"\n--- PAUSED at step {step} ---")
    if action_dict:
        print(f"  Last action: {format_action(action_dict)}")
    for text in messages:
        print(f"  Northstar: {text}")

    print("\nOptions:")
    print("  [Enter]          Continue (Northstar retries)")
    print("  'type <text>'    Type text into the active field")
    print("  'click <x> <y>'  Click at coordinates")
    print("  'go <url>'       Navigate to URL")
    print("  'q'              Quit")

    return input("> ").strip()


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

    for step in range(1, 76):
        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            tools=[TOOL, DONE_TOOL],
            input=items,
        )
        items.extend(response.output or [])

        calls, call_ids = get_computer_calls(response.output, TOOL)
        messages = get_messages(response.output)

        needs_human = (
            not calls
            or any(is_terminal_action(c) for c in calls)
            or (FORCE_HUMAN_STEP and step == 1)
        )

        if needs_human:
            action_dict = calls[0] if calls else None
            human_input = ask_human(step, action_dict, messages)

            if human_input.lower() == "q":
                print("Quitting.")
                break
            elif human_input.lower().startswith("type "):
                computer.type(human_input[5:])
            elif human_input.lower().startswith("click "):
                parts = human_input.split()
                if len(parts) == 3:
                    computer.click(float(parts[1]), float(parts[2]))
            elif human_input.lower().startswith("go "):
                computer.navigate(human_input[3:])

            computer.wait(1)
            screenshot_url = computer.get_screenshot_url(computer.screenshot())

            if human_input.lower().startswith(("type ", "click ", "go ")):
                context = f"The user manually performed: {human_input}. Continue with the original task: {TASK}"
            elif human_input:
                context = f"The user says: {human_input}. Continue with the original task: {TASK}"
            else:
                context = f"The user asked you to retry. Continue with the original task: {TASK}"

            items.append({
                "role": "user",
                "content": [
                    {"type": "input_text", "text": context},
                    {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
                ],
            })
            continue

        for c in calls:
            print(f"[{step}] {format_action(c)}")

        computer.batch(calls)
        time.sleep(1)

        screenshot_url = computer.get_screenshot_url(computer.screenshot())
        for call_id in call_ids:
            items.append({
                "type": "computer_call_output",
                "call_id": call_id,
                "output": {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
            })

    print("Done.")
