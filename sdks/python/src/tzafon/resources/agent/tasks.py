# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ...types.agent import task_start_params, task_start_stream_params, task_inject_message_params
from ..._base_client import make_request_options
from ...types.agent.task_pause_response import TaskPauseResponse
from ...types.agent.task_start_response import TaskStartResponse
from ...types.agent.task_resume_response import TaskResumeResponse
from ...types.agent.task_start_stream_response import TaskStartStreamResponse
from ...types.agent.task_inject_message_response import TaskInjectMessageResponse
from ...types.agent.task_retrieve_status_response import TaskRetrieveStatusResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tzafon/lightcone-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tzafon/lightcone-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def inject_message(
        self,
        id: str,
        *,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskInjectMessageResponse:
        """
        Injects a message into a running agent task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/agent/tasks/{id}/messages", id=id),
            body=maybe_transform({"message": message}, task_inject_message_params.TaskInjectMessageParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskInjectMessageResponse,
        )

    def pause(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskPauseResponse:
        """
        Pauses a running agent task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/agent/tasks/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskPauseResponse,
        )

    def resume(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskResumeResponse:
        """
        Resumes a paused agent task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/agent/tasks/{id}/resume", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskResumeResponse,
        )

    def retrieve_status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRetrieveStatusResponse:
        """
        Returns the current status/result for a task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/agent/tasks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveStatusResponse,
        )

    def start(
        self,
        *,
        instruction: str,
        agent_icon: str | Omit = omit,
        agent_type: str | Omit = omit,
        computer_id: str | Omit = omit,
        context: Iterable[task_start_params.Context] | Omit = omit,
        environment_id: str | Omit = omit,
        harness_version: Literal["v1", "v2"] | Omit = omit,
        idempotency_key: str | Omit = omit,
        keep_alive: bool | Omit = omit,
        kind: Literal["desktop", "browser"] | Omit = omit,
        max_duration_seconds: int | Omit = omit,
        max_steps: int | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        model: str | Omit = omit,
        on_missing_computer: Literal["fail", "restore", "create_new"] | Omit = omit,
        persistent: bool | Omit = omit,
        save_session: bool | Omit = omit,
        screenshot_mode: Literal["url", "base64"] | Omit = omit,
        start_url: str | Omit = omit,
        stream_deltas: bool | Omit = omit,
        stream_mode: Literal["verbose", "concise"] | Omit = omit,
        system_prompt: str | Omit = omit,
        temperature: float | Omit = omit,
        terminate_on_completion: bool | Omit = omit,
        thread_id: str | Omit = omit,
        viewport_height: int | Omit = omit,
        viewport_width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskStartResponse:
        """
        Starts an agent task and returns a task_id immediately.

        Args:
          instruction: Instruction is the task prompt for the agent.

          agent_icon: AgentIcon is optional client metadata used by task history UIs. It is captured
              by go-backend before proxying and ignored by older agent servers.

          agent_type: AgentType is accepted for legacy clients. Current agent servers ignore it.

          computer_id: ComputerID reuses a live computer session, or restores a saved persistent
              session with the same ID if it is not currently live.

          context: Context seeds the worker transcript with recent conversation turns, oldest
              first.

          environment_id: EnvironmentID restores a previous persistent session snapshot. Prefer ComputerID
              with the saved computer/session ID for new integrations.

          harness_version: HarnessVersion selects which agent harness implementation runs the task. "v1" is
              the stable/core harness with broader shell/search tools. "v2" is the
              training-aligned GUI harness.

          idempotency_key: IdempotencyKey deduplicates retried task start requests.

          keep_alive: KeepAlive is a user-friendly alias for terminate_on_completion=false.

          kind:
              Kind selects the virtual environment type. Omit to use the agent default:
              browser when start_url is set, otherwise desktop. Saved computer_id sessions
              restore using the stored session kind.

          max_duration_seconds: MaxDurationSeconds caps wall-clock runtime before the server cancels the task.

          max_steps: MaxSteps caps how many agent loop steps can run before max-steps termination.

          metadata: Metadata is customer-defined task metadata for correlating with external
              workflows.

          model: Model is the LLM model to use. Omit to use the agent server default.

          on_missing_computer: OnMissingComputer controls fallback when ComputerID is not live: "restore"
              (default) restores a saved persistent session or returns 404, "fail" always
              returns 404, "create_new" restores when possible and otherwise creates a fresh
              computer.

          persistent: Persistent controls whether the computer session should persist state on
              teardown.

          save_session: SaveSession is a user-friendly alias for Persistent.

          screenshot_mode: ScreenshotMode controls whether task screenshots are emitted as URLs or base64
              data URLs.

          start_url: StartURL opens this URL before the agent starts. Omitted kind defaults to
              browser.

          stream_deltas: StreamDeltas streams per-token text deltas as progress_update events when
              supported.

          stream_mode: StreamMode controls event verbosity. "verbose" emits all events; "concise" emits
              product-facing progress, screenshots, completion, and errors.

          system_prompt: SystemPrompt is appended to the harness system message.

          temperature: Temperature controls LLM sampling temperature. Omit to use the harness default.

          terminate_on_completion: TerminateOnCompletion controls whether the task should terminate its computer
              automatically. Set false to keep the computer alive for handoff or inspection.

          thread_id: ThreadID is optional client metadata for grouping task history by chat thread.
              It is captured by go-backend before proxying and ignored by older agent servers.

          viewport_height: ViewportHeight is the browser viewport height in pixels.

          viewport_width: ViewportWidth is the browser viewport width in pixels.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agent/tasks",
            body=maybe_transform(
                {
                    "instruction": instruction,
                    "agent_icon": agent_icon,
                    "agent_type": agent_type,
                    "computer_id": computer_id,
                    "context": context,
                    "environment_id": environment_id,
                    "harness_version": harness_version,
                    "idempotency_key": idempotency_key,
                    "keep_alive": keep_alive,
                    "kind": kind,
                    "max_duration_seconds": max_duration_seconds,
                    "max_steps": max_steps,
                    "metadata": metadata,
                    "model": model,
                    "on_missing_computer": on_missing_computer,
                    "persistent": persistent,
                    "save_session": save_session,
                    "screenshot_mode": screenshot_mode,
                    "start_url": start_url,
                    "stream_deltas": stream_deltas,
                    "stream_mode": stream_mode,
                    "system_prompt": system_prompt,
                    "temperature": temperature,
                    "terminate_on_completion": terminate_on_completion,
                    "thread_id": thread_id,
                    "viewport_height": viewport_height,
                    "viewport_width": viewport_width,
                },
                task_start_params.TaskStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskStartResponse,
        )

    def start_stream(
        self,
        *,
        instruction: str,
        agent_icon: str | Omit = omit,
        agent_type: str | Omit = omit,
        computer_id: str | Omit = omit,
        context: Iterable[task_start_stream_params.Context] | Omit = omit,
        environment_id: str | Omit = omit,
        harness_version: Literal["v1", "v2"] | Omit = omit,
        idempotency_key: str | Omit = omit,
        keep_alive: bool | Omit = omit,
        kind: Literal["desktop", "browser"] | Omit = omit,
        max_duration_seconds: int | Omit = omit,
        max_steps: int | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        model: str | Omit = omit,
        on_missing_computer: Literal["fail", "restore", "create_new"] | Omit = omit,
        persistent: bool | Omit = omit,
        save_session: bool | Omit = omit,
        screenshot_mode: Literal["url", "base64"] | Omit = omit,
        start_url: str | Omit = omit,
        stream_deltas: bool | Omit = omit,
        stream_mode: Literal["verbose", "concise"] | Omit = omit,
        system_prompt: str | Omit = omit,
        temperature: float | Omit = omit,
        terminate_on_completion: bool | Omit = omit,
        thread_id: str | Omit = omit,
        viewport_height: int | Omit = omit,
        viewport_width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[TaskStartStreamResponse]:
        """
        Starts an agent task and streams events via SSE (Content-Type:
        text/event-stream).

        Args:
          instruction: Instruction is the task prompt for the agent.

          agent_icon: AgentIcon is optional client metadata used by task history UIs. It is captured
              by go-backend before proxying and ignored by older agent servers.

          agent_type: AgentType is accepted for legacy clients. Current agent servers ignore it.

          computer_id: ComputerID reuses a live computer session, or restores a saved persistent
              session with the same ID if it is not currently live.

          context: Context seeds the worker transcript with recent conversation turns, oldest
              first.

          environment_id: EnvironmentID restores a previous persistent session snapshot. Prefer ComputerID
              with the saved computer/session ID for new integrations.

          harness_version: HarnessVersion selects which agent harness implementation runs the task. "v1" is
              the stable/core harness with broader shell/search tools. "v2" is the
              training-aligned GUI harness.

          idempotency_key: IdempotencyKey deduplicates retried task start requests.

          keep_alive: KeepAlive is a user-friendly alias for terminate_on_completion=false.

          kind:
              Kind selects the virtual environment type. Omit to use the agent default:
              browser when start_url is set, otherwise desktop. Saved computer_id sessions
              restore using the stored session kind.

          max_duration_seconds: MaxDurationSeconds caps wall-clock runtime before the server cancels the task.

          max_steps: MaxSteps caps how many agent loop steps can run before max-steps termination.

          metadata: Metadata is customer-defined task metadata for correlating with external
              workflows.

          model: Model is the LLM model to use. Omit to use the agent server default.

          on_missing_computer: OnMissingComputer controls fallback when ComputerID is not live: "restore"
              (default) restores a saved persistent session or returns 404, "fail" always
              returns 404, "create_new" restores when possible and otherwise creates a fresh
              computer.

          persistent: Persistent controls whether the computer session should persist state on
              teardown.

          save_session: SaveSession is a user-friendly alias for Persistent.

          screenshot_mode: ScreenshotMode controls whether task screenshots are emitted as URLs or base64
              data URLs.

          start_url: StartURL opens this URL before the agent starts. Omitted kind defaults to
              browser.

          stream_deltas: StreamDeltas streams per-token text deltas as progress_update events when
              supported.

          stream_mode: StreamMode controls event verbosity. "verbose" emits all events; "concise" emits
              product-facing progress, screenshots, completion, and errors.

          system_prompt: SystemPrompt is appended to the harness system message.

          temperature: Temperature controls LLM sampling temperature. Omit to use the harness default.

          terminate_on_completion: TerminateOnCompletion controls whether the task should terminate its computer
              automatically. Set false to keep the computer alive for handoff or inspection.

          thread_id: ThreadID is optional client metadata for grouping task history by chat thread.
              It is captured by go-backend before proxying and ignored by older agent servers.

          viewport_height: ViewportHeight is the browser viewport height in pixels.

          viewport_width: ViewportWidth is the browser viewport width in pixels.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/agent/tasks/stream",
            body=maybe_transform(
                {
                    "instruction": instruction,
                    "agent_icon": agent_icon,
                    "agent_type": agent_type,
                    "computer_id": computer_id,
                    "context": context,
                    "environment_id": environment_id,
                    "harness_version": harness_version,
                    "idempotency_key": idempotency_key,
                    "keep_alive": keep_alive,
                    "kind": kind,
                    "max_duration_seconds": max_duration_seconds,
                    "max_steps": max_steps,
                    "metadata": metadata,
                    "model": model,
                    "on_missing_computer": on_missing_computer,
                    "persistent": persistent,
                    "save_session": save_session,
                    "screenshot_mode": screenshot_mode,
                    "start_url": start_url,
                    "stream_deltas": stream_deltas,
                    "stream_mode": stream_mode,
                    "system_prompt": system_prompt,
                    "temperature": temperature,
                    "terminate_on_completion": terminate_on_completion,
                    "thread_id": thread_id,
                    "viewport_height": viewport_height,
                    "viewport_width": viewport_width,
                },
                task_start_stream_params.TaskStartStreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=Stream[TaskStartStreamResponse],
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tzafon/lightcone-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tzafon/lightcone-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def inject_message(
        self,
        id: str,
        *,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskInjectMessageResponse:
        """
        Injects a message into a running agent task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/agent/tasks/{id}/messages", id=id),
            body=await async_maybe_transform({"message": message}, task_inject_message_params.TaskInjectMessageParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskInjectMessageResponse,
        )

    async def pause(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskPauseResponse:
        """
        Pauses a running agent task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/agent/tasks/{id}/pause", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskPauseResponse,
        )

    async def resume(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskResumeResponse:
        """
        Resumes a paused agent task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/agent/tasks/{id}/resume", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskResumeResponse,
        )

    async def retrieve_status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRetrieveStatusResponse:
        """
        Returns the current status/result for a task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/agent/tasks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveStatusResponse,
        )

    async def start(
        self,
        *,
        instruction: str,
        agent_icon: str | Omit = omit,
        agent_type: str | Omit = omit,
        computer_id: str | Omit = omit,
        context: Iterable[task_start_params.Context] | Omit = omit,
        environment_id: str | Omit = omit,
        harness_version: Literal["v1", "v2"] | Omit = omit,
        idempotency_key: str | Omit = omit,
        keep_alive: bool | Omit = omit,
        kind: Literal["desktop", "browser"] | Omit = omit,
        max_duration_seconds: int | Omit = omit,
        max_steps: int | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        model: str | Omit = omit,
        on_missing_computer: Literal["fail", "restore", "create_new"] | Omit = omit,
        persistent: bool | Omit = omit,
        save_session: bool | Omit = omit,
        screenshot_mode: Literal["url", "base64"] | Omit = omit,
        start_url: str | Omit = omit,
        stream_deltas: bool | Omit = omit,
        stream_mode: Literal["verbose", "concise"] | Omit = omit,
        system_prompt: str | Omit = omit,
        temperature: float | Omit = omit,
        terminate_on_completion: bool | Omit = omit,
        thread_id: str | Omit = omit,
        viewport_height: int | Omit = omit,
        viewport_width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskStartResponse:
        """
        Starts an agent task and returns a task_id immediately.

        Args:
          instruction: Instruction is the task prompt for the agent.

          agent_icon: AgentIcon is optional client metadata used by task history UIs. It is captured
              by go-backend before proxying and ignored by older agent servers.

          agent_type: AgentType is accepted for legacy clients. Current agent servers ignore it.

          computer_id: ComputerID reuses a live computer session, or restores a saved persistent
              session with the same ID if it is not currently live.

          context: Context seeds the worker transcript with recent conversation turns, oldest
              first.

          environment_id: EnvironmentID restores a previous persistent session snapshot. Prefer ComputerID
              with the saved computer/session ID for new integrations.

          harness_version: HarnessVersion selects which agent harness implementation runs the task. "v1" is
              the stable/core harness with broader shell/search tools. "v2" is the
              training-aligned GUI harness.

          idempotency_key: IdempotencyKey deduplicates retried task start requests.

          keep_alive: KeepAlive is a user-friendly alias for terminate_on_completion=false.

          kind:
              Kind selects the virtual environment type. Omit to use the agent default:
              browser when start_url is set, otherwise desktop. Saved computer_id sessions
              restore using the stored session kind.

          max_duration_seconds: MaxDurationSeconds caps wall-clock runtime before the server cancels the task.

          max_steps: MaxSteps caps how many agent loop steps can run before max-steps termination.

          metadata: Metadata is customer-defined task metadata for correlating with external
              workflows.

          model: Model is the LLM model to use. Omit to use the agent server default.

          on_missing_computer: OnMissingComputer controls fallback when ComputerID is not live: "restore"
              (default) restores a saved persistent session or returns 404, "fail" always
              returns 404, "create_new" restores when possible and otherwise creates a fresh
              computer.

          persistent: Persistent controls whether the computer session should persist state on
              teardown.

          save_session: SaveSession is a user-friendly alias for Persistent.

          screenshot_mode: ScreenshotMode controls whether task screenshots are emitted as URLs or base64
              data URLs.

          start_url: StartURL opens this URL before the agent starts. Omitted kind defaults to
              browser.

          stream_deltas: StreamDeltas streams per-token text deltas as progress_update events when
              supported.

          stream_mode: StreamMode controls event verbosity. "verbose" emits all events; "concise" emits
              product-facing progress, screenshots, completion, and errors.

          system_prompt: SystemPrompt is appended to the harness system message.

          temperature: Temperature controls LLM sampling temperature. Omit to use the harness default.

          terminate_on_completion: TerminateOnCompletion controls whether the task should terminate its computer
              automatically. Set false to keep the computer alive for handoff or inspection.

          thread_id: ThreadID is optional client metadata for grouping task history by chat thread.
              It is captured by go-backend before proxying and ignored by older agent servers.

          viewport_height: ViewportHeight is the browser viewport height in pixels.

          viewport_width: ViewportWidth is the browser viewport width in pixels.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agent/tasks",
            body=await async_maybe_transform(
                {
                    "instruction": instruction,
                    "agent_icon": agent_icon,
                    "agent_type": agent_type,
                    "computer_id": computer_id,
                    "context": context,
                    "environment_id": environment_id,
                    "harness_version": harness_version,
                    "idempotency_key": idempotency_key,
                    "keep_alive": keep_alive,
                    "kind": kind,
                    "max_duration_seconds": max_duration_seconds,
                    "max_steps": max_steps,
                    "metadata": metadata,
                    "model": model,
                    "on_missing_computer": on_missing_computer,
                    "persistent": persistent,
                    "save_session": save_session,
                    "screenshot_mode": screenshot_mode,
                    "start_url": start_url,
                    "stream_deltas": stream_deltas,
                    "stream_mode": stream_mode,
                    "system_prompt": system_prompt,
                    "temperature": temperature,
                    "terminate_on_completion": terminate_on_completion,
                    "thread_id": thread_id,
                    "viewport_height": viewport_height,
                    "viewport_width": viewport_width,
                },
                task_start_params.TaskStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskStartResponse,
        )

    async def start_stream(
        self,
        *,
        instruction: str,
        agent_icon: str | Omit = omit,
        agent_type: str | Omit = omit,
        computer_id: str | Omit = omit,
        context: Iterable[task_start_stream_params.Context] | Omit = omit,
        environment_id: str | Omit = omit,
        harness_version: Literal["v1", "v2"] | Omit = omit,
        idempotency_key: str | Omit = omit,
        keep_alive: bool | Omit = omit,
        kind: Literal["desktop", "browser"] | Omit = omit,
        max_duration_seconds: int | Omit = omit,
        max_steps: int | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        model: str | Omit = omit,
        on_missing_computer: Literal["fail", "restore", "create_new"] | Omit = omit,
        persistent: bool | Omit = omit,
        save_session: bool | Omit = omit,
        screenshot_mode: Literal["url", "base64"] | Omit = omit,
        start_url: str | Omit = omit,
        stream_deltas: bool | Omit = omit,
        stream_mode: Literal["verbose", "concise"] | Omit = omit,
        system_prompt: str | Omit = omit,
        temperature: float | Omit = omit,
        terminate_on_completion: bool | Omit = omit,
        thread_id: str | Omit = omit,
        viewport_height: int | Omit = omit,
        viewport_width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[TaskStartStreamResponse]:
        """
        Starts an agent task and streams events via SSE (Content-Type:
        text/event-stream).

        Args:
          instruction: Instruction is the task prompt for the agent.

          agent_icon: AgentIcon is optional client metadata used by task history UIs. It is captured
              by go-backend before proxying and ignored by older agent servers.

          agent_type: AgentType is accepted for legacy clients. Current agent servers ignore it.

          computer_id: ComputerID reuses a live computer session, or restores a saved persistent
              session with the same ID if it is not currently live.

          context: Context seeds the worker transcript with recent conversation turns, oldest
              first.

          environment_id: EnvironmentID restores a previous persistent session snapshot. Prefer ComputerID
              with the saved computer/session ID for new integrations.

          harness_version: HarnessVersion selects which agent harness implementation runs the task. "v1" is
              the stable/core harness with broader shell/search tools. "v2" is the
              training-aligned GUI harness.

          idempotency_key: IdempotencyKey deduplicates retried task start requests.

          keep_alive: KeepAlive is a user-friendly alias for terminate_on_completion=false.

          kind:
              Kind selects the virtual environment type. Omit to use the agent default:
              browser when start_url is set, otherwise desktop. Saved computer_id sessions
              restore using the stored session kind.

          max_duration_seconds: MaxDurationSeconds caps wall-clock runtime before the server cancels the task.

          max_steps: MaxSteps caps how many agent loop steps can run before max-steps termination.

          metadata: Metadata is customer-defined task metadata for correlating with external
              workflows.

          model: Model is the LLM model to use. Omit to use the agent server default.

          on_missing_computer: OnMissingComputer controls fallback when ComputerID is not live: "restore"
              (default) restores a saved persistent session or returns 404, "fail" always
              returns 404, "create_new" restores when possible and otherwise creates a fresh
              computer.

          persistent: Persistent controls whether the computer session should persist state on
              teardown.

          save_session: SaveSession is a user-friendly alias for Persistent.

          screenshot_mode: ScreenshotMode controls whether task screenshots are emitted as URLs or base64
              data URLs.

          start_url: StartURL opens this URL before the agent starts. Omitted kind defaults to
              browser.

          stream_deltas: StreamDeltas streams per-token text deltas as progress_update events when
              supported.

          stream_mode: StreamMode controls event verbosity. "verbose" emits all events; "concise" emits
              product-facing progress, screenshots, completion, and errors.

          system_prompt: SystemPrompt is appended to the harness system message.

          temperature: Temperature controls LLM sampling temperature. Omit to use the harness default.

          terminate_on_completion: TerminateOnCompletion controls whether the task should terminate its computer
              automatically. Set false to keep the computer alive for handoff or inspection.

          thread_id: ThreadID is optional client metadata for grouping task history by chat thread.
              It is captured by go-backend before proxying and ignored by older agent servers.

          viewport_height: ViewportHeight is the browser viewport height in pixels.

          viewport_width: ViewportWidth is the browser viewport width in pixels.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/agent/tasks/stream",
            body=await async_maybe_transform(
                {
                    "instruction": instruction,
                    "agent_icon": agent_icon,
                    "agent_type": agent_type,
                    "computer_id": computer_id,
                    "context": context,
                    "environment_id": environment_id,
                    "harness_version": harness_version,
                    "idempotency_key": idempotency_key,
                    "keep_alive": keep_alive,
                    "kind": kind,
                    "max_duration_seconds": max_duration_seconds,
                    "max_steps": max_steps,
                    "metadata": metadata,
                    "model": model,
                    "on_missing_computer": on_missing_computer,
                    "persistent": persistent,
                    "save_session": save_session,
                    "screenshot_mode": screenshot_mode,
                    "start_url": start_url,
                    "stream_deltas": stream_deltas,
                    "stream_mode": stream_mode,
                    "system_prompt": system_prompt,
                    "temperature": temperature,
                    "terminate_on_completion": terminate_on_completion,
                    "thread_id": thread_id,
                    "viewport_height": viewport_height,
                    "viewport_width": viewport_width,
                },
                task_start_stream_params.TaskStartStreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[TaskStartStreamResponse],
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.inject_message = to_raw_response_wrapper(
            tasks.inject_message,
        )
        self.pause = to_raw_response_wrapper(
            tasks.pause,
        )
        self.resume = to_raw_response_wrapper(
            tasks.resume,
        )
        self.retrieve_status = to_raw_response_wrapper(
            tasks.retrieve_status,
        )
        self.start = to_raw_response_wrapper(
            tasks.start,
        )
        self.start_stream = to_raw_response_wrapper(
            tasks.start_stream,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.inject_message = async_to_raw_response_wrapper(
            tasks.inject_message,
        )
        self.pause = async_to_raw_response_wrapper(
            tasks.pause,
        )
        self.resume = async_to_raw_response_wrapper(
            tasks.resume,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            tasks.retrieve_status,
        )
        self.start = async_to_raw_response_wrapper(
            tasks.start,
        )
        self.start_stream = async_to_raw_response_wrapper(
            tasks.start_stream,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.inject_message = to_streamed_response_wrapper(
            tasks.inject_message,
        )
        self.pause = to_streamed_response_wrapper(
            tasks.pause,
        )
        self.resume = to_streamed_response_wrapper(
            tasks.resume,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            tasks.retrieve_status,
        )
        self.start = to_streamed_response_wrapper(
            tasks.start,
        )
        self.start_stream = to_streamed_response_wrapper(
            tasks.start_stream,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.inject_message = async_to_streamed_response_wrapper(
            tasks.inject_message,
        )
        self.pause = async_to_streamed_response_wrapper(
            tasks.pause,
        )
        self.resume = async_to_streamed_response_wrapper(
            tasks.resume,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            tasks.retrieve_status,
        )
        self.start = async_to_streamed_response_wrapper(
            tasks.start,
        )
        self.start_stream = async_to_streamed_response_wrapper(
            tasks.start_stream,
        )
