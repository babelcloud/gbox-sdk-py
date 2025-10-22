# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gbox_sdk import GboxClient, AsyncGboxClient
from tests.utils import assert_matches_type
from gbox_sdk.types.v1 import ModelCallResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_call(self, client: GboxClient) -> None:
        model = client.v1.models.call(
            action={
                "type": "click",
                "target": "the VSCode app icon on the bottom dock",
            },
            screenshot="https://gru-activate2-public-assets.s3.us-west-2.amazonaws.com/jessica/screenshot-1759332945616-pu0ovj.png",
        )
        assert_matches_type(ModelCallResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_call_with_all_params(self, client: GboxClient) -> None:
        model = client.v1.models.call(
            action={
                "type": "click",
                "target": "the VSCode app icon on the bottom dock",
            },
            screenshot="https://gru-activate2-public-assets.s3.us-west-2.amazonaws.com/jessica/screenshot-1759332945616-pu0ovj.png",
            model="gbox-handy-1",
        )
        assert_matches_type(ModelCallResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_call(self, client: GboxClient) -> None:
        response = client.v1.models.with_raw_response.call(
            action={
                "type": "click",
                "target": "the VSCode app icon on the bottom dock",
            },
            screenshot="https://gru-activate2-public-assets.s3.us-west-2.amazonaws.com/jessica/screenshot-1759332945616-pu0ovj.png",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelCallResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_call(self, client: GboxClient) -> None:
        with client.v1.models.with_streaming_response.call(
            action={
                "type": "click",
                "target": "the VSCode app icon on the bottom dock",
            },
            screenshot="https://gru-activate2-public-assets.s3.us-west-2.amazonaws.com/jessica/screenshot-1759332945616-pu0ovj.png",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelCallResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_call(self, async_client: AsyncGboxClient) -> None:
        model = await async_client.v1.models.call(
            action={
                "type": "click",
                "target": "the VSCode app icon on the bottom dock",
            },
            screenshot="https://gru-activate2-public-assets.s3.us-west-2.amazonaws.com/jessica/screenshot-1759332945616-pu0ovj.png",
        )
        assert_matches_type(ModelCallResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_call_with_all_params(self, async_client: AsyncGboxClient) -> None:
        model = await async_client.v1.models.call(
            action={
                "type": "click",
                "target": "the VSCode app icon on the bottom dock",
            },
            screenshot="https://gru-activate2-public-assets.s3.us-west-2.amazonaws.com/jessica/screenshot-1759332945616-pu0ovj.png",
            model="gbox-handy-1",
        )
        assert_matches_type(ModelCallResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_call(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.models.with_raw_response.call(
            action={
                "type": "click",
                "target": "the VSCode app icon on the bottom dock",
            },
            screenshot="https://gru-activate2-public-assets.s3.us-west-2.amazonaws.com/jessica/screenshot-1759332945616-pu0ovj.png",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelCallResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_call(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.models.with_streaming_response.call(
            action={
                "type": "click",
                "target": "the VSCode app icon on the bottom dock",
            },
            screenshot="https://gru-activate2-public-assets.s3.us-west-2.amazonaws.com/jessica/screenshot-1759332945616-pu0ovj.png",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelCallResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True
