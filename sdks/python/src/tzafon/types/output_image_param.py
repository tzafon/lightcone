# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OutputImageParam"]


class OutputImageParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The image output from the code interpreter."""

    type: Required[Literal["image"]]

    url: Required[str]
