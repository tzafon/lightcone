"""Desktop CUA loop — Northstar operates a full Lightcone OS desktop.

Launches a cloud computer, opens the terminal, runs a command, and reads
the output. Demonstrates the core loop on a desktop environment:
screenshot → think → act → repeat.
"""

import os
from tzafon import Lightcone
from _cua import run_cua_loop

client = Lightcone()

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "desktop",
}


with client.computer.create(kind="desktop") as computer:
    items, screenshot_url = run_cua_loop(
        client, computer, TOOL,
        "Open the terminal. Run 'uname -a' to check the system info, "
        "then run 'df -h' to check disk usage. Report back what you find.",
        max_steps=30,
    )
    print(f"Final state: {screenshot_url}")
