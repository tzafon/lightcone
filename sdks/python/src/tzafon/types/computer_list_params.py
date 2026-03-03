# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ComputerListParams"]


class ComputerListParams(TypedDict, total=False):
    type: Literal["live", "persistent"]
    """Session type filter"""
