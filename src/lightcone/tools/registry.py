"""Auto-discovering tool registry."""

from __future__ import annotations

import importlib
import logging
import pkgutil
from typing import Dict, List, Optional

from lightcone import tools as tools_pkg
from lightcone.tools.base import ToolContext, ToolSpec

logger = logging.getLogger("lightcone.tools")

_TOOL_CACHE: Optional[Dict[str, ToolSpec]] = None


def _discover_tools() -> Dict[str, ToolSpec]:
    global _TOOL_CACHE
    if _TOOL_CACHE is not None:
        return _TOOL_CACHE

    tools: Dict[str, ToolSpec] = {}
    for module in pkgutil.iter_modules(tools_pkg.__path__, prefix=f"{tools_pkg.__name__}."):
        mod = importlib.import_module(module.name)
        tool = getattr(mod, "TOOL", None)
        if tool is None:
            continue
        if tool.name in tools:
            logger.warning("Duplicate tool name ignored: %s", tool.name)
            continue
        tools[tool.name] = tool

    _TOOL_CACHE = tools
    return tools


def list_tools() -> List[ToolSpec]:
    """Return all discovered tool specs."""
    return list(_discover_tools().values())


def build_tool_definitions(context: ToolContext) -> List[Dict[str, object]]:
    """Build OpenAI-compatible function schemas for all registered tools."""
    return [tool.build_schema(context) for tool in list_tools()]


def normalize_tool_call(name: str, arguments: Dict[str, object]) -> Optional[Dict[str, object]]:
    """Normalise a tool call's arguments using the tool's own normaliser."""
    tool = _discover_tools().get(name)
    if not tool:
        return None
    return tool.normalize(arguments)
