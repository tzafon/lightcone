# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import response_create_params, response_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ResponsesResource", "AsyncResponsesResource"]


class ResponsesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tzafon/lightcone-python#accessing-raw-response-data-eg-headers
        """
        return ResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tzafon/lightcone-python#with_streaming_response
        """
        return ResponsesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        background: Optional[bool] | Omit = omit,
        cache_salt: Optional[str] | Omit = omit,
        enable_response_messages: bool | Omit = omit,
        include: Optional[
            List[
                Literal[
                    "code_interpreter_call.outputs",
                    "computer_call_output.output.image_url",
                    "file_search_call.results",
                    "message.input_image.image_url",
                    "message.output_text.logprobs",
                    "reasoning.encrypted_content",
                ]
            ]
        ]
        | Omit = omit,
        include_stop_str_in_output: bool | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        logit_bias: Optional[Dict[str, float]] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        mm_processor_kwargs: Optional[Dict[str, object]] | Omit = omit,
        model: Optional[str] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        previous_input_messages: Optional[Iterable[response_create_params.PreviousInputMessage]] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        priority: int | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        request_id: str | Omit = omit,
        service_tier: Literal["auto", "default", "flex", "scale", "priority"] | Omit = omit,
        skip_special_tokens: bool | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create Responses

        Args:
          cache_salt: If specified, the prefix cache will be salted with the provided string to
              prevent an attacker to guess prompts in multi-user environments. The salt should
              be random, protected from access by 3rd parties, and long enough to be
              unpredictable (e.g., 43 characters base64-encoded, corresponding to 256 bit).

          enable_response_messages: Dictates whether or not to return messages as part of the response object.
              Currently only supported fornon-background and gpt-oss only.

          mm_processor_kwargs: Additional kwargs to pass to the HF processor.

          priority: The priority of the request (lower means earlier handling; default: 0). Any
              priority other than 0 will raise an error if the served model does not use
              priority scheduling.

          prompt: Reference to a prompt template and its variables.
              [Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

          prompt_cache_key: A key that was used to read from or write to the prompt cache.Note: This field
              has not been implemented yet and vLLM will ignore it.

          reasoning: **gpt-5 and o-series models only**

              Configuration options for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning).

          request_id: The request_id related to this request. If the caller does not set it, a
              random_uuid will be generated. This id is used through out the inference process
              and return in response.

          text: Configuration options for a text response from the model.

              Can be plain text or structured JSON data. Learn more:

              - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
              - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

          tool_choice: Constrains the tools available to the model to a pre-defined set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/responses",
            body=maybe_transform(
                {
                    "input": input,
                    "background": background,
                    "cache_salt": cache_salt,
                    "enable_response_messages": enable_response_messages,
                    "include": include,
                    "include_stop_str_in_output": include_stop_str_in_output,
                    "instructions": instructions,
                    "logit_bias": logit_bias,
                    "max_output_tokens": max_output_tokens,
                    "max_tool_calls": max_tool_calls,
                    "metadata": metadata,
                    "mm_processor_kwargs": mm_processor_kwargs,
                    "model": model,
                    "parallel_tool_calls": parallel_tool_calls,
                    "previous_input_messages": previous_input_messages,
                    "previous_response_id": previous_response_id,
                    "priority": priority,
                    "prompt": prompt,
                    "prompt_cache_key": prompt_cache_key,
                    "reasoning": reasoning,
                    "request_id": request_id,
                    "service_tier": service_tier,
                    "skip_special_tokens": skip_special_tokens,
                    "store": store,
                    "stream": stream,
                    "temperature": temperature,
                    "text": text,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "truncation": truncation,
                    "user": user,
                },
                response_create_params.ResponseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve(
        self,
        response_id: str,
        *,
        starting_after: Optional[int] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieve Responses

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return self._get(
            path_template("/v1/responses/{response_id}", response_id=response_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "starting_after": starting_after,
                        "stream": stream,
                    },
                    response_retrieve_params.ResponseRetrieveParams,
                ),
            ),
            cast_to=object,
        )

    def cancel(
        self,
        response_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Cancel Responses

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return self._post(
            path_template("/v1/responses/{response_id}/cancel", response_id=response_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncResponsesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tzafon/lightcone-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tzafon/lightcone-python#with_streaming_response
        """
        return AsyncResponsesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        background: Optional[bool] | Omit = omit,
        cache_salt: Optional[str] | Omit = omit,
        enable_response_messages: bool | Omit = omit,
        include: Optional[
            List[
                Literal[
                    "code_interpreter_call.outputs",
                    "computer_call_output.output.image_url",
                    "file_search_call.results",
                    "message.input_image.image_url",
                    "message.output_text.logprobs",
                    "reasoning.encrypted_content",
                ]
            ]
        ]
        | Omit = omit,
        include_stop_str_in_output: bool | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        logit_bias: Optional[Dict[str, float]] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        mm_processor_kwargs: Optional[Dict[str, object]] | Omit = omit,
        model: Optional[str] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        previous_input_messages: Optional[Iterable[response_create_params.PreviousInputMessage]] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        priority: int | Omit = omit,
        prompt: Optional[response_create_params.Prompt] | Omit = omit,
        prompt_cache_key: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        request_id: str | Omit = omit,
        service_tier: Literal["auto", "default", "flex", "scale", "priority"] | Omit = omit,
        skip_special_tokens: bool | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create Responses

        Args:
          cache_salt: If specified, the prefix cache will be salted with the provided string to
              prevent an attacker to guess prompts in multi-user environments. The salt should
              be random, protected from access by 3rd parties, and long enough to be
              unpredictable (e.g., 43 characters base64-encoded, corresponding to 256 bit).

          enable_response_messages: Dictates whether or not to return messages as part of the response object.
              Currently only supported fornon-background and gpt-oss only.

          mm_processor_kwargs: Additional kwargs to pass to the HF processor.

          priority: The priority of the request (lower means earlier handling; default: 0). Any
              priority other than 0 will raise an error if the served model does not use
              priority scheduling.

          prompt: Reference to a prompt template and its variables.
              [Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

          prompt_cache_key: A key that was used to read from or write to the prompt cache.Note: This field
              has not been implemented yet and vLLM will ignore it.

          reasoning: **gpt-5 and o-series models only**

              Configuration options for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning).

          request_id: The request_id related to this request. If the caller does not set it, a
              random_uuid will be generated. This id is used through out the inference process
              and return in response.

          text: Configuration options for a text response from the model.

              Can be plain text or structured JSON data. Learn more:

              - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
              - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

          tool_choice: Constrains the tools available to the model to a pre-defined set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/responses",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "background": background,
                    "cache_salt": cache_salt,
                    "enable_response_messages": enable_response_messages,
                    "include": include,
                    "include_stop_str_in_output": include_stop_str_in_output,
                    "instructions": instructions,
                    "logit_bias": logit_bias,
                    "max_output_tokens": max_output_tokens,
                    "max_tool_calls": max_tool_calls,
                    "metadata": metadata,
                    "mm_processor_kwargs": mm_processor_kwargs,
                    "model": model,
                    "parallel_tool_calls": parallel_tool_calls,
                    "previous_input_messages": previous_input_messages,
                    "previous_response_id": previous_response_id,
                    "priority": priority,
                    "prompt": prompt,
                    "prompt_cache_key": prompt_cache_key,
                    "reasoning": reasoning,
                    "request_id": request_id,
                    "service_tier": service_tier,
                    "skip_special_tokens": skip_special_tokens,
                    "store": store,
                    "stream": stream,
                    "temperature": temperature,
                    "text": text,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "truncation": truncation,
                    "user": user,
                },
                response_create_params.ResponseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve(
        self,
        response_id: str,
        *,
        starting_after: Optional[int] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieve Responses

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return await self._get(
            path_template("/v1/responses/{response_id}", response_id=response_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "starting_after": starting_after,
                        "stream": stream,
                    },
                    response_retrieve_params.ResponseRetrieveParams,
                ),
            ),
            cast_to=object,
        )

    async def cancel(
        self,
        response_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Cancel Responses

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return await self._post(
            path_template("/v1/responses/{response_id}/cancel", response_id=response_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ResponsesResourceWithRawResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_raw_response_wrapper(
            responses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            responses.retrieve,
        )
        self.cancel = to_raw_response_wrapper(
            responses.cancel,
        )


class AsyncResponsesResourceWithRawResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_raw_response_wrapper(
            responses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            responses.retrieve,
        )
        self.cancel = async_to_raw_response_wrapper(
            responses.cancel,
        )


class ResponsesResourceWithStreamingResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_streamed_response_wrapper(
            responses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            responses.retrieve,
        )
        self.cancel = to_streamed_response_wrapper(
            responses.cancel,
        )


class AsyncResponsesResourceWithStreamingResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_streamed_response_wrapper(
            responses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            responses.retrieve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            responses.cancel,
        )
