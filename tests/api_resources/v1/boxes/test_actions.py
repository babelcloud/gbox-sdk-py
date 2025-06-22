# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gbox_sdk import GboxClient, AsyncGboxClient
from tests.utils import assert_matches_type
from gbox_sdk.types.v1.boxes import (
    ActionResult,
    ActionScreenshotResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_click(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.click(
            box_id="boxId",
            x=100,
            y=100,
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_click_with_all_params(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.click(
            box_id="boxId",
            x=100,
            y=100,
            button="left",
            double=False,
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_click(self, client: GboxClient) -> None:
        response = client.v1.boxes.actions.with_raw_response.click(
            box_id="boxId",
            x=100,
            y=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_click(self, client: GboxClient) -> None:
        with client.v1.boxes.actions.with_streaming_response.click(
            box_id="boxId",
            x=100,
            y=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_click(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.actions.with_raw_response.click(
                box_id="",
                x=100,
                y=100,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_drag(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.drag(
            box_id="boxId",
            path=[
                {
                    "x": 100,
                    "y": 100,
                },
                {
                    "x": 200,
                    "y": 200,
                },
            ],
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_drag_with_all_params(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.drag(
            box_id="boxId",
            path=[
                {
                    "x": 100,
                    "y": 100,
                },
                {
                    "x": 200,
                    "y": 200,
                },
            ],
            duration="50ms",
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_drag(self, client: GboxClient) -> None:
        response = client.v1.boxes.actions.with_raw_response.drag(
            box_id="boxId",
            path=[
                {
                    "x": 100,
                    "y": 100,
                },
                {
                    "x": 200,
                    "y": 200,
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_drag(self, client: GboxClient) -> None:
        with client.v1.boxes.actions.with_streaming_response.drag(
            box_id="boxId",
            path=[
                {
                    "x": 100,
                    "y": 100,
                },
                {
                    "x": 200,
                    "y": 200,
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_drag(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.actions.with_raw_response.drag(
                box_id="",
                path=[
                    {
                        "x": 100,
                        "y": 100,
                    },
                    {
                        "x": 200,
                        "y": 200,
                    },
                ],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_move(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.move(
            box_id="boxId",
            x=200,
            y=300,
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_move_with_all_params(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.move(
            box_id="boxId",
            x=200,
            y=300,
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_move(self, client: GboxClient) -> None:
        response = client.v1.boxes.actions.with_raw_response.move(
            box_id="boxId",
            x=200,
            y=300,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_move(self, client: GboxClient) -> None:
        with client.v1.boxes.actions.with_streaming_response.move(
            box_id="boxId",
            x=200,
            y=300,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_move(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.actions.with_raw_response.move(
                box_id="",
                x=200,
                y=300,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_press_button(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.press_button(
            box_id="boxId",
            buttons=["power"],
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_press_button_with_all_params(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.press_button(
            box_id="boxId",
            buttons=["power"],
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_press_button(self, client: GboxClient) -> None:
        response = client.v1.boxes.actions.with_raw_response.press_button(
            box_id="boxId",
            buttons=["power"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_press_button(self, client: GboxClient) -> None:
        with client.v1.boxes.actions.with_streaming_response.press_button(
            box_id="boxId",
            buttons=["power"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_press_button(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.actions.with_raw_response.press_button(
                box_id="",
                buttons=["power"],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_press_key(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.press_key(
            box_id="boxId",
            keys=["enter"],
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_press_key_with_all_params(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.press_key(
            box_id="boxId",
            keys=["enter"],
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_press_key(self, client: GboxClient) -> None:
        response = client.v1.boxes.actions.with_raw_response.press_key(
            box_id="boxId",
            keys=["enter"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_press_key(self, client: GboxClient) -> None:
        with client.v1.boxes.actions.with_streaming_response.press_key(
            box_id="boxId",
            keys=["enter"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_press_key(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.actions.with_raw_response.press_key(
                box_id="",
                keys=["enter"],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_screen_rotation(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.screen_rotation(
            box_id="boxId",
            angle=90,
            direction="clockwise",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_screen_rotation(self, client: GboxClient) -> None:
        response = client.v1.boxes.actions.with_raw_response.screen_rotation(
            box_id="boxId",
            angle=90,
            direction="clockwise",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_screen_rotation(self, client: GboxClient) -> None:
        with client.v1.boxes.actions.with_streaming_response.screen_rotation(
            box_id="boxId",
            angle=90,
            direction="clockwise",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_screen_rotation(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.actions.with_raw_response.screen_rotation(
                box_id="",
                angle=90,
                direction="clockwise",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_screenshot(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.screenshot(
            box_id="boxId",
        )
        assert_matches_type(ActionScreenshotResponse, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_screenshot_with_all_params(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.screenshot(
            box_id="boxId",
            clip={
                "height": 600,
                "width": 800,
                "x": 100,
                "y": 50,
            },
            output_format="base64",
        )
        assert_matches_type(ActionScreenshotResponse, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_screenshot(self, client: GboxClient) -> None:
        response = client.v1.boxes.actions.with_raw_response.screenshot(
            box_id="boxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionScreenshotResponse, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_screenshot(self, client: GboxClient) -> None:
        with client.v1.boxes.actions.with_streaming_response.screenshot(
            box_id="boxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionScreenshotResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_screenshot(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.actions.with_raw_response.screenshot(
                box_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_scroll(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.scroll(
            box_id="boxId",
            scroll_x=0,
            scroll_y=100,
            x=100,
            y=100,
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_scroll_with_all_params(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.scroll(
            box_id="boxId",
            scroll_x=0,
            scroll_y=100,
            x=100,
            y=100,
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_scroll(self, client: GboxClient) -> None:
        response = client.v1.boxes.actions.with_raw_response.scroll(
            box_id="boxId",
            scroll_x=0,
            scroll_y=100,
            x=100,
            y=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_scroll(self, client: GboxClient) -> None:
        with client.v1.boxes.actions.with_streaming_response.scroll(
            box_id="boxId",
            scroll_x=0,
            scroll_y=100,
            x=100,
            y=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_scroll(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.actions.with_raw_response.scroll(
                box_id="",
                scroll_x=0,
                scroll_y=100,
                x=100,
                y=100,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_swipe_overload_1(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.swipe(
            box_id="boxId",
            direction="up",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_swipe_with_all_params_overload_1(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.swipe(
            box_id="boxId",
            direction="up",
            distance=300,
            duration="200ms",
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_swipe_overload_1(self, client: GboxClient) -> None:
        response = client.v1.boxes.actions.with_raw_response.swipe(
            box_id="boxId",
            direction="up",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_swipe_overload_1(self, client: GboxClient) -> None:
        with client.v1.boxes.actions.with_streaming_response.swipe(
            box_id="boxId",
            direction="up",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_swipe_overload_1(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.actions.with_raw_response.swipe(
                box_id="",
                direction="up",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_swipe_overload_2(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.swipe(
            box_id="boxId",
            end={
                "x": 400,
                "y": 300,
            },
            start={
                "x": 100,
                "y": 150,
            },
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_swipe_with_all_params_overload_2(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.swipe(
            box_id="boxId",
            end={
                "x": 400,
                "y": 300,
            },
            start={
                "x": 100,
                "y": 150,
            },
            duration="200ms",
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_swipe_overload_2(self, client: GboxClient) -> None:
        response = client.v1.boxes.actions.with_raw_response.swipe(
            box_id="boxId",
            end={
                "x": 400,
                "y": 300,
            },
            start={
                "x": 100,
                "y": 150,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_swipe_overload_2(self, client: GboxClient) -> None:
        with client.v1.boxes.actions.with_streaming_response.swipe(
            box_id="boxId",
            end={
                "x": 400,
                "y": 300,
            },
            start={
                "x": 100,
                "y": 150,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_swipe_overload_2(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.actions.with_raw_response.swipe(
                box_id="",
                end={
                    "x": 400,
                    "y": 300,
                },
                start={
                    "x": 100,
                    "y": 150,
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_touch(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.touch(
            box_id="boxId",
            points=[
                {
                    "start": {
                        "x": 100,
                        "y": 150,
                    }
                }
            ],
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_touch_with_all_params(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.touch(
            box_id="boxId",
            points=[
                {
                    "start": {
                        "x": 100,
                        "y": 150,
                    },
                    "actions": [
                        {
                            "x": 400,
                            "y": 300,
                            "duration": "200ms",
                        },
                        {"duration": "500ms"},
                    ],
                }
            ],
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_touch(self, client: GboxClient) -> None:
        response = client.v1.boxes.actions.with_raw_response.touch(
            box_id="boxId",
            points=[
                {
                    "start": {
                        "x": 100,
                        "y": 150,
                    }
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_touch(self, client: GboxClient) -> None:
        with client.v1.boxes.actions.with_streaming_response.touch(
            box_id="boxId",
            points=[
                {
                    "start": {
                        "x": 100,
                        "y": 150,
                    }
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_touch(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.actions.with_raw_response.touch(
                box_id="",
                points=[
                    {
                        "start": {
                            "x": 100,
                            "y": 150,
                        }
                    }
                ],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_type(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.type(
            box_id="boxId",
            text="Hello World",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_type_with_all_params(self, client: GboxClient) -> None:
        action = client.v1.boxes.actions.type(
            box_id="boxId",
            text="Hello World",
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_type(self, client: GboxClient) -> None:
        response = client.v1.boxes.actions.with_raw_response.type(
            box_id="boxId",
            text="Hello World",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_type(self, client: GboxClient) -> None:
        with client.v1.boxes.actions.with_streaming_response.type(
            box_id="boxId",
            text="Hello World",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_type(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.actions.with_raw_response.type(
                box_id="",
                text="Hello World",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_click(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.click(
            box_id="boxId",
            x=100,
            y=100,
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_click_with_all_params(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.click(
            box_id="boxId",
            x=100,
            y=100,
            button="left",
            double=False,
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_click(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.actions.with_raw_response.click(
            box_id="boxId",
            x=100,
            y=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_click(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.actions.with_streaming_response.click(
            box_id="boxId",
            x=100,
            y=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_click(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.actions.with_raw_response.click(
                box_id="",
                x=100,
                y=100,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_drag(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.drag(
            box_id="boxId",
            path=[
                {
                    "x": 100,
                    "y": 100,
                },
                {
                    "x": 200,
                    "y": 200,
                },
            ],
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_drag_with_all_params(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.drag(
            box_id="boxId",
            path=[
                {
                    "x": 100,
                    "y": 100,
                },
                {
                    "x": 200,
                    "y": 200,
                },
            ],
            duration="50ms",
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_drag(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.actions.with_raw_response.drag(
            box_id="boxId",
            path=[
                {
                    "x": 100,
                    "y": 100,
                },
                {
                    "x": 200,
                    "y": 200,
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_drag(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.actions.with_streaming_response.drag(
            box_id="boxId",
            path=[
                {
                    "x": 100,
                    "y": 100,
                },
                {
                    "x": 200,
                    "y": 200,
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_drag(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.actions.with_raw_response.drag(
                box_id="",
                path=[
                    {
                        "x": 100,
                        "y": 100,
                    },
                    {
                        "x": 200,
                        "y": 200,
                    },
                ],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_move(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.move(
            box_id="boxId",
            x=200,
            y=300,
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_move_with_all_params(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.move(
            box_id="boxId",
            x=200,
            y=300,
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_move(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.actions.with_raw_response.move(
            box_id="boxId",
            x=200,
            y=300,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.actions.with_streaming_response.move(
            box_id="boxId",
            x=200,
            y=300,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_move(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.actions.with_raw_response.move(
                box_id="",
                x=200,
                y=300,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_press_button(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.press_button(
            box_id="boxId",
            buttons=["power"],
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_press_button_with_all_params(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.press_button(
            box_id="boxId",
            buttons=["power"],
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_press_button(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.actions.with_raw_response.press_button(
            box_id="boxId",
            buttons=["power"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_press_button(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.actions.with_streaming_response.press_button(
            box_id="boxId",
            buttons=["power"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_press_button(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.actions.with_raw_response.press_button(
                box_id="",
                buttons=["power"],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_press_key(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.press_key(
            box_id="boxId",
            keys=["enter"],
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_press_key_with_all_params(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.press_key(
            box_id="boxId",
            keys=["enter"],
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_press_key(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.actions.with_raw_response.press_key(
            box_id="boxId",
            keys=["enter"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_press_key(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.actions.with_streaming_response.press_key(
            box_id="boxId",
            keys=["enter"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_press_key(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.actions.with_raw_response.press_key(
                box_id="",
                keys=["enter"],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_screen_rotation(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.screen_rotation(
            box_id="boxId",
            angle=90,
            direction="clockwise",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_screen_rotation(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.actions.with_raw_response.screen_rotation(
            box_id="boxId",
            angle=90,
            direction="clockwise",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_screen_rotation(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.actions.with_streaming_response.screen_rotation(
            box_id="boxId",
            angle=90,
            direction="clockwise",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_screen_rotation(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.actions.with_raw_response.screen_rotation(
                box_id="",
                angle=90,
                direction="clockwise",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_screenshot(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.screenshot(
            box_id="boxId",
        )
        assert_matches_type(ActionScreenshotResponse, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_screenshot_with_all_params(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.screenshot(
            box_id="boxId",
            clip={
                "height": 600,
                "width": 800,
                "x": 100,
                "y": 50,
            },
            output_format="base64",
        )
        assert_matches_type(ActionScreenshotResponse, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_screenshot(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.actions.with_raw_response.screenshot(
            box_id="boxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionScreenshotResponse, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_screenshot(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.actions.with_streaming_response.screenshot(
            box_id="boxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionScreenshotResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_screenshot(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.actions.with_raw_response.screenshot(
                box_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_scroll(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.scroll(
            box_id="boxId",
            scroll_x=0,
            scroll_y=100,
            x=100,
            y=100,
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_scroll_with_all_params(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.scroll(
            box_id="boxId",
            scroll_x=0,
            scroll_y=100,
            x=100,
            y=100,
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_scroll(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.actions.with_raw_response.scroll(
            box_id="boxId",
            scroll_x=0,
            scroll_y=100,
            x=100,
            y=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_scroll(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.actions.with_streaming_response.scroll(
            box_id="boxId",
            scroll_x=0,
            scroll_y=100,
            x=100,
            y=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_scroll(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.actions.with_raw_response.scroll(
                box_id="",
                scroll_x=0,
                scroll_y=100,
                x=100,
                y=100,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_swipe_overload_1(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.swipe(
            box_id="boxId",
            direction="up",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_swipe_with_all_params_overload_1(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.swipe(
            box_id="boxId",
            direction="up",
            distance=300,
            duration="200ms",
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_swipe_overload_1(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.actions.with_raw_response.swipe(
            box_id="boxId",
            direction="up",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_swipe_overload_1(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.actions.with_streaming_response.swipe(
            box_id="boxId",
            direction="up",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_swipe_overload_1(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.actions.with_raw_response.swipe(
                box_id="",
                direction="up",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_swipe_overload_2(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.swipe(
            box_id="boxId",
            end={
                "x": 400,
                "y": 300,
            },
            start={
                "x": 100,
                "y": 150,
            },
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_swipe_with_all_params_overload_2(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.swipe(
            box_id="boxId",
            end={
                "x": 400,
                "y": 300,
            },
            start={
                "x": 100,
                "y": 150,
            },
            duration="200ms",
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_swipe_overload_2(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.actions.with_raw_response.swipe(
            box_id="boxId",
            end={
                "x": 400,
                "y": 300,
            },
            start={
                "x": 100,
                "y": 150,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_swipe_overload_2(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.actions.with_streaming_response.swipe(
            box_id="boxId",
            end={
                "x": 400,
                "y": 300,
            },
            start={
                "x": 100,
                "y": 150,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_swipe_overload_2(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.actions.with_raw_response.swipe(
                box_id="",
                end={
                    "x": 400,
                    "y": 300,
                },
                start={
                    "x": 100,
                    "y": 150,
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_touch(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.touch(
            box_id="boxId",
            points=[
                {
                    "start": {
                        "x": 100,
                        "y": 150,
                    }
                }
            ],
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_touch_with_all_params(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.touch(
            box_id="boxId",
            points=[
                {
                    "start": {
                        "x": 100,
                        "y": 150,
                    },
                    "actions": [
                        {
                            "x": 400,
                            "y": 300,
                            "duration": "200ms",
                        },
                        {"duration": "500ms"},
                    ],
                }
            ],
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_touch(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.actions.with_raw_response.touch(
            box_id="boxId",
            points=[
                {
                    "start": {
                        "x": 100,
                        "y": 150,
                    }
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_touch(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.actions.with_streaming_response.touch(
            box_id="boxId",
            points=[
                {
                    "start": {
                        "x": 100,
                        "y": 150,
                    }
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_touch(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.actions.with_raw_response.touch(
                box_id="",
                points=[
                    {
                        "start": {
                            "x": 100,
                            "y": 150,
                        }
                    }
                ],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_type(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.type(
            box_id="boxId",
            text="Hello World",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_type_with_all_params(self, async_client: AsyncGboxClient) -> None:
        action = await async_client.v1.boxes.actions.type(
            box_id="boxId",
            text="Hello World",
            output_format="base64",
            screenshot_delay="500ms",
        )
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_type(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.actions.with_raw_response.type(
            box_id="boxId",
            text="Hello World",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionResult, action, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_type(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.actions.with_streaming_response.type(
            box_id="boxId",
            text="Hello World",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionResult, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_type(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.actions.with_raw_response.type(
                box_id="",
                text="Hello World",
            )
