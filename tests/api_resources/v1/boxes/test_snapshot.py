# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gbox_sdk import GboxClient, AsyncGboxClient
from tests.utils import assert_matches_type
from gbox_sdk.types.v1.boxes import (
    SnapshotGetResponse,
    SnapshotListResponse,
    SnapshotCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnapshot:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: GboxClient) -> None:
        snapshot = client.v1.boxes.snapshot.create(
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            name="my-snapshot-1",
        )
        assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: GboxClient) -> None:
        response = client.v1.boxes.snapshot.with_raw_response.create(
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            name="my-snapshot-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: GboxClient) -> None:
        with client.v1.boxes.snapshot.with_streaming_response.create(
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            name="my-snapshot-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.snapshot.with_raw_response.create(
                box_id="",
                name="my-snapshot-1",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: GboxClient) -> None:
        snapshot = client.v1.boxes.snapshot.list()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: GboxClient) -> None:
        snapshot = client.v1.boxes.snapshot.list(
            page=1,
            page_size=10,
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: GboxClient) -> None:
        response = client.v1.boxes.snapshot.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: GboxClient) -> None:
        with client.v1.boxes.snapshot.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: GboxClient) -> None:
        snapshot = client.v1.boxes.snapshot.get(
            "snapshotName",
        )
        assert_matches_type(SnapshotGetResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: GboxClient) -> None:
        response = client.v1.boxes.snapshot.with_raw_response.get(
            "snapshotName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotGetResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: GboxClient) -> None:
        with client.v1.boxes.snapshot.with_streaming_response.get(
            "snapshotName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotGetResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_name` but received ''"):
            client.v1.boxes.snapshot.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: GboxClient) -> None:
        snapshot = client.v1.boxes.snapshot.remove(
            "snapshotName",
        )
        assert snapshot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: GboxClient) -> None:
        response = client.v1.boxes.snapshot.with_raw_response.remove(
            "snapshotName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert snapshot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: GboxClient) -> None:
        with client.v1.boxes.snapshot.with_streaming_response.remove(
            "snapshotName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert snapshot is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_name` but received ''"):
            client.v1.boxes.snapshot.with_raw_response.remove(
                "",
            )


class TestAsyncSnapshot:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGboxClient) -> None:
        snapshot = await async_client.v1.boxes.snapshot.create(
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            name="my-snapshot-1",
        )
        assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.snapshot.with_raw_response.create(
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            name="my-snapshot-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.snapshot.with_streaming_response.create(
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            name="my-snapshot-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotCreateResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.snapshot.with_raw_response.create(
                box_id="",
                name="my-snapshot-1",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGboxClient) -> None:
        snapshot = await async_client.v1.boxes.snapshot.list()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGboxClient) -> None:
        snapshot = await async_client.v1.boxes.snapshot.list(
            page=1,
            page_size=10,
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.snapshot.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.snapshot.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncGboxClient) -> None:
        snapshot = await async_client.v1.boxes.snapshot.get(
            "snapshotName",
        )
        assert_matches_type(SnapshotGetResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.snapshot.with_raw_response.get(
            "snapshotName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotGetResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.snapshot.with_streaming_response.get(
            "snapshotName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotGetResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_name` but received ''"):
            await async_client.v1.boxes.snapshot.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncGboxClient) -> None:
        snapshot = await async_client.v1.boxes.snapshot.remove(
            "snapshotName",
        )
        assert snapshot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.snapshot.with_raw_response.remove(
            "snapshotName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert snapshot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.snapshot.with_streaming_response.remove(
            "snapshotName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert snapshot is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_name` but received ''"):
            await async_client.v1.boxes.snapshot.with_raw_response.remove(
                "",
            )
