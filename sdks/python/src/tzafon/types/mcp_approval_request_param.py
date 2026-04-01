# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["McpApprovalRequestParam"]


class McpApprovalRequestParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A request for human approval of a tool invocation."""

    id: Required[str]

    arguments: Required[str]

    name: Required[str]

    server_label: Required[str]

    type: Required[Literal["mcp_approval_request"]]
