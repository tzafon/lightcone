"""System prompt construction with profile support."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List

from lightcone.tools.base import ToolContext
from lightcone.tools.registry import build_tool_definitions

_PROFILES_DIR = Path(__file__).resolve().parent / "prompts"
_DEFAULT_PROFILE = "default"

# ---------------------------------------------------------------------------
# Profile helpers
# ---------------------------------------------------------------------------


def list_profiles() -> List[str]:
    """Return available profile names (stems of .md files in the prompts dir)."""
    if not _PROFILES_DIR.exists():
        return [_DEFAULT_PROFILE]
    return sorted(p.stem for p in _PROFILES_DIR.glob("*.md"))


def load_profile(name: str | None) -> tuple[str, str]:
    """Load a prompt profile by name.  Returns ``(resolved_name, text)``."""
    profile = (name or _DEFAULT_PROFILE).strip().lower() or _DEFAULT_PROFILE
    path = _PROFILES_DIR / f"{profile}.md"
    if not path.exists():
        profile = _DEFAULT_PROFILE
        path = _PROFILES_DIR / f"{profile}.md"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    return profile, text


# ---------------------------------------------------------------------------
# Prompt templates (S2 only — S1 removed)
# ---------------------------------------------------------------------------

DESCRIPTION_PROMPT_TEMPLATE = """\
Use a mouse and keyboard to interact with a computer, and take screenshots.
* This is an interface to a desktop GUI. You must click on desktop icons to start applications.
* Some applications may take time to start or process actions, so you may need to wait and take \
successive screenshots to see the results of your actions. E.g. if you click on Firefox and a \
window doesn't open, try wait and taking another screenshot.
{resolution_info}
* All coordinates in tool calls use a normalized 0-999 grid: (0,0) is top-left, (999,999) is \
bottom-right.
* The agent will scale these normalized coordinates to the real viewport size automatically.
* Whenever you intend to move the cursor to click on an element like an icon, you should consult \
a screenshot to determine the coordinates of the element before moving the cursor.
* If you tried clicking on a program or link but it failed to load even after waiting, try \
adjusting your cursor position so that the tip of the cursor visually falls on the element that \
you want to click.
* Make sure to click any buttons, links, icons, etc with the cursor tip in the center of the \
element. Don't click boxes on their edges unless asked."""

DECISION_GUIDE = """\
Decision Guide (what to open):
- If the task involves websites, web search, logins, web forms, or online content: open Firefox.
- If the task involves running commands, inspecting logs, code execution, or environment checks: \
open Terminal.
- If the task involves browsing, moving, renaming, or inspecting local files visually: open Files \
(file manager).
- If the task changes system preferences (network, display, audio, input, date/time): open Settings.
- If an app is already open and can complete the task, stay in that app; only switch when stuck.
- Prefer the simplest app that accomplishes the goal; avoid opening multiple apps at once.
- When unsure, look for existing windows first, then open the most likely app based on the task."""

SYSTEM_PROMPT_TEMPLATE = """\
# Role
You are a desktop automation agent. Operate the GUI from screenshots with precision, safety, \
and good judgment.

# Operating Principles
- First identify the immediate goal for this step and choose the most appropriate app.
- Minimize app switching; keep context in the active window if possible.
- If the screen does not change, adjust your approach (scroll, refocus, wait, or target a \
different UI element).
- Do not close apps or tabs unless explicitly instructed.

# App Selection
{decision_guide}

# Mode Guidance
{profile_instructions}

# Tools

You may call one or more functions to assist with the user query.

You are provided with function signatures within <tools></tools> XML tags:
<tools>
{tools_xml}
</tools>

For each function call, return a json object with function name and arguments within \
<tool_call></tool_call> XML tags:
<tool_call>
{{"name": <function-name>, "arguments": <args-json-object>}}
</tool_call>

# Browser JSON Actions

You can also control a browser by responding with a single JSON action object (no tool calls).
Coordinates use a normalized 0-999 grid where (0,0) is top-left and (999,999) is bottom-right, \
scaled to the viewport.

Available actions:
- {{"action": "click", "x": <0-999>, "y": <0-999>}} - Click at coordinates
- {{"action": "double_click", "x": <0-999>, "y": <0-999>}} - Double-click at coordinates
- {{"action": "right_click", "x": <0-999>, "y": <0-999>}} - Right-click at coordinates
- {{"action": "type", "text": "<string>"}} - Type text at current cursor
- {{"action": "hotkey", "keys": ["<key1>", "<key2>"]}} - Press keyboard shortcut
- {{"action": "scroll", "dx": <int>, "dy": <int>}} - Scroll by delta (positive dy = down)
- {{"action": "drag", "from_x": <0-999>, "from_y": <0-999>, "to_x": <0-999>, "to_y": <0-999>}}
- {{"action": "navigate", "url": "<string>"}} - Navigate to URL
- {{"action": "wait", "seconds": <float>}} - Wait for seconds
- {{"action": "done", "result": "<string>"}} - Task complete, return result

When using browser JSON actions, respond with a single JSON object. No markdown, no explanation, \
just the JSON.

# Response format

Response format for every step:
1) Action: a short imperative describing what to do in the UI.
2) A single <tool_call>...</tool_call> block containing only the JSON: \
{{"name": <function-name>, "arguments": <args-json-object>}}.

Rules:
- Output exactly in the order: Action, <tool_call>.
- Be brief: one sentence for Action.
- Do not output anything else outside those parts.
- If finishing, use action=terminate in the tool call."""


def build_system_prompt(
    viewport_width: int = 1920,
    viewport_height: int = 1080,
    profile: str | None = None,
) -> str:
    """Build the complete system prompt with tool definitions and profile."""
    resolution_info = (
        f"* Viewport (physical): {viewport_width}x{viewport_height} pixels.\n"
        "* Coordinate grid for actions: 0-999 (normalized), scaled to the viewport."
    )
    description_prompt = DESCRIPTION_PROMPT_TEMPLATE.format(resolution_info=resolution_info)

    tool_context = ToolContext(
        description_prompt=description_prompt,
        viewport_width=viewport_width,
        viewport_height=viewport_height,
    )
    tools_def = build_tool_definitions(tool_context)

    _, profile_text = load_profile(profile)

    return SYSTEM_PROMPT_TEMPLATE.format(
        tools_xml=json.dumps(tools_def),
        decision_guide=DECISION_GUIDE.strip(),
        profile_instructions=profile_text.strip()
        or "Use best judgment for the current environment.",
    )
