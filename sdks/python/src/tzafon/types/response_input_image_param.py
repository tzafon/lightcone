# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResponseInputImageParam"]


class ResponseInputImageParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """An image input to the model.

    Learn about [image inputs](https://platform.openai.com/docs/guides/vision).
    """

    detail: Required[Literal["low", "high", "auto"]]

    type: Required[Literal["input_image"]]

    file_id: Optional[str]

    image_url: Optional[str]
