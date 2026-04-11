"""CUA loop with a persistent session for authenticated workflows.

Persistent sessions save cookies and storage state across reconnects,
so you can log in once and run multiple tasks without re-authenticating.
"""

import json
import os
import sys
from tzafon import Lightcone
from tzafon.lib.computer_session import ComputerSession
from _cua import run_cua_loop

client = Lightcone()

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "desktop",
}

TASKS = [
    {
        "label": "Task 1: Log in",
        "task": "Log in with username 'demo' and password 'demo123'",
        "start_url": "https://example.com/login",
    },
    {
        "label": "Task 2: Export report",
        "task": "Go to the dashboard and export the monthly report",
    },
    {
        "label": "Task 3: Update settings",
        "task": "Navigate to settings and update notification preferences",
    },
]


# Reconnect to an existing session, or create a new persistent one.
session_id = sys.argv[1] if len(sys.argv) > 1 else None

if session_id:
    print(f"Reconnecting to session {session_id}")
    computer = ComputerSession(client, session_id)
else:
    computer = client.computer.create(kind="desktop", persistent=True)
    print(f"Created persistent session: {computer.id}")
    print(f"  Re-run with: python {sys.argv[0]} {computer.id}")

_tasks_env = os.getenv("LIGHTCONE_PERSISTENT_TASKS_JSON")
tasks = json.loads(_tasks_env) if _tasks_env else TASKS

for entry in tasks:
    print(f"\n{entry['label']}")
    start_url = entry.get("start_url")
    if start_url:
        computer.navigate(start_url)
        computer.wait(2)

    items, screenshot_url = run_cua_loop(
        client, computer, TOOL,
        entry["task"],
        max_steps=entry.get("max_steps", 50),
    )
