# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatCompletionContentPartImageParam", "ImageURL"]


class ImageURL(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    url: Required[str]

    detail: Literal["auto", "low", "high"]


class ChatCompletionContentPartImageParam(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """Learn about [image inputs](https://platform.openai.com/docs/guides/vision)."""

    image_url: Required[ImageURL]

    type: Required[Literal["image_url"]]
