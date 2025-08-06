# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gbox_sdk import GboxClient, AsyncGboxClient
from tests.utils import assert_matches_type
from gbox_sdk.types.v1.boxes import (
    MediaListAlbumsResponse,
    MediaCreateAlbumResponse,
    MediaUpdateAlbumResponse,
    MediaDownloadMediaResponse,
    MediaGetAlbumDetailResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedia:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_album(self, client: GboxClient) -> None:
        media = client.v1.boxes.media.create_album(
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            media=[b"raw file contents"],
            name="Vacation Photos",
        )
        assert_matches_type(MediaCreateAlbumResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_album(self, client: GboxClient) -> None:
        response = client.v1.boxes.media.with_raw_response.create_album(
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            media=[b"raw file contents"],
            name="Vacation Photos",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaCreateAlbumResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_album(self, client: GboxClient) -> None:
        with client.v1.boxes.media.with_streaming_response.create_album(
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            media=[b"raw file contents"],
            name="Vacation Photos",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaCreateAlbumResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_album(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.media.with_raw_response.create_album(
                box_id="",
                media=[b"raw file contents"],
                name="Vacation Photos",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_album(self, client: GboxClient) -> None:
        media = client.v1.boxes.media.delete_album(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert media is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_album(self, client: GboxClient) -> None:
        response = client.v1.boxes.media.with_raw_response.delete_album(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert media is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_album(self, client: GboxClient) -> None:
        with client.v1.boxes.media.with_streaming_response.delete_album(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert media is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete_album(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.media.with_raw_response.delete_album(
                album_name="albumName",
                box_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_name` but received ''"):
            client.v1.boxes.media.with_raw_response.delete_album(
                album_name="",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_media(self, client: GboxClient) -> None:
        media = client.v1.boxes.media.delete_media(
            media_name="mediaName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            album_name="albumName",
        )
        assert media is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_media(self, client: GboxClient) -> None:
        response = client.v1.boxes.media.with_raw_response.delete_media(
            media_name="mediaName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            album_name="albumName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert media is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_media(self, client: GboxClient) -> None:
        with client.v1.boxes.media.with_streaming_response.delete_media(
            media_name="mediaName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            album_name="albumName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert media is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete_media(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.media.with_raw_response.delete_media(
                media_name="mediaName",
                box_id="",
                album_name="albumName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_name` but received ''"):
            client.v1.boxes.media.with_raw_response.delete_media(
                media_name="mediaName",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
                album_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_name` but received ''"):
            client.v1.boxes.media.with_raw_response.delete_media(
                media_name="",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
                album_name="albumName",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_download_media(self, client: GboxClient) -> None:
        media = client.v1.boxes.media.download_media(
            media_name="mediaName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            album_name="albumName",
        )
        assert_matches_type(MediaDownloadMediaResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_download_media(self, client: GboxClient) -> None:
        response = client.v1.boxes.media.with_raw_response.download_media(
            media_name="mediaName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            album_name="albumName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaDownloadMediaResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_download_media(self, client: GboxClient) -> None:
        with client.v1.boxes.media.with_streaming_response.download_media(
            media_name="mediaName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            album_name="albumName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaDownloadMediaResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_download_media(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.media.with_raw_response.download_media(
                media_name="mediaName",
                box_id="",
                album_name="albumName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_name` but received ''"):
            client.v1.boxes.media.with_raw_response.download_media(
                media_name="mediaName",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
                album_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_name` but received ''"):
            client.v1.boxes.media.with_raw_response.download_media(
                media_name="",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
                album_name="albumName",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_album_detail(self, client: GboxClient) -> None:
        media = client.v1.boxes.media.get_album_detail(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert_matches_type(MediaGetAlbumDetailResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_album_detail(self, client: GboxClient) -> None:
        response = client.v1.boxes.media.with_raw_response.get_album_detail(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaGetAlbumDetailResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_album_detail(self, client: GboxClient) -> None:
        with client.v1.boxes.media.with_streaming_response.get_album_detail(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaGetAlbumDetailResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_album_detail(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.media.with_raw_response.get_album_detail(
                album_name="albumName",
                box_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_name` but received ''"):
            client.v1.boxes.media.with_raw_response.get_album_detail(
                album_name="",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_albums(self, client: GboxClient) -> None:
        media = client.v1.boxes.media.list_albums(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert_matches_type(MediaListAlbumsResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_albums(self, client: GboxClient) -> None:
        response = client.v1.boxes.media.with_raw_response.list_albums(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaListAlbumsResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_albums(self, client: GboxClient) -> None:
        with client.v1.boxes.media.with_streaming_response.list_albums(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaListAlbumsResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_albums(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.media.with_raw_response.list_albums(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_album(self, client: GboxClient) -> None:
        media = client.v1.boxes.media.update_album(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            media=[b"raw file contents"],
        )
        assert_matches_type(MediaUpdateAlbumResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_album(self, client: GboxClient) -> None:
        response = client.v1.boxes.media.with_raw_response.update_album(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            media=[b"raw file contents"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaUpdateAlbumResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_album(self, client: GboxClient) -> None:
        with client.v1.boxes.media.with_streaming_response.update_album(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            media=[b"raw file contents"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaUpdateAlbumResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_album(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            client.v1.boxes.media.with_raw_response.update_album(
                album_name="albumName",
                box_id="",
                media=[b"raw file contents"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_name` but received ''"):
            client.v1.boxes.media.with_raw_response.update_album(
                album_name="",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
                media=[b"raw file contents"],
            )


class TestAsyncMedia:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_album(self, async_client: AsyncGboxClient) -> None:
        media = await async_client.v1.boxes.media.create_album(
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            media=[b"raw file contents"],
            name="Vacation Photos",
        )
        assert_matches_type(MediaCreateAlbumResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_album(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.media.with_raw_response.create_album(
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            media=[b"raw file contents"],
            name="Vacation Photos",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaCreateAlbumResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_album(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.media.with_streaming_response.create_album(
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            media=[b"raw file contents"],
            name="Vacation Photos",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaCreateAlbumResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_album(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.create_album(
                box_id="",
                media=[b"raw file contents"],
                name="Vacation Photos",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_album(self, async_client: AsyncGboxClient) -> None:
        media = await async_client.v1.boxes.media.delete_album(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert media is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_album(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.media.with_raw_response.delete_album(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert media is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_album(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.media.with_streaming_response.delete_album(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert media is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete_album(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.delete_album(
                album_name="albumName",
                box_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_name` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.delete_album(
                album_name="",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_media(self, async_client: AsyncGboxClient) -> None:
        media = await async_client.v1.boxes.media.delete_media(
            media_name="mediaName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            album_name="albumName",
        )
        assert media is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_media(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.media.with_raw_response.delete_media(
            media_name="mediaName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            album_name="albumName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert media is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_media(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.media.with_streaming_response.delete_media(
            media_name="mediaName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            album_name="albumName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert media is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete_media(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.delete_media(
                media_name="mediaName",
                box_id="",
                album_name="albumName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_name` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.delete_media(
                media_name="mediaName",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
                album_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_name` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.delete_media(
                media_name="",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
                album_name="albumName",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_download_media(self, async_client: AsyncGboxClient) -> None:
        media = await async_client.v1.boxes.media.download_media(
            media_name="mediaName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            album_name="albumName",
        )
        assert_matches_type(MediaDownloadMediaResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_download_media(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.media.with_raw_response.download_media(
            media_name="mediaName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            album_name="albumName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaDownloadMediaResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_download_media(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.media.with_streaming_response.download_media(
            media_name="mediaName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            album_name="albumName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaDownloadMediaResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_download_media(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.download_media(
                media_name="mediaName",
                box_id="",
                album_name="albumName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_name` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.download_media(
                media_name="mediaName",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
                album_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_name` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.download_media(
                media_name="",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
                album_name="albumName",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_album_detail(self, async_client: AsyncGboxClient) -> None:
        media = await async_client.v1.boxes.media.get_album_detail(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert_matches_type(MediaGetAlbumDetailResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_album_detail(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.media.with_raw_response.get_album_detail(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaGetAlbumDetailResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_album_detail(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.media.with_streaming_response.get_album_detail(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaGetAlbumDetailResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_album_detail(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.get_album_detail(
                album_name="albumName",
                box_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_name` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.get_album_detail(
                album_name="",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_albums(self, async_client: AsyncGboxClient) -> None:
        media = await async_client.v1.boxes.media.list_albums(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert_matches_type(MediaListAlbumsResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_albums(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.media.with_raw_response.list_albums(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaListAlbumsResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_albums(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.media.with_streaming_response.list_albums(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaListAlbumsResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_albums(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.list_albums(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_album(self, async_client: AsyncGboxClient) -> None:
        media = await async_client.v1.boxes.media.update_album(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            media=[b"raw file contents"],
        )
        assert_matches_type(MediaUpdateAlbumResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_album(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.media.with_raw_response.update_album(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            media=[b"raw file contents"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaUpdateAlbumResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_album(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.media.with_streaming_response.update_album(
            album_name="albumName",
            box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            media=[b"raw file contents"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaUpdateAlbumResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_album(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `box_id` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.update_album(
                album_name="albumName",
                box_id="",
                media=[b"raw file contents"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_name` but received ''"):
            await async_client.v1.boxes.media.with_raw_response.update_album(
                album_name="",
                box_id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
                media=[b"raw file contents"],
            )
