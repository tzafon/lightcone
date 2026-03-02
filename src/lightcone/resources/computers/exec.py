# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

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
from ..._base_client import make_request_options
from ..._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ...types.computers import exec_execute_params, exec_execute_sync_params
from ...types.computers.exec_execute_response import ExecExecuteResponse
from ...types.computers.exec_execute_sync_response import ExecExecuteSyncResponse

__all__ = ["ExecResource", "AsyncExecResource"]


class ExecResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExecResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lightcone-python#accessing-raw-response-data-eg-headers
        """
        return ExecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lightcone-python#with_streaming_response
        """
        return ExecResourceWithStreamingResponse(self)

    def execute(
        self,
        id: str,
        *,
        command: str | Omit = omit,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JSONLDecoder[ExecExecuteResponse]:
        """Execute a shell command with real-time streaming output as NDJSON.

        Each line is
        a JSON object with type (stdout/stderr/exit/error).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/x-ndjson", **(extra_headers or {})}
        return self._post(
            f"/computers/{id}/exec",
            body=maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "timeout_seconds": timeout_seconds,
                },
                exec_execute_params.ExecExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JSONLDecoder[ExecExecuteResponse],
            stream=True,
        )

    def execute_sync(
        self,
        id: str,
        *,
        command: str | Omit = omit,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecExecuteSyncResponse:
        """
        Execute a shell command and wait for completion, returning buffered
        stdout/stderr.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/computers/{id}/exec/sync",
            body=maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "timeout_seconds": timeout_seconds,
                },
                exec_execute_sync_params.ExecExecuteSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecExecuteSyncResponse,
        )


class AsyncExecResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExecResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lightcone-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lightcone-python#with_streaming_response
        """
        return AsyncExecResourceWithStreamingResponse(self)

    async def execute(
        self,
        id: str,
        *,
        command: str | Omit = omit,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncJSONLDecoder[ExecExecuteResponse]:
        """Execute a shell command with real-time streaming output as NDJSON.

        Each line is
        a JSON object with type (stdout/stderr/exit/error).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/x-ndjson", **(extra_headers or {})}
        return await self._post(
            f"/computers/{id}/exec",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "timeout_seconds": timeout_seconds,
                },
                exec_execute_params.ExecExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncJSONLDecoder[ExecExecuteResponse],
            stream=True,
        )

    async def execute_sync(
        self,
        id: str,
        *,
        command: str | Omit = omit,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecExecuteSyncResponse:
        """
        Execute a shell command and wait for completion, returning buffered
        stdout/stderr.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/computers/{id}/exec/sync",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "timeout_seconds": timeout_seconds,
                },
                exec_execute_sync_params.ExecExecuteSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecExecuteSyncResponse,
        )


class ExecResourceWithRawResponse:
    def __init__(self, exec: ExecResource) -> None:
        self._exec = exec

        self.execute = to_raw_response_wrapper(
            exec.execute,
        )
        self.execute_sync = to_raw_response_wrapper(
            exec.execute_sync,
        )


class AsyncExecResourceWithRawResponse:
    def __init__(self, exec: AsyncExecResource) -> None:
        self._exec = exec

        self.execute = async_to_raw_response_wrapper(
            exec.execute,
        )
        self.execute_sync = async_to_raw_response_wrapper(
            exec.execute_sync,
        )


class ExecResourceWithStreamingResponse:
    def __init__(self, exec: ExecResource) -> None:
        self._exec = exec

        self.execute = to_streamed_response_wrapper(
            exec.execute,
        )
        self.execute_sync = to_streamed_response_wrapper(
            exec.execute_sync,
        )


class AsyncExecResourceWithStreamingResponse:
    def __init__(self, exec: AsyncExecResource) -> None:
        self._exec = exec

        self.execute = async_to_streamed_response_wrapper(
            exec.execute,
        )
        self.execute_sync = async_to_streamed_response_wrapper(
            exec.execute_sync,
        )
