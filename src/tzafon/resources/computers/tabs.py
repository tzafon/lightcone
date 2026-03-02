# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.computers import tab_create_params
from ...types.action_result import ActionResult

__all__ = ["TabsResource", "AsyncTabsResource"]


class TabsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TabsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tzafon/lightcone#accessing-raw-response-data-eg-headers
        """
        return TabsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TabsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tzafon/lightcone#with_streaming_response
        """
        return TabsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResult:
        """Create a new tab, optionally navigating to a URL.

        The new tab becomes the main
        tab (browser sessions only).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/computers/{id}/tabs",
            body=maybe_transform({"url": url}, tab_create_params.TabCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResult,
        )

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResult:
        """
        Get a list of open tabs with IDs, URLs, titles, and main tab status (browser
        sessions only). Includes external CDP pages (e.g., Playwright). Excludes
        devtools:// and chrome:// tabs. Results may be eventually consistent for newly
        created tabs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/computers/{id}/tabs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResult,
        )

    def delete(
        self,
        tab_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResult:
        """Close a specific tab by ID.

        Cannot close the last remaining tab (browser
        sessions only). Tab IDs come from ListTabs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not tab_id:
            raise ValueError(f"Expected a non-empty value for `tab_id` but received {tab_id!r}")
        return self._delete(
            f"/computers/{id}/tabs/{tab_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResult,
        )

    def switch(
        self,
        tab_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResult:
        """Switch the main/active tab to a different tab by ID (browser sessions only).

        Tab
        IDs come from ListTabs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not tab_id:
            raise ValueError(f"Expected a non-empty value for `tab_id` but received {tab_id!r}")
        return self._post(
            f"/computers/{id}/tabs/{tab_id}/switch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResult,
        )


class AsyncTabsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTabsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tzafon/lightcone#accessing-raw-response-data-eg-headers
        """
        return AsyncTabsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTabsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tzafon/lightcone#with_streaming_response
        """
        return AsyncTabsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResult:
        """Create a new tab, optionally navigating to a URL.

        The new tab becomes the main
        tab (browser sessions only).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/computers/{id}/tabs",
            body=await async_maybe_transform({"url": url}, tab_create_params.TabCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResult,
        )

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResult:
        """
        Get a list of open tabs with IDs, URLs, titles, and main tab status (browser
        sessions only). Includes external CDP pages (e.g., Playwright). Excludes
        devtools:// and chrome:// tabs. Results may be eventually consistent for newly
        created tabs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/computers/{id}/tabs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResult,
        )

    async def delete(
        self,
        tab_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResult:
        """Close a specific tab by ID.

        Cannot close the last remaining tab (browser
        sessions only). Tab IDs come from ListTabs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not tab_id:
            raise ValueError(f"Expected a non-empty value for `tab_id` but received {tab_id!r}")
        return await self._delete(
            f"/computers/{id}/tabs/{tab_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResult,
        )

    async def switch(
        self,
        tab_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResult:
        """Switch the main/active tab to a different tab by ID (browser sessions only).

        Tab
        IDs come from ListTabs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not tab_id:
            raise ValueError(f"Expected a non-empty value for `tab_id` but received {tab_id!r}")
        return await self._post(
            f"/computers/{id}/tabs/{tab_id}/switch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResult,
        )


class TabsResourceWithRawResponse:
    def __init__(self, tabs: TabsResource) -> None:
        self._tabs = tabs

        self.create = to_raw_response_wrapper(
            tabs.create,
        )
        self.list = to_raw_response_wrapper(
            tabs.list,
        )
        self.delete = to_raw_response_wrapper(
            tabs.delete,
        )
        self.switch = to_raw_response_wrapper(
            tabs.switch,
        )


class AsyncTabsResourceWithRawResponse:
    def __init__(self, tabs: AsyncTabsResource) -> None:
        self._tabs = tabs

        self.create = async_to_raw_response_wrapper(
            tabs.create,
        )
        self.list = async_to_raw_response_wrapper(
            tabs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tabs.delete,
        )
        self.switch = async_to_raw_response_wrapper(
            tabs.switch,
        )


class TabsResourceWithStreamingResponse:
    def __init__(self, tabs: TabsResource) -> None:
        self._tabs = tabs

        self.create = to_streamed_response_wrapper(
            tabs.create,
        )
        self.list = to_streamed_response_wrapper(
            tabs.list,
        )
        self.delete = to_streamed_response_wrapper(
            tabs.delete,
        )
        self.switch = to_streamed_response_wrapper(
            tabs.switch,
        )


class AsyncTabsResourceWithStreamingResponse:
    def __init__(self, tabs: AsyncTabsResource) -> None:
        self._tabs = tabs

        self.create = async_to_streamed_response_wrapper(
            tabs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            tabs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tabs.delete,
        )
        self.switch = async_to_streamed_response_wrapper(
            tabs.switch,
        )
