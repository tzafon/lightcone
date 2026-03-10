# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ComputerKeyUpParams"]


class ComputerKeyUpParams(TypedDict, total=False):
    key: str
    """Key name to release. Case-insensitive. Examples: "shift", "ctrl", "a", "Enter" """

    tab_id: str
    """Optional tab ID for browser sessions (ignored for desktop sessions)"""
