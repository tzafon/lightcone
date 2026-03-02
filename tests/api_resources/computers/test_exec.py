# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lightcone import Lightcone, AsyncLightcone
from tests.utils import assert_matches_type
from lightcone.types.computers import (
    ExecExecuteResponse,
    ExecExecuteSyncResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExec:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute(self, client: Lightcone) -> None:
        exec_stream = client.computers.exec.execute(
            id="id",
        )
        for item in exec_stream:
            assert_matches_type(ExecExecuteResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_with_all_params(self, client: Lightcone) -> None:
        exec_stream = client.computers.exec.execute(
            id="id",
            command="command",
            cwd="cwd",
            env={"foo": "string"},
            timeout_seconds=0,
        )
        for item in exec_stream:
            assert_matches_type(ExecExecuteResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute(self, client: Lightcone) -> None:
        response = client.computers.exec.with_raw_response.execute(
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        for item in stream:
            assert_matches_type(ExecExecuteResponse, item, path=["line"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute(self, client: Lightcone) -> None:
        with client.computers.exec.with_streaming_response.execute(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            for item in stream:
                assert_matches_type(ExecExecuteResponse, item, path=["item"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_execute(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.exec.with_raw_response.execute(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_sync(self, client: Lightcone) -> None:
        exec = client.computers.exec.execute_sync(
            id="id",
        )
        assert_matches_type(ExecExecuteSyncResponse, exec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_sync_with_all_params(self, client: Lightcone) -> None:
        exec = client.computers.exec.execute_sync(
            id="id",
            command="command",
            cwd="cwd",
            env={"foo": "string"},
            timeout_seconds=0,
        )
        assert_matches_type(ExecExecuteSyncResponse, exec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute_sync(self, client: Lightcone) -> None:
        response = client.computers.exec.with_raw_response.execute_sync(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exec = response.parse()
        assert_matches_type(ExecExecuteSyncResponse, exec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute_sync(self, client: Lightcone) -> None:
        with client.computers.exec.with_streaming_response.execute_sync(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exec = response.parse()
            assert_matches_type(ExecExecuteSyncResponse, exec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_execute_sync(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.exec.with_raw_response.execute_sync(
                id="",
            )


class TestAsyncExec:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute(self, async_client: AsyncLightcone) -> None:
        exec_stream = await async_client.computers.exec.execute(
            id="id",
        )
        async for item in exec_stream:
            assert_matches_type(ExecExecuteResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncLightcone) -> None:
        exec_stream = await async_client.computers.exec.execute(
            id="id",
            command="command",
            cwd="cwd",
            env={"foo": "string"},
            timeout_seconds=0,
        )
        async for item in exec_stream:
            assert_matches_type(ExecExecuteResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.exec.with_raw_response.execute(
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        async for item in stream:
            assert_matches_type(ExecExecuteResponse, item, path=["line"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.exec.with_streaming_response.execute(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            async for item in stream:
                assert_matches_type(ExecExecuteResponse, item, path=["item"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_execute(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.exec.with_raw_response.execute(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_sync(self, async_client: AsyncLightcone) -> None:
        exec = await async_client.computers.exec.execute_sync(
            id="id",
        )
        assert_matches_type(ExecExecuteSyncResponse, exec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_sync_with_all_params(self, async_client: AsyncLightcone) -> None:
        exec = await async_client.computers.exec.execute_sync(
            id="id",
            command="command",
            cwd="cwd",
            env={"foo": "string"},
            timeout_seconds=0,
        )
        assert_matches_type(ExecExecuteSyncResponse, exec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute_sync(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.exec.with_raw_response.execute_sync(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exec = await response.parse()
        assert_matches_type(ExecExecuteSyncResponse, exec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute_sync(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.exec.with_streaming_response.execute_sync(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exec = await response.parse()
            assert_matches_type(ExecExecuteSyncResponse, exec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_execute_sync(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.exec.with_raw_response.execute_sync(
                id="",
            )
