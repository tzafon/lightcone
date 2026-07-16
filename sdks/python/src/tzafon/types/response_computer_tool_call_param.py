# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .action_drag_param import ActionDragParam
from .action_move_param import ActionMoveParam
from .action_type_param import ActionTypeParam
from .action_wait_param import ActionWaitParam
from .action_click_param import ActionClickParam
from .action_key_up_param import ActionKeyUpParam
from .action_scroll_param import ActionScrollParam
from .action_key_down_param import ActionKeyDownParam
from .action_keypress_param import ActionKeypressParam
from .action_mouse_up_param import ActionMouseUpParam
from .action_mouse_down_param import ActionMouseDownParam
from .action_screenshot_param import ActionScreenshotParam
from .action_double_click_param import ActionDoubleClickParam
from .pending_safety_check_param import PendingSafetyCheckParam
from .action_point_and_type_param import ActionPointAndTypeParam

__all__ = ["ResponseComputerToolCallParam", "Action"]

Action: TypeAlias = Union[
    ActionClickParam,
    ActionDoubleClickParam,
    ActionDragParam,
    ActionKeypressParam,
    ActionMoveParam,
    ActionScreenshotParam,
    ActionScrollParam,
    ActionTypeParam,
    ActionWaitParam,
    ActionPointAndTypeParam,
    ActionMouseDownParam,
    ActionMouseUpParam,
    ActionKeyDownParam,
    ActionKeyUpParam,
]


class ResponseComputerToolCallParam(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """A tool call to a computer use tool.

    See the
    [computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.
    """

    id: Required[str]

    action: Required[Action]
    """A click action."""

    call_id: Required[str]

    pending_safety_checks: Required[Iterable[PendingSafetyCheckParam]]

    status: Required[Literal["in_progress", "completed", "incomplete"]]

    type: Required[Literal["computer_call"]]
