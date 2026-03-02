# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ContentBlock"]


class ContentBlock(BaseModel):
    image_url: Optional[str] = None

    text: Optional[str] = None

    type: Optional[Literal["input_text", "output_text", "summary_text", "input_image"]] = None
