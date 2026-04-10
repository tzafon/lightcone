"""Convenience wrapper around the Lightcone computers API."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Type, Iterable, Optional, cast
from typing_extensions import override

if TYPE_CHECKING:
    from .._client import Lightcone
    from ..types.action_result import ActionResult
    from ..types.computer_response import ComputerResponse
    from ..types.computer_action_param import ComputerActionParam
    from ..types.computer_batch_response import ComputerBatchResponse
    from ..types.computer_keepalive_response import ComputerKeepaliveResponse

__all__ = ["ComputerResource", "ComputerSession"]


class ComputerResource:
    """
    Resource for creating and managing computer sessions.

    Accessed as ``client.computer`` on a :class:`Lightcone` client.

    Example::

        from tzafon import Lightcone

        client = Lightcone()
        with client.computer.create(kind="browser") as computer:
            computer.navigate("https://example.com")
            computer.click(100, 200)
            result = computer.screenshot()
    """

    def __init__(self, client: Lightcone) -> None:
        self._client = client

    def create(self, kind: str = "browser", **kwargs: Any) -> ComputerSession:
        """
        Create a new computer session.

        Args:
            kind: Session type — ``"browser"`` or ``"desktop"``
            **kwargs: Additional arguments passed to the API (e.g.
                ``timeout_seconds``, ``inactivity_timeout_seconds``,
                ``persistent``, ``display``, ``stealth``).

        Returns:
            A :class:`ComputerSession` bound to the new session ID.
        """
        response = self._client.computers.create(kind=kind, **kwargs)
        assert response.id is not None
        display = kwargs.get("display") or {}
        width = display.get("width", 1024)
        height = display.get("height", 768)
        return ComputerSession(self._client, response.id, width=width, height=height)


class ComputerSession:
    """
    High-level wrapper that binds a computer ID to a client.

    Provides the same methods as the previous ``computer-python`` SDK,
    with automatic ID management and context-manager cleanup.

    Example::

        with client.computer.create(kind="browser") as computer:
            computer.navigate("https://example.com")
            computer.click(100, 200)
            result = computer.screenshot()
            url = computer.get_screenshot_url(result)
            # automatically terminated on exit
    """

    def __init__(self, client: Lightcone, computer_id: str, width: int = 1024, height: int = 768) -> None:
        self._client = client
        self.id = computer_id
        self.width = width
        self.height = height

    # ── Navigation ────────────────────────────────────────────────

    def navigate(self, url: str) -> ActionResult:
        """Navigate to a URL."""
        return self._client.computers.navigate(self.id, url=url)

    # ── Mouse ─────────────────────────────────────────────────────

    def click(self, x: float, y: float) -> ActionResult:
        """Click at coordinates."""
        return self._client.computers.click(self.id, x=x, y=y)

    def double_click(self, x: float, y: float) -> ActionResult:
        """Double-click at coordinates."""
        return self._client.computers.double_click(self.id, x=x, y=y)

    def right_click(self, x: float, y: float) -> ActionResult:
        """Right-click at coordinates."""
        return self._client.computers.right_click(self.id, x=x, y=y)

    def drag(self, x1: float, y1: float, x2: float, y2: float) -> ActionResult:
        """Drag from (x1, y1) to (x2, y2)."""
        return self._client.computers.drag(self.id, x1=x1, y1=y1, x2=x2, y2=y2)

    def mouse_down(self, x: float, y: float) -> ActionResult:
        """Press mouse button at coordinates."""
        return self._client.computers.mouse_down(self.id, x=x, y=y)

    def mouse_up(self, x: float, y: float) -> ActionResult:
        """Release mouse button at coordinates."""
        return self._client.computers.mouse_up(self.id, x=x, y=y)

    # ── Keyboard ──────────────────────────────────────────────────

    def type(self, text: str) -> ActionResult:
        """Type text into the focused element."""
        return self._client.computers.type(self.id, text=text)

    def hotkey(self, *keys: str | list[str] | tuple[str, ...]) -> ActionResult:
        """
        Press a keyboard shortcut.

        Accepts varargs or a single list/tuple::

            computer.hotkey("Control", "c")
            computer.hotkey(["Control", "v"])
        """
        keys_list: list[str]
        if len(keys) == 1 and isinstance(keys[0], (list, tuple)):
            keys_list = list(keys[0])
        else:
            keys_list = cast(list[str], list(keys))
        return self._client.computers.hotkey(self.id, keys=keys_list)

    def key_down(self, key: str) -> ActionResult:
        """Press and hold a key."""
        return self._client.computers.key_down(self.id, key=key)

    def key_up(self, key: str) -> ActionResult:
        """Release a held key."""
        return self._client.computers.key_up(self.id, key=key)

    # ── Scrolling & Viewport ──────────────────────────────────────

    def scroll(self, dx: float = 0, dy: float = 0, x: float = 0, y: float = 0) -> ActionResult:
        """
        Scroll the viewport.

        Args:
            dx: Horizontal scroll delta (positive = right)
            dy: Vertical scroll delta (positive = down)
            x: Scroll origin X coordinate
            y: Scroll origin Y coordinate
        """
        return self._client.computers.scroll(self.id, dx=dx, dy=dy, x=x, y=y)

    def set_viewport(self, width: int, height: int, scale_factor: float = 1.0) -> ActionResult:
        """Change viewport dimensions."""
        result = self._client.computers.viewport(self.id, width=width, height=height, scale_factor=scale_factor)
        self.width = width
        self.height = height
        return result

    # ── Content ───────────────────────────────────────────────────

    def screenshot(self, base64: bool = False) -> ActionResult:
        """
        Capture a screenshot.

        Use ``get_screenshot_url(result)`` to extract the URL from the result.
        """
        return self._client.computers.screenshot(self.id, base64=base64)

    def html(self, auto_detect_encoding: bool = False) -> ActionResult:
        """
        Get page HTML content.

        Use ``get_html_content(result)`` to extract the HTML from the result.
        """
        return self._client.computers.html(self.id, auto_detect_encoding=auto_detect_encoding)

    # ── Shell / Debug ─────────────────────────────────────────────

    def debug(self, command: str, timeout_seconds: int = 120, max_output_length: int = 65536) -> ActionResult:
        """
        Execute a debug/shell command.

        Use ``get_debug_response(result)`` to extract the output from the result.
        """
        return self._client.computers.debug(
            self.id, command=command, timeout_seconds=timeout_seconds, max_output_length=max_output_length
        )

    # ── Timing ────────────────────────────────────────────────────

    def wait(self, seconds: float) -> ActionResult:
        """
        Wait for a duration on the remote computer.

        Args:
            seconds: Seconds to wait (e.g. 0.5 for 500ms)
        """
        ms = int(seconds * 1000)
        return self._client.computers.execute(self.id, action={"type": "wait", "ms": ms})

    # ── Generic / Batch ───────────────────────────────────────────

    def execute(self, action: ComputerActionParam) -> ActionResult:
        """
        Execute a single generic action.

        Useful for actions without dedicated methods (tab ops, etc.)::

            computer.execute({"type": "new_tab", "url": "https://example.com"})
            computer.execute({"type": "switch_tab", "tab_id": "tab_123"})
        """
        return self._client.computers.execute(self.id, action=action)

    def batch(self, actions: Iterable[ComputerActionParam]) -> ComputerBatchResponse:
        """
        Execute multiple actions in sequence with a single API call.

        Stops on first error::

            computer.batch([
                {"type": "go_to_url", "url": "https://example.com"},
                {"type": "wait", "ms": 2000},
                {"type": "click", "x": 100, "y": 200},
                {"type": "screenshot"},
            ])
        """
        return self._client.computers.batch(self.id, actions=actions)

    # ── Session management ────────────────────────────────────────

    def keep_alive(self) -> ComputerKeepaliveResponse:
        """Extend session timeout to prevent automatic termination."""
        return self._client.computers.keepalive(self.id)

    def retrieve(self) -> ComputerResponse:
        """Get current session status and metadata."""
        return self._client.computers.retrieve(self.id)

    def terminate(self) -> None:
        """Terminate the session and clean up resources."""
        self._client.computers.delete(self.id)

    # ── Result helpers ────────────────────────────────────────────

    @staticmethod
    def get_screenshot_url(result: ActionResult) -> Optional[str]:
        """Extract screenshot URL from an ActionResult."""
        if result.result:
            return result.result.get("screenshot_url")  # type: ignore[return-value]
        return None

    @staticmethod
    def get_html_content(result: ActionResult) -> Optional[str]:
        """Extract HTML content from an ActionResult."""
        if result.result:
            return result.result.get("html_content")  # type: ignore[return-value]
        return None

    @staticmethod
    def get_debug_response(result: ActionResult) -> Optional[str]:
        """Extract debug command output from an ActionResult."""
        if result.result:
            return result.result.get("debug_response")  # type: ignore[return-value]
        return None

    # ── Context manager ───────────────────────────────────────────

    def __enter__(self) -> ComputerSession:
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        self.terminate()

    @override
    def __repr__(self) -> str:
        return f"ComputerSession(id={self.id!r})"
