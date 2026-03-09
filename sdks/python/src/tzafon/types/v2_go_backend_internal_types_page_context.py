# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["V2GoBackendInternalTypesPageContext"]


class V2GoBackendInternalTypesPageContext(BaseModel):
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
