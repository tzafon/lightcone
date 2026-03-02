# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tzafon import Lightcone, AsyncLightcone
from tests.utils import assert_matches_type
from tzafon.types.agent import (
    TaskPauseResponse,
    TaskStartResponse,
    TaskResumeResponse,
    TaskInjectMessageResponse,
    TaskRetrieveStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_inject_message(self, client: Lightcone) -> None:
        task = client.agent.tasks.inject_message(
            id="id",
        )
        assert_matches_type(TaskInjectMessageResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_inject_message_with_all_params(self, client: Lightcone) -> None:
        task = client.agent.tasks.inject_message(
            id="id",
            message="message",
        )
        assert_matches_type(TaskInjectMessageResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_inject_message(self, client: Lightcone) -> None:
        response = client.agent.tasks.with_raw_response.inject_message(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskInjectMessageResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_inject_message(self, client: Lightcone) -> None:
        with client.agent.tasks.with_streaming_response.inject_message(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskInjectMessageResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_inject_message(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.tasks.with_raw_response.inject_message(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pause(self, client: Lightcone) -> None:
        task = client.agent.tasks.pause(
            "id",
        )
        assert_matches_type(TaskPauseResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pause(self, client: Lightcone) -> None:
        response = client.agent.tasks.with_raw_response.pause(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskPauseResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pause(self, client: Lightcone) -> None:
        with client.agent.tasks.with_streaming_response.pause(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskPauseResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_pause(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.tasks.with_raw_response.pause(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resume(self, client: Lightcone) -> None:
        task = client.agent.tasks.resume(
            "id",
        )
        assert_matches_type(TaskResumeResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_resume(self, client: Lightcone) -> None:
        response = client.agent.tasks.with_raw_response.resume(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskResumeResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_resume(self, client: Lightcone) -> None:
        with client.agent.tasks.with_streaming_response.resume(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskResumeResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_resume(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.tasks.with_raw_response.resume(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: Lightcone) -> None:
        task = client.agent.tasks.retrieve_status(
            "id",
        )
        assert_matches_type(TaskRetrieveStatusResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: Lightcone) -> None:
        response = client.agent.tasks.with_raw_response.retrieve_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskRetrieveStatusResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: Lightcone) -> None:
        with client.agent.tasks.with_streaming_response.retrieve_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskRetrieveStatusResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.tasks.with_raw_response.retrieve_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: Lightcone) -> None:
        task = client.agent.tasks.start()
        assert_matches_type(TaskStartResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_with_all_params(self, client: Lightcone) -> None:
        task = client.agent.tasks.start(
            agent_type="agent_type",
            environment_id="environment_id",
            instruction="instruction",
            kind="desktop",
            max_steps=0,
            model="model",
            persistent=True,
            screenshot_mode="url",
            temperature=0,
            viewport_height=0,
            viewport_width=0,
        )
        assert_matches_type(TaskStartResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Lightcone) -> None:
        response = client.agent.tasks.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskStartResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Lightcone) -> None:
        with client.agent.tasks.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskStartResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_stream(self, client: Lightcone) -> None:
        task_stream = client.agent.tasks.start_stream()
        task_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_stream_with_all_params(self, client: Lightcone) -> None:
        task_stream = client.agent.tasks.start_stream(
            agent_type="agent_type",
            environment_id="environment_id",
            instruction="instruction",
            kind="desktop",
            max_steps=0,
            model="model",
            persistent=True,
            screenshot_mode="url",
            temperature=0,
            viewport_height=0,
            viewport_width=0,
        )
        task_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start_stream(self, client: Lightcone) -> None:
        response = client.agent.tasks.with_raw_response.start_stream()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start_stream(self, client: Lightcone) -> None:
        with client.agent.tasks.with_streaming_response.start_stream() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_inject_message(self, async_client: AsyncLightcone) -> None:
        task = await async_client.agent.tasks.inject_message(
            id="id",
        )
        assert_matches_type(TaskInjectMessageResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_inject_message_with_all_params(self, async_client: AsyncLightcone) -> None:
        task = await async_client.agent.tasks.inject_message(
            id="id",
            message="message",
        )
        assert_matches_type(TaskInjectMessageResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_inject_message(self, async_client: AsyncLightcone) -> None:
        response = await async_client.agent.tasks.with_raw_response.inject_message(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskInjectMessageResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_inject_message(self, async_client: AsyncLightcone) -> None:
        async with async_client.agent.tasks.with_streaming_response.inject_message(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskInjectMessageResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_inject_message(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.tasks.with_raw_response.inject_message(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pause(self, async_client: AsyncLightcone) -> None:
        task = await async_client.agent.tasks.pause(
            "id",
        )
        assert_matches_type(TaskPauseResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncLightcone) -> None:
        response = await async_client.agent.tasks.with_raw_response.pause(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskPauseResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncLightcone) -> None:
        async with async_client.agent.tasks.with_streaming_response.pause(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskPauseResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_pause(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.tasks.with_raw_response.pause(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resume(self, async_client: AsyncLightcone) -> None:
        task = await async_client.agent.tasks.resume(
            "id",
        )
        assert_matches_type(TaskResumeResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_resume(self, async_client: AsyncLightcone) -> None:
        response = await async_client.agent.tasks.with_raw_response.resume(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskResumeResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_resume(self, async_client: AsyncLightcone) -> None:
        async with async_client.agent.tasks.with_streaming_response.resume(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskResumeResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_resume(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.tasks.with_raw_response.resume(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncLightcone) -> None:
        task = await async_client.agent.tasks.retrieve_status(
            "id",
        )
        assert_matches_type(TaskRetrieveStatusResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncLightcone) -> None:
        response = await async_client.agent.tasks.with_raw_response.retrieve_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskRetrieveStatusResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncLightcone) -> None:
        async with async_client.agent.tasks.with_streaming_response.retrieve_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskRetrieveStatusResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.tasks.with_raw_response.retrieve_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncLightcone) -> None:
        task = await async_client.agent.tasks.start()
        assert_matches_type(TaskStartResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncLightcone) -> None:
        task = await async_client.agent.tasks.start(
            agent_type="agent_type",
            environment_id="environment_id",
            instruction="instruction",
            kind="desktop",
            max_steps=0,
            model="model",
            persistent=True,
            screenshot_mode="url",
            temperature=0,
            viewport_height=0,
            viewport_width=0,
        )
        assert_matches_type(TaskStartResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncLightcone) -> None:
        response = await async_client.agent.tasks.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskStartResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncLightcone) -> None:
        async with async_client.agent.tasks.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskStartResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_stream(self, async_client: AsyncLightcone) -> None:
        task_stream = await async_client.agent.tasks.start_stream()
        await task_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_stream_with_all_params(self, async_client: AsyncLightcone) -> None:
        task_stream = await async_client.agent.tasks.start_stream(
            agent_type="agent_type",
            environment_id="environment_id",
            instruction="instruction",
            kind="desktop",
            max_steps=0,
            model="model",
            persistent=True,
            screenshot_mode="url",
            temperature=0,
            viewport_height=0,
            viewport_width=0,
        )
        await task_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start_stream(self, async_client: AsyncLightcone) -> None:
        response = await async_client.agent.tasks.with_raw_response.start_stream()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start_stream(self, async_client: AsyncLightcone) -> None:
        async with async_client.agent.tasks.with_streaming_response.start_stream() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
