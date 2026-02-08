"""computer_use tool — the primary action tool for the agent."""

from __future__ import annotations

from typing import Any, Dict

from lightcone.tools.base import ToolContext, ToolSpec

S2_ACTION_DESCRIPTION = """
* Coordinates are always normalized to a 0-999 grid (0,0 top-left; 999,999 bottom-right). The agent scales them to the real viewport.
* `key`: Performs key down presses on the arguments passed in order, then performs key releases in reverse order.
* `key_down`: Press and HOLD the specified key(s) down in order (no release). Use this for stateful holds like holding Shift while clicking.
* `key_up`: Release the specified key(s) in reverse order.
* `type`: Type a string of text on the keyboard.
* `mouse_move`: Move the cursor to a specified (x, y) coordinate in the 0-999 grid.
* `left_click`: Click the left mouse button at a specified (x, y) coordinate in the 0-999 grid.
* `left_click_drag`: Click and drag the cursor to a specified (x, y) coordinate in the 0-999 grid.
* `right_click`: Click the right mouse button at a specified (x, y) coordinate in the 0-999 grid.
* `middle_click`: Click the middle mouse button at a specified (x, y) coordinate in the 0-999 grid.
* `double_click`: Double-click the left mouse button at a specified (x, y) coordinate in the 0-999 grid.
* `triple_click`: Triple-click the left mouse button at a specified (x, y) coordinate in the 0-999 grid.
* `scroll`: Performs a scroll of the mouse scroll wheel.
* `hscroll`: Performs a horizontal scroll (mapped to regular scroll).
* `wait`: Wait specified seconds for the change to happen.
* `terminate`: Terminate the current task and report its completion status.
* `answer`: Answer a question.
"""


def build_schema(context: ToolContext) -> Dict[str, Any]:
    return {
        "type": "function",
        "function": {
            "name_for_human": "computer_use",
            "name": "computer_use",
            "description": context.description_prompt,
            "parameters": {
                "properties": {
                    "action": {
                        "description": S2_ACTION_DESCRIPTION,
                        "enum": [
                            "key",
                            "type",
                            "mouse_move",
                            "left_click",
                            "left_click_drag",
                            "right_click",
                            "middle_click",
                            "double_click",
                            "triple_click",
                            "scroll",
                            "hscroll",
                            "wait",
                            "terminate",
                            "answer",
                            "key_down",
                            "key_up",
                        ],
                        "type": "string",
                    },
                    "keys": {"description": "Required only by `action=key`.", "type": "array"},
                    "text": {"description": "Required only by `action=type`.", "type": "string"},
                    "coordinate": {
                        "description": "Normalized [x, y] in 0-999 grid (top-left to bottom-right).",
                        "type": "array",
                    },
                    "pixels": {"description": "The amount of scrolling.", "type": "number"},
                    "time": {"description": "The seconds to wait.", "type": "number"},
                    "status": {
                        "description": "The status of the task.",
                        "type": "string",
                        "enum": ["success", "failure"],
                    },
                },
                "required": ["action"],
                "type": "object",
            },
            "args_format": "Format the arguments as a JSON object.",
        },
    }


def normalize(arguments: Dict[str, Any]) -> Dict[str, Any]:
    return arguments or {}


TOOL = ToolSpec(name="computer_use", build_schema=build_schema, normalize=normalize)
