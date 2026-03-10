# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ContentBlockParam"]


class ContentBlockParam(TypedDict, total=False):
    image_url: str

    text: str

    type: Literal["input_text", "output_text", "summary_text", "input_image"]
