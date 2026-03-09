# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tzafon import Lightcone, AsyncLightcone
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_completion(self, client: Lightcone) -> None:
        chat = client.chat.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "developer",
                }
            ],
        )
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_completion_with_all_params(self, client: Lightcone) -> None:
        chat = client.chat.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "developer",
                    "name": "name",
                }
            ],
            add_generation_prompt=True,
            add_special_tokens=True,
            allowed_token_ids=[0],
            bad_words=["string"],
            cache_salt="cache_salt",
            chat_template="chat_template",
            chat_template_kwargs={"foo": "bar"},
            continue_final_message=True,
            documents=[{"foo": "string"}],
            echo=True,
            frequency_penalty=0,
            ignore_eos=True,
            include_reasoning=True,
            include_stop_str_in_output=True,
            kv_transfer_params={"foo": "bar"},
            length_penalty=0,
            logit_bias={"foo": 0},
            logits_processors=["string"],
            logprobs=True,
            max_completion_tokens=0,
            max_tokens=0,
            min_p=0,
            min_tokens=0,
            mm_processor_kwargs={"foo": "bar"},
            model="model",
            n=0,
            parallel_tool_calls=True,
            presence_penalty=0,
            priority=0,
            prompt_logprobs=0,
            reasoning_effort="low",
            repetition_penalty=0,
            request_id="request_id",
            response_format={
                "type": "text",
                "json_schema": {
                    "name": "name",
                    "description": "description",
                    "schema": {"foo": "bar"},
                    "strict": True,
                },
            },
            return_token_ids=True,
            return_tokens_as_token_ids=True,
            seed=-9007199254740991,
            skip_special_tokens=True,
            spaces_between_special_tokens=True,
            stop="string",
            stop_token_ids=[0],
            stream=True,
            stream_options={
                "continuous_usage_stats": True,
                "include_usage": True,
            },
            structured_outputs={
                "_backend": "_backend",
                "_backend_was_auto": True,
                "choice": ["string"],
                "disable_additional_properties": True,
                "disable_any_whitespace": True,
                "disable_fallback": True,
                "grammar": "grammar",
                "json": "string",
                "json_object": True,
                "regex": "regex",
                "structural_tag": "structural_tag",
                "whitespace_pattern": "whitespace_pattern",
            },
            temperature=0,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                    },
                    "type": "function",
                }
            ],
            top_k=0,
            top_logprobs=0,
            top_p=0,
            truncate_prompt_tokens=-1,
            use_beam_search=True,
            user="user",
            vllm_xargs={"foo": "string"},
        )
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_completion(self, client: Lightcone) -> None:
        response = client.chat.with_raw_response.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "developer",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_completion(self, client: Lightcone) -> None:
        with client.chat.with_streaming_response.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "developer",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_completion(self, async_client: AsyncLightcone) -> None:
        chat = await async_client.chat.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "developer",
                }
            ],
        )
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_completion_with_all_params(self, async_client: AsyncLightcone) -> None:
        chat = await async_client.chat.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "developer",
                    "name": "name",
                }
            ],
            add_generation_prompt=True,
            add_special_tokens=True,
            allowed_token_ids=[0],
            bad_words=["string"],
            cache_salt="cache_salt",
            chat_template="chat_template",
            chat_template_kwargs={"foo": "bar"},
            continue_final_message=True,
            documents=[{"foo": "string"}],
            echo=True,
            frequency_penalty=0,
            ignore_eos=True,
            include_reasoning=True,
            include_stop_str_in_output=True,
            kv_transfer_params={"foo": "bar"},
            length_penalty=0,
            logit_bias={"foo": 0},
            logits_processors=["string"],
            logprobs=True,
            max_completion_tokens=0,
            max_tokens=0,
            min_p=0,
            min_tokens=0,
            mm_processor_kwargs={"foo": "bar"},
            model="model",
            n=0,
            parallel_tool_calls=True,
            presence_penalty=0,
            priority=0,
            prompt_logprobs=0,
            reasoning_effort="low",
            repetition_penalty=0,
            request_id="request_id",
            response_format={
                "type": "text",
                "json_schema": {
                    "name": "name",
                    "description": "description",
                    "schema": {"foo": "bar"},
                    "strict": True,
                },
            },
            return_token_ids=True,
            return_tokens_as_token_ids=True,
            seed=-9007199254740991,
            skip_special_tokens=True,
            spaces_between_special_tokens=True,
            stop="string",
            stop_token_ids=[0],
            stream=True,
            stream_options={
                "continuous_usage_stats": True,
                "include_usage": True,
            },
            structured_outputs={
                "_backend": "_backend",
                "_backend_was_auto": True,
                "choice": ["string"],
                "disable_additional_properties": True,
                "disable_any_whitespace": True,
                "disable_fallback": True,
                "grammar": "grammar",
                "json": "string",
                "json_object": True,
                "regex": "regex",
                "structural_tag": "structural_tag",
                "whitespace_pattern": "whitespace_pattern",
            },
            temperature=0,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                    },
                    "type": "function",
                }
            ],
            top_k=0,
            top_logprobs=0,
            top_p=0,
            truncate_prompt_tokens=-1,
            use_beam_search=True,
            user="user",
            vllm_xargs={"foo": "string"},
        )
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncLightcone) -> None:
        response = await async_client.chat.with_raw_response.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "developer",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncLightcone) -> None:
        async with async_client.chat.with_streaming_response.create_completion(
            messages=[
                {
                    "content": "string",
                    "role": "developer",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
