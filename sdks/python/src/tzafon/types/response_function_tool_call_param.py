# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResponseFunctionToolCallParam"]


class ResponseFunctionToolCallParam(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """A tool call to run a function.

    See the
    [function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.
    """

    arguments: Required[str]

    call_id: Required[str]

    name: Required[str]

    type: Required[Literal["function_call"]]

    id: Optional[str]

    status: Optional[Literal["in_progress", "completed", "incomplete"]]
