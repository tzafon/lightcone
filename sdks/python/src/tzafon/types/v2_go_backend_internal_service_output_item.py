# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .content_block import ContentBlock
from .v2_go_backend_internal_service_action import V2GoBackendInternalServiceAction

__all__ = ["V2GoBackendInternalServiceOutputItem"]


class V2GoBackendInternalServiceOutputItem(BaseModel):
    id: Optional[str] = None

    action: Optional[V2GoBackendInternalServiceAction] = None

    call_id: Optional[str] = None

    content: Optional[List[ContentBlock]] = None

    role: Optional[str] = None

    status: Optional[str] = None

    summary: Optional[List[ContentBlock]] = None

    type: Optional[Literal["reasoning", "computer_call", "computer_call_output", "message"]] = None
