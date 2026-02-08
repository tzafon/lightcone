"""Action execution — translates parsed action dicts into computer SDK calls."""

from __future__ import annotations

import logging
from typing import Any, Dict, Optional, Tuple

from lightcone.images import scale_coordinates

logger = logging.getLogger("lightcone.actions")

# Shared key normalisation table.
_KEY_MAP: dict[str, str] = {
    "RETURN": "enter", "RETURN2": "enter", "ENTER": "enter",
    "TAB": "tab", "BACKSPACE": "backspace", "DELETE": "delete",
    "SPACE": "space", "ESC": "escape", "ESCAPE": "escape",
    "UP": "up", "DOWN": "down", "LEFT": "left", "RIGHT": "right",
    "PGUP": "pageup", "PGDN": "pagedown", "HOME": "home", "END": "end",
    "CTRL": "ctrl", "SHIFT": "shift", "ALT": "alt", "META": "meta",
}

_HOTKEY_MAP: dict[str, str] = {
    **_KEY_MAP,
    "esc": "escape",
    "Control": "ctrl", "Ctrl": "ctrl",
    "Super": "Super_L", "super": "Super_L",
    "Meta": "Super_L", "meta": "Super_L",
    "Win": "Super_L", "win": "Super_L",
    "Windows": "Super_L", "windows": "Super_L",
    "Command": "Super_L", "command": "Super_L", "cmd": "Super_L",
}


def execute_action(
    computer: Any,
    action: Dict[str, Any],
    viewport_width: int,
    viewport_height: int,
) -> Tuple[bool, Optional[str], Optional[str]]:
    """Execute *action* on *computer*.

    Returns ``(should_continue, status, result)``:
    - *should_continue*: ``True`` if the agent loop should keep running.
    - *status*: ``'success'``, ``'failure'``, or ``None`` if not terminated.
    - *result*: optional text result from a terminate/answer action.
    """
    action_type = action.get("action")
    if not action_type:
        logger.warning("No action type in action dict")
        return True, None, None

    def _coord(default: Tuple[int, int] = (500, 500)) -> Tuple[int, int]:
        if "coordinate" in action and isinstance(action["coordinate"], list):
            c = action["coordinate"]
            return int(c[0]), int(c[1])
        if "x" in action and "y" in action:
            return int(action["x"]), int(action["y"])
        return default

    try:
        # ------------------------------------------------------------------
        # Mouse actions
        # ------------------------------------------------------------------
        if action_type in ("left_click", "click"):
            cx, cy = _coord()
            x, y = scale_coordinates(cx, cy, viewport_width, viewport_height)
            computer.click(x, y)

        elif action_type == "double_click":
            cx, cy = _coord()
            x, y = scale_coordinates(cx, cy, viewport_width, viewport_height)
            computer.double_click(x, y)

        elif action_type == "triple_click":
            cx, cy = _coord()
            x, y = scale_coordinates(cx, cy, viewport_width, viewport_height)
            computer.click(x, y)
            computer.click(x, y)
            computer.click(x, y)

        elif action_type == "right_click":
            cx, cy = _coord()
            x, y = scale_coordinates(cx, cy, viewport_width, viewport_height)
            computer.right_click(x, y)

        elif action_type == "middle_click":
            cx, cy = _coord()
            x, y = scale_coordinates(cx, cy, viewport_width, viewport_height)
            computer.middle_click(x, y)

        elif action_type == "mouse_move":
            cx, cy = _coord()
            x, y = scale_coordinates(cx, cy, viewport_width, viewport_height)
            computer.move(x, y)

        elif action_type == "left_click_drag":
            cx, cy = _coord()
            x, y = scale_coordinates(cx, cy, viewport_width, viewport_height)
            computer.drag(x, y)

        elif action_type == "drag":
            fx, fy = int(action.get("from_x", 500)), int(action.get("from_y", 500))
            tx, ty = int(action.get("to_x", 500)), int(action.get("to_y", 500))
            sx, sy = scale_coordinates(fx, fy, viewport_width, viewport_height)
            ex, ey = scale_coordinates(tx, ty, viewport_width, viewport_height)
            computer.move(sx, sy)
            computer.drag(ex, ey)

        # ------------------------------------------------------------------
        # Keyboard actions
        # ------------------------------------------------------------------
        elif action_type == "type":
            text = action.get("text", "")
            if text:
                computer.type(text)

        elif action_type == "key":
            key = action.get("key", "")
            if key:
                computer.key(_KEY_MAP.get(key.upper(), key))

        elif action_type == "hotkey":
            keys = action.get("keys", [])
            if isinstance(keys, str):
                keys = [keys]
            if keys:
                mapped = [_HOTKEY_MAP.get(k, k) for k in keys]
                computer.hotkey(*mapped)

        elif action_type == "key_down":
            keys = action.get("keys", [])
            if isinstance(keys, str):
                keys = [keys]
            for key in keys:
                computer.key_down(key)

        elif action_type == "key_up":
            keys = action.get("keys", [])
            if isinstance(keys, str):
                keys = [keys]
            for key in reversed(keys):
                computer.key_up(key)

        # ------------------------------------------------------------------
        # Scroll
        # ------------------------------------------------------------------
        elif action_type == "scroll":
            if "dx" in action or "dy" in action:
                computer.scroll(dx=int(action.get("dx", 0)), dy=int(action.get("dy", 0)))
                return True, None, None

            coord = action.get("coordinate", [])
            pixels = action.get("pixels")

            if pixels is None and isinstance(coord, list) and len(coord) >= 3:
                try:
                    pixels = int(coord[-1])
                except (ValueError, TypeError):
                    pixels = None
            if pixels is None:
                pixels = 0

            x = y = None
            if isinstance(coord, list) and len(coord) >= 2:
                try:
                    cx, cy = int(coord[0]), int(coord[1])
                    if 0 <= cx <= 999 and 0 <= cy <= 999 and not (cx == 0 and cy == 0):
                        x, y = scale_coordinates(cx, cy, viewport_width, viewport_height)
                except (ValueError, TypeError):
                    pass
            if x is None or y is None:
                x, y = viewport_width // 2, viewport_height // 2

            computer.scroll(dy=pixels, x=x, y=y)

        elif action_type == "hscroll":
            computer.scroll(dx=int(action.get("pixels", 0)), dy=0)

        # ------------------------------------------------------------------
        # Timing / termination
        # ------------------------------------------------------------------
        elif action_type == "wait":
            seconds = action.get("seconds", action.get("time", 2))
            computer.wait(seconds)

        elif action_type == "terminate":
            status = action.get("status", "success")
            result = action.get("result", "")
            logger.info("Task terminated with status: %s", status)
            return False, status, result

        elif action_type == "answer":
            result = action.get("result", action.get("answer", ""))
            return False, "success", result

        elif action_type == "navigate":
            url = action.get("url", "")
            if url:
                computer.navigate(url)

        elif action_type == "done":
            result = action.get("result", "")
            return False, "success", result

        else:
            logger.warning("Unknown action type: %s", action_type)

    except Exception as exc:
        logger.error("Error executing action %s: %s", action_type, exc)

    return True, None, None
