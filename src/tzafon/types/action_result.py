# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ActionResult", "PageContext"]


class PageContext(BaseModel):
    device_scale_factor: Optional[float] = None

    is_main_tab: Optional[bool] = None

    page_height: Optional[int] = None

    page_width: Optional[int] = None

    scroll_x: Optional[float] = None

    scroll_y: Optional[float] = None

    tab_id: Optional[str] = None

    title: Optional[str] = None

    url: Optional[str] = None

    viewport_height: Optional[int] = None

    viewport_width: Optional[int] = None


class ActionResult(BaseModel):
    error_message: Optional[str] = None

    executed_tab_id: Optional[str] = None

    page_context: Optional[PageContext] = None

    request_id: Optional[str] = None

    result: Optional[Dict[str, object]] = None

    status: Optional[str] = None

    timestamp: Optional[str] = None
