# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .v2_go_backend_internal_service_viewport import V2GoBackendInternalServiceViewport
from .v2_go_backend_internal_service_output_item import V2GoBackendInternalServiceOutputItem
from .v2_go_backend_internal_service_responses_usage import V2GoBackendInternalServiceResponsesUsage

__all__ = ["ResponsesResponse"]


class ResponsesResponse(BaseModel):
    id: Optional[str] = None

    computer_id: Optional[str] = None

    created_at: Optional[str] = None

    max_output_tokens: Optional[int] = None

    model: Optional[str] = None

    object: Optional[str] = None

    output: Optional[List[V2GoBackendInternalServiceOutputItem]] = None

    status: Optional[str] = None

    temperature: Optional[float] = None

    top_p: Optional[float] = None

    usage: Optional[V2GoBackendInternalServiceResponsesUsage] = None

    viewport: Optional[V2GoBackendInternalServiceViewport] = None
