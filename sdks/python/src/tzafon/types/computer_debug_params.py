# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ComputerDebugParams"]


class ComputerDebugParams(TypedDict, total=False):
    command: str

    max_output_length: int

    tab_id: str

    timeout_seconds: int
