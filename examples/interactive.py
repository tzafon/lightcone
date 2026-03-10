"""Human-in-the-loop CUA — pauses for user input on CAPTCHAs, 2FA, or ambiguity.

The agent runs autonomously but yields control to the human when it encounters
something it can't handle. The human can type instructions, press Enter to
continue, or type 'q' to quit.
"""

import os
from tzafon import Lightcone

client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "browser",
}
TASK = "Log in to https://example.com/dashboard"
MAX_STEPS = 75

# Action types that signal the agent is stuck or needs human help.
PAUSE_SIGNALS = {"wait", "terminate", "done", "answer"}


def execute_action(computer, action):
    """Execute a model action on the computer session."""
    t = action.type
    if t == "click":
        computer.click(action.x, action.y)
    elif t == "double_click":
        computer.double_click(action.x, action.y)
    elif t == "triple_click":
        computer.click(action.x, action.y)
        computer.click(action.x, action.y)
        computer.click(action.x, action.y)
    elif t == "right_click":
        computer.right_click(action.x, action.y)
    elif t == "type":
        computer.type(action.text)
    elif t in ("key", "keypress"):
        computer.hotkey(action.keys)
    elif t == "key_down":
        computer.key_down(action.keys[0])
    elif t == "key_up":
        computer.key_up(action.keys[0])
    elif t == "scroll":
        computer.scroll(
            dx=action.scroll_x or 0,
            dy=action.scroll_y or 0,
            x=action.x or 0,
            y=action.y or 0,
        )
    elif t == "hscroll":
        computer.scroll(
            dx=action.scroll_x or 0,
            dy=0,
            x=action.x or 0,
            y=action.y or 0,
        )
    elif t == "navigate":
        computer.navigate(action.url)
    elif t == "drag":
        computer.drag(action.x, action.y, action.end_x, action.end_y)
    elif t == "wait":
        computer.wait(2)


def ask_human(step, action, messages):
    """Pause and ask the human what to do."""
    print(f"\n--- PAUSED at step {step + 1} ---")
    if action:
        print(f"  Last action: {action.type}")
        if action.result or action.text:
            print(f"  Message: {action.result or action.text}")

    # Check for model messages (e.g. "I see a CAPTCHA" or "Please provide 2FA code")
    for item in messages or []:
        if item.type == "message":
            for block in item.content or []:
                if block.text:
                    print(f"  Agent: {block.text}")

    print("\nOptions:")
    print("  [Enter]          Continue (agent retries)")
    print("  'type <text>'    Type text into the active field")
    print("  'click <x> <y>'  Click at coordinates")
    print("  'go <url>'       Navigate to URL")
    print("  'q'              Quit")

    return input("> ").strip()


with client.computer.create(kind="browser") as computer:
    screenshot_url = computer.get_screenshot_url(computer.screenshot())
    task = TASK

    response = client.responses.create(
        model="tzafon.northstar-cua-fast",
        tools=[TOOL],
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text", "text": task},
                {"type": "input_image", "image_url": screenshot_url},
            ],
        }],
    )

    for step in range(MAX_STEPS):
        computer_call = next(
            (o for o in (response.output or []) if o.type == "computer_call"), None
        )

        # No action or a pause signal — ask the human.
        needs_human = (
            not computer_call
            or computer_call.action.type in PAUSE_SIGNALS
        )

        if needs_human:
            action = computer_call.action if computer_call else None
            human_input = ask_human(step, action, response.output)

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

            # After human intervention, re-screenshot and tell the agent
            # what happened so it can continue.
            computer.wait(1)
            screenshot_url = computer.get_screenshot_url(computer.screenshot())

            if human_input.lower().startswith(("type ", "click ", "go ")):
                context = f"The user manually performed: {human_input}. Continue with the original task: {task}"
            elif human_input:
                context = f"The user says: {human_input}. Continue with the original task: {task}"
            else:
                context = f"The user asked you to retry. Continue with the original task: {task}"

            response = client.responses.create(
                model="tzafon.northstar-cua-fast",
                tools=[TOOL],
                input=[{
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": context},
                        {"type": "input_image", "image_url": screenshot_url},
                    ],
                }],
            )
            continue

        # Normal autonomous step.
        action = computer_call.action
        print(f"[{step + 1}] {action.type}", end="")
        if action.text:
            print(f" '{action.text}'", end="")
        print()

        execute_action(computer, action)
        computer.wait(1)

        screenshot_url = computer.get_screenshot_url(computer.screenshot())
        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            previous_response_id=response.id,
            tools=[TOOL],
            input=[{
                "type": "computer_call_output",
                "call_id": computer_call.call_id,
                "output": {"type": "input_image", "image_url": screenshot_url},
            }],
        )

    print("Done.")
