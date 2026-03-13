# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ComputerRetrieveStatusResponse"]


class ComputerRetrieveStatusResponse(BaseModel):
    id: Optional[str] = None

    auto_kill: Optional[bool] = None
    """Deprecated: mirrors IdleTimeoutEnabled. Remove after 2026-06-06."""

    created_at: Optional[str] = None

    expires_at: Optional[str] = None

    idle_expires_at: Optional[str] = None

    idle_timeout_enabled: Optional[bool] = None

    inactivity_timeout_seconds: Optional[int] = None

    last_activity_at: Optional[str] = None

    max_lifetime_seconds: Optional[int] = None

    status: Optional[str] = None
