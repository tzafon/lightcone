# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResponseInputFileParam"]


class ResponseInputFileParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A file input to the model."""

    type: Required[Literal["input_file"]]

    file_data: str

    file_id: Optional[str]

    file_url: str

    filename: str
