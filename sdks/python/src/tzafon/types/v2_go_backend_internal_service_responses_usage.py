# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["V2GoBackendInternalServiceResponsesUsage"]


class V2GoBackendInternalServiceResponsesUsage(BaseModel):
    input_tokens: Optional[int] = None

    output_tokens: Optional[int] = None

    total_tokens: Optional[int] = None
