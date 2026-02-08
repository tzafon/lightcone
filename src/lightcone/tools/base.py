"""Tool specification data types."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict


@dataclass(frozen=True)
class ToolContext:
    description_prompt: str
    viewport_width: int
    viewport_height: int


@dataclass(frozen=True)
class ToolSpec:
    name: str
    build_schema: Callable[[ToolContext], Dict[str, Any]]
    normalize: Callable[[Dict[str, Any]], Dict[str, Any]]
