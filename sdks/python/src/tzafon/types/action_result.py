# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .page_context import PageContext

__all__ = ["ActionResult"]


class ActionResult(BaseModel):
    error_message: Optional[str] = None

    executed_tab_id: Optional[str] = None

    page_context: Optional[PageContext] = None

    request_id: Optional[str] = None

    result: Optional[Dict[str, object]] = None

    status: Optional[str] = None

    timestamp: Optional[str] = None
