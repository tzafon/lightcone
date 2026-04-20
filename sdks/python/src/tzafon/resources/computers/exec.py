# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

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
from ..._base_client import make_request_options
from ..._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ...types.computers import exec_sync_params, exec_create_params
from ...types.computers.exec_sync_response import ExecSyncResponse
from ...types.computers.exec_create_response import ExecCreateResponse

__all__ = ["ExecResource", "AsyncExecResource"]


class ExecResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExecResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tzafon/lightcone-python#accessing-raw-response-data-eg-headers
        """
        return ExecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tzafon/lightcone-python#with_streaming_response
        """
        return ExecResourceWithStreamingResponse(self)

    def create(
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
    ) -> JSONLDecoder[ExecCreateResponse]:
        """
        Execute a shell command (desktop sessions only) and stream output back as
        newline-delimited JSON. Each line is a `types.ExecOutput` object whose `type` is
        one of `stdout`, `stderr`, `exit`, or `error`. The stream terminates with a
        single `{"type":"exit","code":<int>}` line; code `-1` indicates timeout or
        abnormal termination.

        **Error model:** this endpoint always returns HTTP 200 and reports failures
        (invalid JSON body, missing command, stream-setup failure) as a single
        `{"type":"error","code":"<CODE>","message":"..."}` NDJSON line followed by
        connection close. Clients MUST parse the first line rather than relying on HTTP
        status codes.

        Output is filtered server-side by request ID, so concurrent `/exec` calls on the
        same computer don't interleave. Defaults: `cwd=/workspace`,
        `timeout_seconds=120`.

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
            path_template("/computers/{id}/exec", id=id),
            body=maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "timeout_seconds": timeout_seconds,
                },
                exec_create_params.ExecCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JSONLDecoder[ExecCreateResponse],
            stream=True,
        )

    def sync(
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
    ) -> ExecSyncResponse:
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
            path_template("/computers/{id}/exec/sync", id=id),
            body=maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "timeout_seconds": timeout_seconds,
                },
                exec_sync_params.ExecSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecSyncResponse,
        )


class AsyncExecResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExecResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tzafon/lightcone-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tzafon/lightcone-python#with_streaming_response
        """
        return AsyncExecResourceWithStreamingResponse(self)

    async def create(
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
    ) -> AsyncJSONLDecoder[ExecCreateResponse]:
        """
        Execute a shell command (desktop sessions only) and stream output back as
        newline-delimited JSON. Each line is a `types.ExecOutput` object whose `type` is
        one of `stdout`, `stderr`, `exit`, or `error`. The stream terminates with a
        single `{"type":"exit","code":<int>}` line; code `-1` indicates timeout or
        abnormal termination.

        **Error model:** this endpoint always returns HTTP 200 and reports failures
        (invalid JSON body, missing command, stream-setup failure) as a single
        `{"type":"error","code":"<CODE>","message":"..."}` NDJSON line followed by
        connection close. Clients MUST parse the first line rather than relying on HTTP
        status codes.

        Output is filtered server-side by request ID, so concurrent `/exec` calls on the
        same computer don't interleave. Defaults: `cwd=/workspace`,
        `timeout_seconds=120`.

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
            path_template("/computers/{id}/exec", id=id),
            body=await async_maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "timeout_seconds": timeout_seconds,
                },
                exec_create_params.ExecCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncJSONLDecoder[ExecCreateResponse],
            stream=True,
        )

    async def sync(
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
    ) -> ExecSyncResponse:
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
            path_template("/computers/{id}/exec/sync", id=id),
            body=await async_maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "timeout_seconds": timeout_seconds,
                },
                exec_sync_params.ExecSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecSyncResponse,
        )


class ExecResourceWithRawResponse:
    def __init__(self, exec: ExecResource) -> None:
        self._exec = exec

        self.create = to_raw_response_wrapper(
            exec.create,
        )
        self.sync = to_raw_response_wrapper(
            exec.sync,
        )


class AsyncExecResourceWithRawResponse:
    def __init__(self, exec: AsyncExecResource) -> None:
        self._exec = exec

        self.create = async_to_raw_response_wrapper(
            exec.create,
        )
        self.sync = async_to_raw_response_wrapper(
            exec.sync,
        )


class ExecResourceWithStreamingResponse:
    def __init__(self, exec: ExecResource) -> None:
        self._exec = exec

        self.create = to_streamed_response_wrapper(
            exec.create,
        )
        self.sync = to_streamed_response_wrapper(
            exec.sync,
        )


class AsyncExecResourceWithStreamingResponse:
    def __init__(self, exec: AsyncExecResource) -> None:
        self._exec = exec

        self.create = async_to_streamed_response_wrapper(
            exec.create,
        )
        self.sync = async_to_streamed_response_wrapper(
            exec.sync,
        )
