# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tzafon import Lightcone, AsyncLightcone
from tests.utils import assert_matches_type
from tzafon.types import (
    ActionResult,
    ComputerResponse,
    ComputerListResponse,
    ComputerBatchResponse,
    ComputerKeepaliveResponse,
    ComputerRetrieveStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComputers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Lightcone) -> None:
        computer = client.computers.create()
        assert_matches_type(ComputerResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.create(
            auto_kill=True,
            context_id="context_id",
            display={
                "height": 0,
                "scale": 0,
                "width": 0,
            },
            environment_id="environment_id",
            inactivity_timeout_seconds=0,
            kind="kind",
            persistent=True,
            stealth={},
            timeout_seconds=0,
            use_advanced_proxy=True,
        )
        assert_matches_type(ComputerResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Lightcone) -> None:
        computer = client.computers.retrieve(
            "id",
        )
        assert_matches_type(ComputerResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Lightcone) -> None:
        computer = client.computers.list()
        assert_matches_type(ComputerListResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.list(
            type="live",
        )
        assert_matches_type(ComputerListResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerListResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerListResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Lightcone) -> None:
        computer = client.computers.delete(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch(self, client: Lightcone) -> None:
        computer = client.computers.batch(
            id="id",
        )
        assert_matches_type(ComputerBatchResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.batch(
            id="id",
            actions=[
                {
                    "auto_detect_encoding": True,
                    "base64": True,
                    "button": "button",
                    "debug": {
                        "command": "command",
                        "cwd": "cwd",
                        "env": {"foo": "string"},
                        "max_output_length": 0,
                        "request_id": "request_id",
                        "stream": True,
                        "timeout_seconds": 0,
                    },
                    "dx": 0,
                    "dy": 0,
                    "height": 0,
                    "include_context": True,
                    "key": "key",
                    "keys": ["string"],
                    "ms": 0,
                    "proxy_url": "proxy_url",
                    "request_id": "request_id",
                    "scale_factor": 0,
                    "tab_id": "tab_id",
                    "text": "text",
                    "type": "type",
                    "url": "url",
                    "width": 0,
                    "x": 0,
                    "x1": 0,
                    "x2": 0,
                    "y": 0,
                    "y1": 0,
                    "y2": 0,
                }
            ],
        )
        assert_matches_type(ComputerBatchResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.batch(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerBatchResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.batch(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerBatchResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_batch(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.batch(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_change_proxy(self, client: Lightcone) -> None:
        computer = client.computers.change_proxy(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_change_proxy_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.change_proxy(
            id="id",
            proxy_url="proxy_url",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_change_proxy(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.change_proxy(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_change_proxy(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.change_proxy(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_change_proxy(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.change_proxy(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_click(self, client: Lightcone) -> None:
        computer = client.computers.click(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_click_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.click(
            id="id",
            tab_id="tab_id",
            x=0,
            y=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_click(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.click(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_click(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.click(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_click(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.click(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_debug(self, client: Lightcone) -> None:
        computer = client.computers.debug(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_debug_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.debug(
            id="id",
            command="command",
            max_output_length=0,
            tab_id="tab_id",
            timeout_seconds=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_debug(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.debug(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_debug(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.debug(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_debug(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.debug(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_double_click(self, client: Lightcone) -> None:
        computer = client.computers.double_click(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_double_click_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.double_click(
            id="id",
            tab_id="tab_id",
            x=0,
            y=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_double_click(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.double_click(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_double_click(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.double_click(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_double_click(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.double_click(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_drag(self, client: Lightcone) -> None:
        computer = client.computers.drag(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_drag_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.drag(
            id="id",
            tab_id="tab_id",
            x1=0,
            x2=0,
            y1=0,
            y2=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_drag(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.drag(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_drag(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.drag(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_drag(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.drag(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute(self, client: Lightcone) -> None:
        computer = client.computers.execute(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.execute(
            id="id",
            action={
                "auto_detect_encoding": True,
                "base64": True,
                "button": "button",
                "debug": {
                    "command": "command",
                    "cwd": "cwd",
                    "env": {"foo": "string"},
                    "max_output_length": 0,
                    "request_id": "request_id",
                    "stream": True,
                    "timeout_seconds": 0,
                },
                "dx": 0,
                "dy": 0,
                "height": 0,
                "include_context": True,
                "key": "key",
                "keys": ["string"],
                "ms": 0,
                "proxy_url": "proxy_url",
                "request_id": "request_id",
                "scale_factor": 0,
                "tab_id": "tab_id",
                "text": "text",
                "type": "type",
                "url": "url",
                "width": 0,
                "x": 0,
                "x1": 0,
                "x2": 0,
                "y": 0,
                "y1": 0,
                "y2": 0,
            },
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.execute(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.execute(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_execute(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.execute(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_hotkey(self, client: Lightcone) -> None:
        computer = client.computers.hotkey(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_hotkey_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.hotkey(
            id="id",
            keys=["string"],
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_hotkey(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.hotkey(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_hotkey(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.hotkey(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_hotkey(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.hotkey(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_html(self, client: Lightcone) -> None:
        computer = client.computers.html(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_html_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.html(
            id="id",
            auto_detect_encoding=True,
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_html(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.html(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_html(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.html(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_html(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.html(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_keepalive(self, client: Lightcone) -> None:
        computer = client.computers.keepalive(
            "id",
        )
        assert_matches_type(ComputerKeepaliveResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_keepalive(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.keepalive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerKeepaliveResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_keepalive(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.keepalive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerKeepaliveResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_keepalive(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.keepalive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_key_down(self, client: Lightcone) -> None:
        computer = client.computers.key_down(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_key_down_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.key_down(
            id="id",
            key="shift",
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_key_down(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.key_down(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_key_down(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.key_down(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_key_down(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.key_down(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_key_up(self, client: Lightcone) -> None:
        computer = client.computers.key_up(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_key_up_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.key_up(
            id="id",
            key="shift",
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_key_up(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.key_up(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_key_up(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.key_up(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_key_up(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.key_up(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mouse_down(self, client: Lightcone) -> None:
        computer = client.computers.mouse_down(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mouse_down_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.mouse_down(
            id="id",
            tab_id="tab_id",
            x=0,
            y=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mouse_down(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.mouse_down(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mouse_down(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.mouse_down(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_mouse_down(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.mouse_down(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mouse_up(self, client: Lightcone) -> None:
        computer = client.computers.mouse_up(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mouse_up_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.mouse_up(
            id="id",
            tab_id="tab_id",
            x=0,
            y=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mouse_up(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.mouse_up(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mouse_up(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.mouse_up(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_mouse_up(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.mouse_up(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_navigate(self, client: Lightcone) -> None:
        computer = client.computers.navigate(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_navigate_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.navigate(
            id="id",
            tab_id="tab_id",
            url="url",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_navigate(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.navigate(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_navigate(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.navigate(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_navigate(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.navigate(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_events(self, client: Lightcone) -> None:
        computer = client.computers.retrieve_events(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_events(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.retrieve_events(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_events(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.retrieve_events(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_events(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.retrieve_events(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_screencast(self, client: Lightcone) -> None:
        computer = client.computers.retrieve_screencast(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_screencast(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.retrieve_screencast(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_screencast(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.retrieve_screencast(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_screencast(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.retrieve_screencast(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: Lightcone) -> None:
        computer = client.computers.retrieve_status(
            "id",
        )
        assert_matches_type(ComputerRetrieveStatusResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.retrieve_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerRetrieveStatusResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.retrieve_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerRetrieveStatusResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.retrieve_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_ws(self, client: Lightcone) -> None:
        computer = client.computers.retrieve_ws(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_ws(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.retrieve_ws(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_ws(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.retrieve_ws(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_ws(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.retrieve_ws(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_right_click(self, client: Lightcone) -> None:
        computer = client.computers.right_click(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_right_click_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.right_click(
            id="id",
            tab_id="tab_id",
            x=0,
            y=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_right_click(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.right_click(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_right_click(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.right_click(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_right_click(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.right_click(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_screenshot(self, client: Lightcone) -> None:
        computer = client.computers.screenshot(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_screenshot_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.screenshot(
            id="id",
            base64=True,
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_screenshot(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.screenshot(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_screenshot(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.screenshot(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_screenshot(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.screenshot(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_scroll(self, client: Lightcone) -> None:
        computer = client.computers.scroll(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_scroll_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.scroll(
            id="id",
            dx=0,
            dy=0,
            tab_id="tab_id",
            x=0,
            y=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_scroll(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.scroll(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_scroll(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.scroll(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_scroll(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.scroll(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_type(self, client: Lightcone) -> None:
        computer = client.computers.type(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_type_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.type(
            id="id",
            tab_id="tab_id",
            text="text",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_type(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.type(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_type(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.type(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_type(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.type(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_viewport(self, client: Lightcone) -> None:
        computer = client.computers.viewport(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_viewport_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.viewport(
            id="id",
            height=0,
            scale_factor=0,
            tab_id="tab_id",
            width=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_viewport(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.viewport(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_viewport(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.viewport(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_viewport(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.viewport(
                id="",
            )


class TestAsyncComputers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.create()
        assert_matches_type(ComputerResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.create(
            auto_kill=True,
            context_id="context_id",
            display={
                "height": 0,
                "scale": 0,
                "width": 0,
            },
            environment_id="environment_id",
            inactivity_timeout_seconds=0,
            kind="kind",
            persistent=True,
            stealth={},
            timeout_seconds=0,
            use_advanced_proxy=True,
        )
        assert_matches_type(ComputerResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.retrieve(
            "id",
        )
        assert_matches_type(ComputerResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.list()
        assert_matches_type(ComputerListResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.list(
            type="live",
        )
        assert_matches_type(ComputerListResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerListResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerListResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.delete(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.batch(
            id="id",
        )
        assert_matches_type(ComputerBatchResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.batch(
            id="id",
            actions=[
                {
                    "auto_detect_encoding": True,
                    "base64": True,
                    "button": "button",
                    "debug": {
                        "command": "command",
                        "cwd": "cwd",
                        "env": {"foo": "string"},
                        "max_output_length": 0,
                        "request_id": "request_id",
                        "stream": True,
                        "timeout_seconds": 0,
                    },
                    "dx": 0,
                    "dy": 0,
                    "height": 0,
                    "include_context": True,
                    "key": "key",
                    "keys": ["string"],
                    "ms": 0,
                    "proxy_url": "proxy_url",
                    "request_id": "request_id",
                    "scale_factor": 0,
                    "tab_id": "tab_id",
                    "text": "text",
                    "type": "type",
                    "url": "url",
                    "width": 0,
                    "x": 0,
                    "x1": 0,
                    "x2": 0,
                    "y": 0,
                    "y1": 0,
                    "y2": 0,
                }
            ],
        )
        assert_matches_type(ComputerBatchResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.batch(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerBatchResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.batch(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerBatchResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_batch(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.batch(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_change_proxy(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.change_proxy(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_change_proxy_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.change_proxy(
            id="id",
            proxy_url="proxy_url",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_change_proxy(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.change_proxy(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_change_proxy(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.change_proxy(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_change_proxy(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.change_proxy(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_click(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.click(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_click_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.click(
            id="id",
            tab_id="tab_id",
            x=0,
            y=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_click(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.click(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_click(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.click(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_click(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.click(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_debug(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.debug(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_debug_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.debug(
            id="id",
            command="command",
            max_output_length=0,
            tab_id="tab_id",
            timeout_seconds=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_debug(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.debug(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_debug(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.debug(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_debug(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.debug(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_double_click(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.double_click(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_double_click_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.double_click(
            id="id",
            tab_id="tab_id",
            x=0,
            y=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_double_click(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.double_click(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_double_click(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.double_click(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_double_click(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.double_click(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_drag(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.drag(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_drag_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.drag(
            id="id",
            tab_id="tab_id",
            x1=0,
            x2=0,
            y1=0,
            y2=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_drag(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.drag(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_drag(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.drag(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_drag(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.drag(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.execute(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.execute(
            id="id",
            action={
                "auto_detect_encoding": True,
                "base64": True,
                "button": "button",
                "debug": {
                    "command": "command",
                    "cwd": "cwd",
                    "env": {"foo": "string"},
                    "max_output_length": 0,
                    "request_id": "request_id",
                    "stream": True,
                    "timeout_seconds": 0,
                },
                "dx": 0,
                "dy": 0,
                "height": 0,
                "include_context": True,
                "key": "key",
                "keys": ["string"],
                "ms": 0,
                "proxy_url": "proxy_url",
                "request_id": "request_id",
                "scale_factor": 0,
                "tab_id": "tab_id",
                "text": "text",
                "type": "type",
                "url": "url",
                "width": 0,
                "x": 0,
                "x1": 0,
                "x2": 0,
                "y": 0,
                "y1": 0,
                "y2": 0,
            },
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.execute(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.execute(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_execute(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.execute(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_hotkey(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.hotkey(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_hotkey_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.hotkey(
            id="id",
            keys=["string"],
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_hotkey(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.hotkey(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_hotkey(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.hotkey(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_hotkey(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.hotkey(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_html(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.html(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_html_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.html(
            id="id",
            auto_detect_encoding=True,
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_html(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.html(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_html(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.html(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_html(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.html(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_keepalive(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.keepalive(
            "id",
        )
        assert_matches_type(ComputerKeepaliveResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_keepalive(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.keepalive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerKeepaliveResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_keepalive(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.keepalive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerKeepaliveResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_keepalive(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.keepalive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_key_down(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.key_down(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_key_down_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.key_down(
            id="id",
            key="shift",
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_key_down(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.key_down(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_key_down(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.key_down(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_key_down(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.key_down(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_key_up(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.key_up(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_key_up_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.key_up(
            id="id",
            key="shift",
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_key_up(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.key_up(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_key_up(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.key_up(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_key_up(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.key_up(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mouse_down(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.mouse_down(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mouse_down_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.mouse_down(
            id="id",
            tab_id="tab_id",
            x=0,
            y=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mouse_down(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.mouse_down(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mouse_down(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.mouse_down(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_mouse_down(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.mouse_down(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mouse_up(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.mouse_up(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mouse_up_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.mouse_up(
            id="id",
            tab_id="tab_id",
            x=0,
            y=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mouse_up(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.mouse_up(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mouse_up(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.mouse_up(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_mouse_up(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.mouse_up(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_navigate(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.navigate(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_navigate_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.navigate(
            id="id",
            tab_id="tab_id",
            url="url",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_navigate(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.navigate(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_navigate(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.navigate(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_navigate(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.navigate(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_events(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.retrieve_events(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_events(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.retrieve_events(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_events(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.retrieve_events(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_events(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.retrieve_events(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_screencast(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.retrieve_screencast(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_screencast(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.retrieve_screencast(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_screencast(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.retrieve_screencast(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_screencast(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.retrieve_screencast(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.retrieve_status(
            "id",
        )
        assert_matches_type(ComputerRetrieveStatusResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.retrieve_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerRetrieveStatusResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.retrieve_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerRetrieveStatusResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.retrieve_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_ws(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.retrieve_ws(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_ws(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.retrieve_ws(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_ws(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.retrieve_ws(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_ws(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.retrieve_ws(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_right_click(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.right_click(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_right_click_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.right_click(
            id="id",
            tab_id="tab_id",
            x=0,
            y=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_right_click(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.right_click(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_right_click(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.right_click(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_right_click(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.right_click(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_screenshot(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.screenshot(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_screenshot_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.screenshot(
            id="id",
            base64=True,
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_screenshot(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.screenshot(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_screenshot(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.screenshot(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_screenshot(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.screenshot(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_scroll(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.scroll(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_scroll_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.scroll(
            id="id",
            dx=0,
            dy=0,
            tab_id="tab_id",
            x=0,
            y=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_scroll(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.scroll(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_scroll(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.scroll(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_scroll(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.scroll(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_type(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.type(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_type_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.type(
            id="id",
            tab_id="tab_id",
            text="text",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_type(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.type(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_type(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.type(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_type(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.type(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_viewport(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.viewport(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_viewport_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.viewport(
            id="id",
            height=0,
            scale_factor=0,
            tab_id="tab_id",
            width=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_viewport(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.viewport(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_viewport(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.viewport(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_viewport(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.viewport(
                id="",
            )
