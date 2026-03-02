# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lightcone import Lightcone, AsyncLightcone
from tests.utils import assert_matches_type
from lightcone.types import (
    ActionResult,
    ComputerResponse,
    ComputerListResponse,
    ComputerGetStatusResponse,
    ComputerKeepAliveResponse,
    ComputerExecuteBatchResponse,
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
    def test_method_capture_screenshot(self, client: Lightcone) -> None:
        computer = client.computers.capture_screenshot(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_capture_screenshot_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.capture_screenshot(
            id="id",
            base64=True,
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_capture_screenshot(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.capture_screenshot(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_capture_screenshot(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.capture_screenshot(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_capture_screenshot(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.capture_screenshot(
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
    def test_method_execute_action(self, client: Lightcone) -> None:
        computer = client.computers.execute_action(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_action_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.execute_action(
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
    def test_raw_response_execute_action(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.execute_action(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute_action(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.execute_action(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_execute_action(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.execute_action(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_batch(self, client: Lightcone) -> None:
        computer = client.computers.execute_batch(
            id="id",
        )
        assert_matches_type(ComputerExecuteBatchResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_batch_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.execute_batch(
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
        assert_matches_type(ComputerExecuteBatchResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute_batch(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.execute_batch(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerExecuteBatchResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute_batch(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.execute_batch(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerExecuteBatchResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_execute_batch(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.execute_batch(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_debug(self, client: Lightcone) -> None:
        computer = client.computers.execute_debug(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_debug_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.execute_debug(
            id="id",
            command="command",
            max_output_length=0,
            tab_id="tab_id",
            timeout_seconds=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute_debug(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.execute_debug(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute_debug(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.execute_debug(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_execute_debug(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.execute_debug(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_html(self, client: Lightcone) -> None:
        computer = client.computers.get_html(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_html_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.get_html(
            id="id",
            auto_detect_encoding=True,
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_html(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.get_html(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_html(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.get_html(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_html(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.get_html(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: Lightcone) -> None:
        computer = client.computers.get_status(
            "id",
        )
        assert_matches_type(ComputerGetStatusResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.get_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerGetStatusResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.get_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerGetStatusResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.get_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_keep_alive(self, client: Lightcone) -> None:
        computer = client.computers.keep_alive(
            "id",
        )
        assert_matches_type(ComputerKeepAliveResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_keep_alive(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.keep_alive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerKeepAliveResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_keep_alive(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.keep_alive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerKeepAliveResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_keep_alive(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.keep_alive(
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
    def test_method_press_hotkey(self, client: Lightcone) -> None:
        computer = client.computers.press_hotkey(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_press_hotkey_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.press_hotkey(
            id="id",
            keys=["string"],
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_press_hotkey(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.press_hotkey(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_press_hotkey(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.press_hotkey(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_press_hotkey(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.press_hotkey(
                id="",
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
    def test_method_set_viewport(self, client: Lightcone) -> None:
        computer = client.computers.set_viewport(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_viewport_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.set_viewport(
            id="id",
            height=0,
            scale_factor=0,
            tab_id="tab_id",
            width=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_viewport(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.set_viewport(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_viewport(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.set_viewport(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_viewport(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.set_viewport(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_events(self, client: Lightcone) -> None:
        computer = client.computers.stream_events(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_events(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.stream_events(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_events(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.stream_events(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stream_events(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.stream_events(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_screencast(self, client: Lightcone) -> None:
        computer = client.computers.stream_screencast(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_screencast(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.stream_screencast(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_screencast(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.stream_screencast(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stream_screencast(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.stream_screencast(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_terminate(self, client: Lightcone) -> None:
        computer = client.computers.terminate(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_terminate(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.terminate(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_terminate(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.terminate(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_terminate(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.terminate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_type_text(self, client: Lightcone) -> None:
        computer = client.computers.type_text(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_type_text_with_all_params(self, client: Lightcone) -> None:
        computer = client.computers.type_text(
            id="id",
            tab_id="tab_id",
            text="text",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_type_text(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.type_text(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_type_text(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.type_text(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_type_text(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.type_text(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_websocket_connection(self, client: Lightcone) -> None:
        computer = client.computers.websocket_connection(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_websocket_connection(self, client: Lightcone) -> None:
        response = client.computers.with_raw_response.websocket_connection(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_websocket_connection(self, client: Lightcone) -> None:
        with client.computers.with_streaming_response.websocket_connection(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_websocket_connection(self, client: Lightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.websocket_connection(
                "",
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
    async def test_method_capture_screenshot(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.capture_screenshot(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_capture_screenshot_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.capture_screenshot(
            id="id",
            base64=True,
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_capture_screenshot(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.capture_screenshot(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_capture_screenshot(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.capture_screenshot(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_capture_screenshot(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.capture_screenshot(
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
    async def test_method_execute_action(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.execute_action(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_action_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.execute_action(
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
    async def test_raw_response_execute_action(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.execute_action(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute_action(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.execute_action(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_execute_action(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.execute_action(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_batch(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.execute_batch(
            id="id",
        )
        assert_matches_type(ComputerExecuteBatchResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_batch_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.execute_batch(
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
        assert_matches_type(ComputerExecuteBatchResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute_batch(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.execute_batch(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerExecuteBatchResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute_batch(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.execute_batch(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerExecuteBatchResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_execute_batch(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.execute_batch(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_debug(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.execute_debug(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_debug_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.execute_debug(
            id="id",
            command="command",
            max_output_length=0,
            tab_id="tab_id",
            timeout_seconds=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute_debug(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.execute_debug(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute_debug(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.execute_debug(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_execute_debug(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.execute_debug(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_html(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.get_html(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_html_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.get_html(
            id="id",
            auto_detect_encoding=True,
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_html(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.get_html(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_html(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.get_html(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_html(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.get_html(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.get_status(
            "id",
        )
        assert_matches_type(ComputerGetStatusResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.get_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerGetStatusResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.get_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerGetStatusResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.get_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_keep_alive(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.keep_alive(
            "id",
        )
        assert_matches_type(ComputerKeepAliveResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_keep_alive(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.keep_alive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerKeepAliveResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_keep_alive(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.keep_alive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerKeepAliveResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_keep_alive(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.keep_alive(
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
    async def test_method_press_hotkey(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.press_hotkey(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_press_hotkey_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.press_hotkey(
            id="id",
            keys=["string"],
            tab_id="tab_id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_press_hotkey(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.press_hotkey(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_press_hotkey(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.press_hotkey(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_press_hotkey(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.press_hotkey(
                id="",
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
    async def test_method_set_viewport(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.set_viewport(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_viewport_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.set_viewport(
            id="id",
            height=0,
            scale_factor=0,
            tab_id="tab_id",
            width=0,
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_viewport(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.set_viewport(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_viewport(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.set_viewport(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_viewport(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.set_viewport(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_events(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.stream_events(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_events(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.stream_events(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_events(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.stream_events(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stream_events(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.stream_events(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_screencast(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.stream_screencast(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_screencast(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.stream_screencast(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_screencast(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.stream_screencast(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stream_screencast(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.stream_screencast(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_terminate(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.terminate(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_terminate(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.terminate(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_terminate(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.terminate(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_terminate(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.terminate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_type_text(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.type_text(
            id="id",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_type_text_with_all_params(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.type_text(
            id="id",
            tab_id="tab_id",
            text="text",
        )
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_type_text(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.type_text(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ActionResult, computer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_type_text(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.type_text(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ActionResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_type_text(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.type_text(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_websocket_connection(self, async_client: AsyncLightcone) -> None:
        computer = await async_client.computers.websocket_connection(
            "id",
        )
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_websocket_connection(self, async_client: AsyncLightcone) -> None:
        response = await async_client.computers.with_raw_response.websocket_connection(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_websocket_connection(self, async_client: AsyncLightcone) -> None:
        async with async_client.computers.with_streaming_response.websocket_connection(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_websocket_connection(self, async_client: AsyncLightcone) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.websocket_connection(
                "",
            )
