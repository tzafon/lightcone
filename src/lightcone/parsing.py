"""Parse LLM responses into structured actions (pure Python)."""

from __future__ import annotations

import json
import re
from typing import Any, Dict, Optional

from lightcone.tools.registry import normalize_tool_call

_ACTION_RE = re.compile(r'\{[^{}]*"action"[^{}]*\}')


def parse_tool_call(response: str) -> Optional[Dict[str, Any]]:
    """Extract a tool-call dict from an LLM response string.

    Tries, in order:
    1. ``<tool_call>…</tool_call>`` XML wrapper
    2. Loose JSON object containing an ``"action"`` key
    3. The full response as JSON (with trailing ``}}`` trimming)
    """
    trimmed = response.strip()
    if not trimmed:
        return None

    # 1. XML-wrapped tool call
    start = trimmed.find("<tool_call>")
    end = trimmed.find("</tool_call>")
    if start != -1 and end != -1 and end > start + 11:
        json_str = trimmed[start + 11 : end].strip()
        raw = _try_parse(json_str)
        if raw is not None:
            return _normalize(raw)

    # 2. Loose JSON with "action" key
    for match in _ACTION_RE.finditer(trimmed):
        raw = _try_parse(match.group())
        if raw is not None:
            return _normalize(raw)

    # 3. Full response as JSON (trim stacked closing braces)
    clean = trimmed
    while clean.endswith("}}"):
        clean = clean[:-1]
    raw = _try_parse(clean)
    if raw is not None:
        return _normalize(raw)

    return None


def parse_action_description(response: str) -> str:
    """Extract a one-line action description (``Action: …``) from a response."""
    for line in response.splitlines():
        stripped = line.strip()
        if stripped.lower().startswith("action:"):
            _, _, value = stripped.partition(":")
            return value.strip()
    return ""


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _try_parse(text: str) -> Optional[Dict[str, Any]]:
    try:
        obj = json.loads(text)
        return obj if isinstance(obj, dict) else None
    except (json.JSONDecodeError, ValueError):
        return None


def _normalize(raw: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Normalise raw parsed JSON into a flat action dict."""
    if "action" in raw:
        return raw
    name = raw.get("name") or raw.get("tool")
    arguments = raw.get("arguments", {}) or {}
    if name:
        normalized = normalize_tool_call(name, arguments)
        if normalized is not None:
            return normalized
    return raw
