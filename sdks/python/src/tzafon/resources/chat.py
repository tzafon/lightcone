# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import chat_create_completion_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tzafon/lightcone-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tzafon/lightcone-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def create_completion(
        self,
        *,
        messages: Iterable[chat_create_completion_params.Message],
        add_generation_prompt: bool | Omit = omit,
        add_special_tokens: bool | Omit = omit,
        allowed_token_ids: Optional[Iterable[int]] | Omit = omit,
        bad_words: SequenceNotStr[str] | Omit = omit,
        cache_salt: Optional[str] | Omit = omit,
        chat_template: Optional[str] | Omit = omit,
        chat_template_kwargs: Optional[Dict[str, object]] | Omit = omit,
        continue_final_message: bool | Omit = omit,
        documents: Optional[Iterable[Dict[str, str]]] | Omit = omit,
        echo: bool | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        ignore_eos: bool | Omit = omit,
        include_reasoning: bool | Omit = omit,
        include_stop_str_in_output: bool | Omit = omit,
        kv_transfer_params: Optional[Dict[str, object]] | Omit = omit,
        length_penalty: float | Omit = omit,
        logit_bias: Optional[Dict[str, float]] | Omit = omit,
        logits_processors: Optional[SequenceNotStr[chat_create_completion_params.LogitsProcessor]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        min_p: Optional[float] | Omit = omit,
        min_tokens: int | Omit = omit,
        mm_processor_kwargs: Optional[Dict[str, object]] | Omit = omit,
        model: Optional[str] | Omit = omit,
        n: Optional[int] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        priority: int | Omit = omit,
        prompt_logprobs: Optional[int] | Omit = omit,
        reasoning_effort: Optional[Literal["low", "medium", "high"]] | Omit = omit,
        repetition_penalty: Optional[float] | Omit = omit,
        request_id: str | Omit = omit,
        response_format: Optional[chat_create_completion_params.ResponseFormat] | Omit = omit,
        return_token_ids: Optional[bool] | Omit = omit,
        return_tokens_as_token_ids: Optional[bool] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        skip_special_tokens: bool | Omit = omit,
        spaces_between_special_tokens: bool | Omit = omit,
        stop: Union[str, SequenceNotStr[str], None] | Omit = omit,
        stop_token_ids: Optional[Iterable[int]] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        stream_options: Optional[chat_create_completion_params.StreamOptions] | Omit = omit,
        structured_outputs: Optional[chat_create_completion_params.StructuredOutputs] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[chat_create_completion_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[chat_create_completion_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncate_prompt_tokens: Optional[int] | Omit = omit,
        use_beam_search: bool | Omit = omit,
        user: Optional[str] | Omit = omit,
        vllm_xargs: Optional[Dict[str, Union[str, float, SequenceNotStr[Union[str, float]]]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create Chat Completion

        Args:
          add_generation_prompt: If true, the generation prompt will be added to the chat template. This is a
              parameter used by chat template in tokenizer config of the model.

          add_special_tokens: If true, special tokens (e.g. BOS) will be added to the prompt on top of what is
              added by the chat template. For most models, the chat template takes care of
              adding the special tokens so this should be set to false (as is the default).

          cache_salt: If specified, the prefix cache will be salted with the provided string to
              prevent an attacker to guess prompts in multi-user environments. The salt should
              be random, protected from access by 3rd parties, and long enough to be
              unpredictable (e.g., 43 characters base64-encoded, corresponding to 256 bit).

          chat_template: A Jinja template to use for this conversion. As of transformers v4.44, default
              chat template is no longer allowed, so you must provide a chat template if the
              tokenizer does not define one.

          chat_template_kwargs: Additional keyword args to pass to the template renderer. Will be accessible by
              the chat template.

          continue_final_message: If this is set, the chat will be formatted so that the final message in the chat
              is open-ended, without any EOS tokens. The model will continue this message
              rather than starting a new one. This allows you to "prefill" part of the model's
              response for it. Cannot be used at the same time as `add_generation_prompt`.

          documents: A list of dicts representing documents that will be accessible to the model if
              it is performing RAG (retrieval-augmented generation). If the template does not
              support RAG, this argument will have no effect. We recommend that each document
              should be a dict containing "title" and "text" keys.

          echo: If true, the new message will be prepended with the last message if they belong
              to the same role.

          kv_transfer_params: KVTransfer parameters used for disaggregated serving.

          logits_processors: A list of either qualified names of logits processors, or constructor objects,
              to apply when sampling. A constructor is a JSON object with a required
              'qualname' field specifying the qualified name of the processor class/factory,
              and optional 'args' and 'kwargs' fields containing positional and keyword
              arguments. For example: {'qualname': 'my_module.MyLogitsProcessor', 'args': [1,
              2], 'kwargs': {'param': 'value'}}.

          mm_processor_kwargs: Additional kwargs to pass to the HF processor.

          priority: The priority of the request (lower means earlier handling; default: 0). Any
              priority other than 0 will raise an error if the served model does not use
              priority scheduling.

          request_id: The request_id related to this request. If the caller does not set it, a
              random_uuid will be generated. This id is used through out the inference process
              and return in response.

          return_token_ids: If specified, the result will include token IDs alongside the generated text. In
              streaming mode, prompt_token_ids is included only in the first chunk, and
              token_ids contains the delta tokens for each chunk. This is useful for debugging
              or when you need to map generated text back to input tokens.

          return_tokens_as_token_ids: If specified with 'logprobs', tokens are represented as strings of the form
              'token_id:{token_id}' so that tokens that are not JSON-encodable can be
              identified.

          structured_outputs: Additional kwargs for structured outputs

          vllm_xargs: Additional request parameters with (list of) string or numeric values, used by
              custom extensions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "add_generation_prompt": add_generation_prompt,
                    "add_special_tokens": add_special_tokens,
                    "allowed_token_ids": allowed_token_ids,
                    "bad_words": bad_words,
                    "cache_salt": cache_salt,
                    "chat_template": chat_template,
                    "chat_template_kwargs": chat_template_kwargs,
                    "continue_final_message": continue_final_message,
                    "documents": documents,
                    "echo": echo,
                    "frequency_penalty": frequency_penalty,
                    "ignore_eos": ignore_eos,
                    "include_reasoning": include_reasoning,
                    "include_stop_str_in_output": include_stop_str_in_output,
                    "kv_transfer_params": kv_transfer_params,
                    "length_penalty": length_penalty,
                    "logit_bias": logit_bias,
                    "logits_processors": logits_processors,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "min_p": min_p,
                    "min_tokens": min_tokens,
                    "mm_processor_kwargs": mm_processor_kwargs,
                    "model": model,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "priority": priority,
                    "prompt_logprobs": prompt_logprobs,
                    "reasoning_effort": reasoning_effort,
                    "repetition_penalty": repetition_penalty,
                    "request_id": request_id,
                    "response_format": response_format,
                    "return_token_ids": return_token_ids,
                    "return_tokens_as_token_ids": return_tokens_as_token_ids,
                    "seed": seed,
                    "skip_special_tokens": skip_special_tokens,
                    "spaces_between_special_tokens": spaces_between_special_tokens,
                    "stop": stop,
                    "stop_token_ids": stop_token_ids,
                    "stream": stream,
                    "stream_options": stream_options,
                    "structured_outputs": structured_outputs,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "truncate_prompt_tokens": truncate_prompt_tokens,
                    "use_beam_search": use_beam_search,
                    "user": user,
                    "vllm_xargs": vllm_xargs,
                },
                chat_create_completion_params.ChatCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tzafon/lightcone-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tzafon/lightcone-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def create_completion(
        self,
        *,
        messages: Iterable[chat_create_completion_params.Message],
        add_generation_prompt: bool | Omit = omit,
        add_special_tokens: bool | Omit = omit,
        allowed_token_ids: Optional[Iterable[int]] | Omit = omit,
        bad_words: SequenceNotStr[str] | Omit = omit,
        cache_salt: Optional[str] | Omit = omit,
        chat_template: Optional[str] | Omit = omit,
        chat_template_kwargs: Optional[Dict[str, object]] | Omit = omit,
        continue_final_message: bool | Omit = omit,
        documents: Optional[Iterable[Dict[str, str]]] | Omit = omit,
        echo: bool | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        ignore_eos: bool | Omit = omit,
        include_reasoning: bool | Omit = omit,
        include_stop_str_in_output: bool | Omit = omit,
        kv_transfer_params: Optional[Dict[str, object]] | Omit = omit,
        length_penalty: float | Omit = omit,
        logit_bias: Optional[Dict[str, float]] | Omit = omit,
        logits_processors: Optional[SequenceNotStr[chat_create_completion_params.LogitsProcessor]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        min_p: Optional[float] | Omit = omit,
        min_tokens: int | Omit = omit,
        mm_processor_kwargs: Optional[Dict[str, object]] | Omit = omit,
        model: Optional[str] | Omit = omit,
        n: Optional[int] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        priority: int | Omit = omit,
        prompt_logprobs: Optional[int] | Omit = omit,
        reasoning_effort: Optional[Literal["low", "medium", "high"]] | Omit = omit,
        repetition_penalty: Optional[float] | Omit = omit,
        request_id: str | Omit = omit,
        response_format: Optional[chat_create_completion_params.ResponseFormat] | Omit = omit,
        return_token_ids: Optional[bool] | Omit = omit,
        return_tokens_as_token_ids: Optional[bool] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        skip_special_tokens: bool | Omit = omit,
        spaces_between_special_tokens: bool | Omit = omit,
        stop: Union[str, SequenceNotStr[str], None] | Omit = omit,
        stop_token_ids: Optional[Iterable[int]] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        stream_options: Optional[chat_create_completion_params.StreamOptions] | Omit = omit,
        structured_outputs: Optional[chat_create_completion_params.StructuredOutputs] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[chat_create_completion_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[chat_create_completion_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncate_prompt_tokens: Optional[int] | Omit = omit,
        use_beam_search: bool | Omit = omit,
        user: Optional[str] | Omit = omit,
        vllm_xargs: Optional[Dict[str, Union[str, float, SequenceNotStr[Union[str, float]]]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create Chat Completion

        Args:
          add_generation_prompt: If true, the generation prompt will be added to the chat template. This is a
              parameter used by chat template in tokenizer config of the model.

          add_special_tokens: If true, special tokens (e.g. BOS) will be added to the prompt on top of what is
              added by the chat template. For most models, the chat template takes care of
              adding the special tokens so this should be set to false (as is the default).

          cache_salt: If specified, the prefix cache will be salted with the provided string to
              prevent an attacker to guess prompts in multi-user environments. The salt should
              be random, protected from access by 3rd parties, and long enough to be
              unpredictable (e.g., 43 characters base64-encoded, corresponding to 256 bit).

          chat_template: A Jinja template to use for this conversion. As of transformers v4.44, default
              chat template is no longer allowed, so you must provide a chat template if the
              tokenizer does not define one.

          chat_template_kwargs: Additional keyword args to pass to the template renderer. Will be accessible by
              the chat template.

          continue_final_message: If this is set, the chat will be formatted so that the final message in the chat
              is open-ended, without any EOS tokens. The model will continue this message
              rather than starting a new one. This allows you to "prefill" part of the model's
              response for it. Cannot be used at the same time as `add_generation_prompt`.

          documents: A list of dicts representing documents that will be accessible to the model if
              it is performing RAG (retrieval-augmented generation). If the template does not
              support RAG, this argument will have no effect. We recommend that each document
              should be a dict containing "title" and "text" keys.

          echo: If true, the new message will be prepended with the last message if they belong
              to the same role.

          kv_transfer_params: KVTransfer parameters used for disaggregated serving.

          logits_processors: A list of either qualified names of logits processors, or constructor objects,
              to apply when sampling. A constructor is a JSON object with a required
              'qualname' field specifying the qualified name of the processor class/factory,
              and optional 'args' and 'kwargs' fields containing positional and keyword
              arguments. For example: {'qualname': 'my_module.MyLogitsProcessor', 'args': [1,
              2], 'kwargs': {'param': 'value'}}.

          mm_processor_kwargs: Additional kwargs to pass to the HF processor.

          priority: The priority of the request (lower means earlier handling; default: 0). Any
              priority other than 0 will raise an error if the served model does not use
              priority scheduling.

          request_id: The request_id related to this request. If the caller does not set it, a
              random_uuid will be generated. This id is used through out the inference process
              and return in response.

          return_token_ids: If specified, the result will include token IDs alongside the generated text. In
              streaming mode, prompt_token_ids is included only in the first chunk, and
              token_ids contains the delta tokens for each chunk. This is useful for debugging
              or when you need to map generated text back to input tokens.

          return_tokens_as_token_ids: If specified with 'logprobs', tokens are represented as strings of the form
              'token_id:{token_id}' so that tokens that are not JSON-encodable can be
              identified.

          structured_outputs: Additional kwargs for structured outputs

          vllm_xargs: Additional request parameters with (list of) string or numeric values, used by
              custom extensions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "add_generation_prompt": add_generation_prompt,
                    "add_special_tokens": add_special_tokens,
                    "allowed_token_ids": allowed_token_ids,
                    "bad_words": bad_words,
                    "cache_salt": cache_salt,
                    "chat_template": chat_template,
                    "chat_template_kwargs": chat_template_kwargs,
                    "continue_final_message": continue_final_message,
                    "documents": documents,
                    "echo": echo,
                    "frequency_penalty": frequency_penalty,
                    "ignore_eos": ignore_eos,
                    "include_reasoning": include_reasoning,
                    "include_stop_str_in_output": include_stop_str_in_output,
                    "kv_transfer_params": kv_transfer_params,
                    "length_penalty": length_penalty,
                    "logit_bias": logit_bias,
                    "logits_processors": logits_processors,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "min_p": min_p,
                    "min_tokens": min_tokens,
                    "mm_processor_kwargs": mm_processor_kwargs,
                    "model": model,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "priority": priority,
                    "prompt_logprobs": prompt_logprobs,
                    "reasoning_effort": reasoning_effort,
                    "repetition_penalty": repetition_penalty,
                    "request_id": request_id,
                    "response_format": response_format,
                    "return_token_ids": return_token_ids,
                    "return_tokens_as_token_ids": return_tokens_as_token_ids,
                    "seed": seed,
                    "skip_special_tokens": skip_special_tokens,
                    "spaces_between_special_tokens": spaces_between_special_tokens,
                    "stop": stop,
                    "stop_token_ids": stop_token_ids,
                    "stream": stream,
                    "stream_options": stream_options,
                    "structured_outputs": structured_outputs,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "truncate_prompt_tokens": truncate_prompt_tokens,
                    "use_beam_search": use_beam_search,
                    "user": user,
                    "vllm_xargs": vllm_xargs,
                },
                chat_create_completion_params.ChatCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create_completion = to_raw_response_wrapper(
            chat.create_completion,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create_completion = async_to_raw_response_wrapper(
            chat.create_completion,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create_completion = to_streamed_response_wrapper(
            chat.create_completion,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create_completion = async_to_streamed_response_wrapper(
            chat.create_completion,
        )
