"""Desktop session mixing browser actions with shell commands.

Uses kind="desktop" for full OS access — Northstar can browse the web,
open a terminal, run scripts, and pipe data between them.
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
    # Run a shell command directly before handing off to the CUA loop.
    # Useful for setup — install packages, seed files, set env vars.
    result = computer.debug("mkdir -p /tmp && echo 'ready'")
    print(f"Shell: {computer.get_debug_response(result)}")

    items, screenshot_url = run_cua_loop(
        client, computer, TOOL,
        "Open Firefox and download the CSV from https://example.com/data.csv, "
        "then open a terminal and run: python3 -c \"import csv; "
        "data=list(csv.reader(open('/tmp/data.csv'))); print(len(data), 'rows')\"",
        max_steps=75,
    )

    # After the CUA loop, inspect the result with a shell command.
    result = computer.debug("ls -la /tmp/*.csv 2>/dev/null || echo 'no CSV found'")
    print(f"\nShell check: {computer.get_debug_response(result)}")
