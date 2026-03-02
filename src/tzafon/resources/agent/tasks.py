# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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

        For more information, see https://www.github.com/tzafon/lightcone#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tzafon/lightcone#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def inject_message(
        self,
        id: str,
        *,
        message: str | Omit = omit,
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
            f"/agent/tasks/{id}/messages",
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
            f"/agent/tasks/{id}/pause",
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
            f"/agent/tasks/{id}/resume",
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
            f"/agent/tasks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveStatusResponse,
        )

    def start(
        self,
        *,
        agent_type: str | Omit = omit,
        environment_id: str | Omit = omit,
        instruction: str | Omit = omit,
        kind: Literal["desktop", "browser"] | Omit = omit,
        max_steps: int | Omit = omit,
        model: str | Omit = omit,
        persistent: bool | Omit = omit,
        screenshot_mode: Literal["url", "base64"] | Omit = omit,
        temperature: float | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agent/tasks",
            body=maybe_transform(
                {
                    "agent_type": agent_type,
                    "environment_id": environment_id,
                    "instruction": instruction,
                    "kind": kind,
                    "max_steps": max_steps,
                    "model": model,
                    "persistent": persistent,
                    "screenshot_mode": screenshot_mode,
                    "temperature": temperature,
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
        agent_type: str | Omit = omit,
        environment_id: str | Omit = omit,
        instruction: str | Omit = omit,
        kind: Literal["desktop", "browser"] | Omit = omit,
        max_steps: int | Omit = omit,
        model: str | Omit = omit,
        persistent: bool | Omit = omit,
        screenshot_mode: Literal["url", "base64"] | Omit = omit,
        temperature: float | Omit = omit,
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
                    "agent_type": agent_type,
                    "environment_id": environment_id,
                    "instruction": instruction,
                    "kind": kind,
                    "max_steps": max_steps,
                    "model": model,
                    "persistent": persistent,
                    "screenshot_mode": screenshot_mode,
                    "temperature": temperature,
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

        For more information, see https://www.github.com/tzafon/lightcone#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tzafon/lightcone#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def inject_message(
        self,
        id: str,
        *,
        message: str | Omit = omit,
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
            f"/agent/tasks/{id}/messages",
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
            f"/agent/tasks/{id}/pause",
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
            f"/agent/tasks/{id}/resume",
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
            f"/agent/tasks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveStatusResponse,
        )

    async def start(
        self,
        *,
        agent_type: str | Omit = omit,
        environment_id: str | Omit = omit,
        instruction: str | Omit = omit,
        kind: Literal["desktop", "browser"] | Omit = omit,
        max_steps: int | Omit = omit,
        model: str | Omit = omit,
        persistent: bool | Omit = omit,
        screenshot_mode: Literal["url", "base64"] | Omit = omit,
        temperature: float | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agent/tasks",
            body=await async_maybe_transform(
                {
                    "agent_type": agent_type,
                    "environment_id": environment_id,
                    "instruction": instruction,
                    "kind": kind,
                    "max_steps": max_steps,
                    "model": model,
                    "persistent": persistent,
                    "screenshot_mode": screenshot_mode,
                    "temperature": temperature,
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
        agent_type: str | Omit = omit,
        environment_id: str | Omit = omit,
        instruction: str | Omit = omit,
        kind: Literal["desktop", "browser"] | Omit = omit,
        max_steps: int | Omit = omit,
        model: str | Omit = omit,
        persistent: bool | Omit = omit,
        screenshot_mode: Literal["url", "base64"] | Omit = omit,
        temperature: float | Omit = omit,
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
                    "agent_type": agent_type,
                    "environment_id": environment_id,
                    "instruction": instruction,
                    "kind": kind,
                    "max_steps": max_steps,
                    "model": model,
                    "persistent": persistent,
                    "screenshot_mode": screenshot_mode,
                    "temperature": temperature,
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
