# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TaskStartStreamParams", "Context"]


class TaskStartStreamParams(TypedDict, total=False):
    instruction: Required[str]
    """Instruction is the task prompt for the agent."""

    agent_icon: str
    """
    AgentIcon is optional client metadata used by task history UIs. It is captured
    by go-backend before proxying and ignored by older agent servers.
    """

    agent_type: str
    """AgentType is accepted for legacy clients. Current agent servers ignore it."""

    computer_id: str
    """
    ComputerID reuses a live computer session, or restores a saved persistent
    session with the same ID if it is not currently live.
    """

    context: Iterable[Context]
    """
    Context seeds the worker transcript with recent conversation turns, oldest
    first.
    """

    environment_id: str
    """
    EnvironmentID restores a previous persistent session snapshot. Prefer ComputerID
    with the saved computer/session ID for new integrations.
    """

    harness_version: Literal["v1", "v2"]
    """
    HarnessVersion selects which agent harness implementation runs the task. "v1" is
    the stable/core harness with broader shell/search tools. "v2" is the
    training-aligned GUI harness.
    """

    idempotency_key: str
    """IdempotencyKey deduplicates retried task start requests."""

    keep_alive: bool
    """KeepAlive is a user-friendly alias for terminate_on_completion=false."""

    kind: Literal["desktop", "browser"]
    """Kind selects the virtual environment type.

    Omit to use the agent default: browser when start_url is set, otherwise desktop.
    Saved computer_id sessions restore using the stored session kind.
    """

    max_duration_seconds: int
    """MaxDurationSeconds caps wall-clock runtime before the server cancels the task."""

    max_steps: int
    """MaxSteps caps how many agent loop steps can run before max-steps termination."""

    metadata: Dict[str, str]
    """
    Metadata is customer-defined task metadata for correlating with external
    workflows.
    """

    model: str
    """Model is the LLM model to use. Omit to use the agent server default."""

    on_missing_computer: Literal["fail", "restore", "create_new"]
    """
    OnMissingComputer controls fallback when ComputerID is not live: "restore"
    (default) restores a saved persistent session or returns 404, "fail" always
    returns 404, "create_new" restores when possible and otherwise creates a fresh
    computer.
    """

    persistent: bool
    """
    Persistent controls whether the computer session should persist state on
    teardown.
    """

    save_session: bool
    """SaveSession is a user-friendly alias for Persistent."""

    screenshot_mode: Literal["url", "base64"]
    """
    ScreenshotMode controls whether task screenshots are emitted as URLs or base64
    data URLs.
    """

    start_url: str
    """StartURL opens this URL before the agent starts.

    Omitted kind defaults to browser.
    """

    stream_deltas: bool
    """
    StreamDeltas streams per-token text deltas as progress_update events when
    supported.
    """

    stream_mode: Literal["verbose", "concise"]
    """StreamMode controls event verbosity.

    "verbose" emits all events; "concise" emits product-facing progress,
    screenshots, completion, and errors.
    """

    system_prompt: str
    """SystemPrompt is appended to the harness system message."""

    temperature: float
    """Temperature controls LLM sampling temperature. Omit to use the harness default."""

    terminate_on_completion: bool
    """
    TerminateOnCompletion controls whether the task should terminate its computer
    automatically. Set false to keep the computer alive for handoff or inspection.
    """

    thread_id: str
    """
    ThreadID is optional client metadata for grouping task history by chat thread.
    It is captured by go-backend before proxying and ignored by older agent servers.
    """

    viewport_height: int
    """ViewportHeight is the browser viewport height in pixels."""

    viewport_width: int
    """ViewportWidth is the browser viewport width in pixels."""


class Context(TypedDict, total=False):
    content: Required[str]
    """Content is the text of this prior conversation turn."""

    role: Required[Literal["user", "assistant"]]
    """Role is the speaker for this prior conversation turn."""
