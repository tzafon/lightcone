# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lightcone import Lightcone, AsyncLightcone
from tests.utils import assert_matches_type
from lightcone.types import ActionResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTabs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Lightcone) -> None:
        tab = client.computers.tabs.create(
            id="id",
        )
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Lightcone) -> None:
        tab = client.computers.tabs.create(
            id="id",
            url="url",
        )
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Lightcone) -> None:
        response = client.computers.tabs.with_raw_response.create(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tab = response.parse()
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Lightcone) -> None:
        with client.computers.tabs.with_streaming_response.create(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tab = response.parse()
            assert_matches_type(ActionResult, tab, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.tabs.with_raw_response.create(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Lightcone) -> None:
        tab = client.computers.tabs.list(
            "id",
        )
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Lightcone) -> None:
        response = client.computers.tabs.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tab = response.parse()
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Lightcone) -> None:
        with client.computers.tabs.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tab = response.parse()
            assert_matches_type(ActionResult, tab, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.tabs.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_close(self, client: Lightcone) -> None:
        tab = client.computers.tabs.close(
            tab_id="tab_id",
            id="id",
        )
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_close(self, client: Lightcone) -> None:
        response = client.computers.tabs.with_raw_response.close(
            tab_id="tab_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tab = response.parse()
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_close(self, client: Lightcone) -> None:
        with client.computers.tabs.with_streaming_response.close(
            tab_id="tab_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tab = response.parse()
            assert_matches_type(ActionResult, tab, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_close(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.tabs.with_raw_response.close(
                tab_id="tab_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tab_id` but received ''"):
            client.computers.tabs.with_raw_response.close(
                tab_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_switch(self, client: Lightcone) -> None:
        tab = client.computers.tabs.switch(
            tab_id="tab_id",
            id="id",
        )
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_switch(self, client: Lightcone) -> None:
        response = client.computers.tabs.with_raw_response.switch(
            tab_id="tab_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tab = response.parse()
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_switch(self, client: Lightcone) -> None:
        with client.computers.tabs.with_streaming_response.switch(
            tab_id="tab_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tab = response.parse()
            assert_matches_type(ActionResult, tab, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_switch(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.tabs.with_raw_response.switch(
                tab_id="tab_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tab_id` but received ''"):
            client.computers.tabs.with_raw_response.switch(
                tab_id="",
                id="id",
            )


class TestAsyncTabs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLightcone) -> None:
        tab = await async_client.computers.tabs.create(
            id="id",
        )
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLightcone) -> None:
        tab = await async_client.computers.tabs.create(
            id="id",
            url="url",
        )
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.tabs.with_raw_response.create(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tab = await response.parse()
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.tabs.with_streaming_response.create(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tab = await response.parse()
            assert_matches_type(ActionResult, tab, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.tabs.with_raw_response.create(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLightcone) -> None:
        tab = await async_client.computers.tabs.list(
            "id",
        )
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.tabs.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tab = await response.parse()
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.tabs.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tab = await response.parse()
            assert_matches_type(ActionResult, tab, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.tabs.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_close(self, async_client: AsyncLightcone) -> None:
        tab = await async_client.computers.tabs.close(
            tab_id="tab_id",
            id="id",
        )
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_close(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.tabs.with_raw_response.close(
            tab_id="tab_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tab = await response.parse()
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_close(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.tabs.with_streaming_response.close(
            tab_id="tab_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tab = await response.parse()
            assert_matches_type(ActionResult, tab, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_close(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.tabs.with_raw_response.close(
                tab_id="tab_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tab_id` but received ''"):
            await async_client.computers.tabs.with_raw_response.close(
                tab_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_switch(self, async_client: AsyncLightcone) -> None:
        tab = await async_client.computers.tabs.switch(
            tab_id="tab_id",
            id="id",
        )
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_switch(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.tabs.with_raw_response.switch(
            tab_id="tab_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tab = await response.parse()
        assert_matches_type(ActionResult, tab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_switch(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.tabs.with_streaming_response.switch(
            tab_id="tab_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tab = await response.parse()
            assert_matches_type(ActionResult, tab, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_switch(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.tabs.with_raw_response.switch(
                tab_id="tab_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tab_id` but received ''"):
            await async_client.computers.tabs.with_raw_response.switch(
                tab_id="",
                id="id",
            )
