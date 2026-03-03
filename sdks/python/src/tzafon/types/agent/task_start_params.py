# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TaskStartParams"]


class TaskStartParams(TypedDict, total=False):
    agent_type: str

    environment_id: str

    instruction: str

    kind: Literal["desktop", "browser"]

    max_steps: int

    model: str

    persistent: bool

    screenshot_mode: Literal["url", "base64"]

    temperature: float

    viewport_height: int

    viewport_width: int
