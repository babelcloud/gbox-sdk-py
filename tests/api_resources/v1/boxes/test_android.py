# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gbox_sdk import GboxClient, AsyncGboxClient
from tests.utils import assert_matches_type
from gbox_sdk.types.v1.boxes import (
    AndroidApp,
    AndroidListResponse,
    AndroidListActivitiesResponse,
    AndroidGetConnectAddressResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAndroid:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.list(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert_matches_type(AndroidListResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.list(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            app_type="third-party",
            is_running=True,
        )
        assert_matches_type(AndroidListResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: GboxClient) -> None:
        response = client.v1.boxes.android.with_raw_response.list(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = response.parse()
        assert_matches_type(AndroidListResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: GboxClient) -> None:
        with client.v1.boxes.android.with_streaming_response.list(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = response.parse()
            assert_matches_type(AndroidListResponse, android, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.boxes.android.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_close(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.close(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_close(self, client: GboxClient) -> None:
        response = client.v1.boxes.android.with_raw_response.close(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_close(self, client: GboxClient) -> None:
        with client.v1.boxes.android.with_streaming_response.close(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_close(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.boxes.android.with_raw_response.close(
                package_name="com.example.myapp",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_name` but received ''"):
            client.v1.boxes.android.with_raw_response.close(
                package_name="",
                id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_close_all(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.close_all(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_close_all(self, client: GboxClient) -> None:
        response = client.v1.boxes.android.with_raw_response.close_all(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_close_all(self, client: GboxClient) -> None:
        with client.v1.boxes.android.with_streaming_response.close_all(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_close_all(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.boxes.android.with_raw_response.close_all(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.get(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert_matches_type(AndroidApp, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: GboxClient) -> None:
        response = client.v1.boxes.android.with_raw_response.get(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = response.parse()
        assert_matches_type(AndroidApp, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: GboxClient) -> None:
        with client.v1.boxes.android.with_streaming_response.get(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = response.parse()
            assert_matches_type(AndroidApp, android, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.boxes.android.with_raw_response.get(
                package_name="com.example.myapp",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_name` but received ''"):
            client.v1.boxes.android.with_raw_response.get(
                package_name="",
                id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_connect_address(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.get_connect_address(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert_matches_type(AndroidGetConnectAddressResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_connect_address(self, client: GboxClient) -> None:
        response = client.v1.boxes.android.with_raw_response.get_connect_address(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = response.parse()
        assert_matches_type(AndroidGetConnectAddressResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_connect_address(self, client: GboxClient) -> None:
        with client.v1.boxes.android.with_streaming_response.get_connect_address(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = response.parse()
            assert_matches_type(AndroidGetConnectAddressResponse, android, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_connect_address(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.boxes.android.with_raw_response.get_connect_address(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_install_overload_1(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.install(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            apk=b"raw file contents",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_install_overload_1(self, client: GboxClient) -> None:
        response = client.v1.boxes.android.with_raw_response.install(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            apk=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_install_overload_1(self, client: GboxClient) -> None:
        with client.v1.boxes.android.with_streaming_response.install(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            apk=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_install_overload_1(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.boxes.android.with_raw_response.install(
                id="",
                apk=b"raw file contents",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_install_overload_2(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.install(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            apk="https://example.com/app.apk",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_install_overload_2(self, client: GboxClient) -> None:
        response = client.v1.boxes.android.with_raw_response.install(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            apk="https://example.com/app.apk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_install_overload_2(self, client: GboxClient) -> None:
        with client.v1.boxes.android.with_streaming_response.install(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            apk="https://example.com/app.apk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_install_overload_2(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.boxes.android.with_raw_response.install(
                id="",
                apk="https://example.com/app.apk",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_activities(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.list_activities(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert_matches_type(AndroidListActivitiesResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_activities(self, client: GboxClient) -> None:
        response = client.v1.boxes.android.with_raw_response.list_activities(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = response.parse()
        assert_matches_type(AndroidListActivitiesResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_activities(self, client: GboxClient) -> None:
        with client.v1.boxes.android.with_streaming_response.list_activities(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = response.parse()
            assert_matches_type(AndroidListActivitiesResponse, android, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_activities(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.boxes.android.with_raw_response.list_activities(
                package_name="com.example.myapp",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_name` but received ''"):
            client.v1.boxes.android.with_raw_response.list_activities(
                package_name="",
                id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_open(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.open(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_method_open_with_all_params(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.open(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            activity_name="com.android.settings.Settings",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_open(self, client: GboxClient) -> None:
        response = client.v1.boxes.android.with_raw_response.open(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_open(self, client: GboxClient) -> None:
        with client.v1.boxes.android.with_streaming_response.open(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_open(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.boxes.android.with_raw_response.open(
                package_name="com.example.myapp",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_name` but received ''"):
            client.v1.boxes.android.with_raw_response.open(
                package_name="",
                id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_restart(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.restart(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_restart(self, client: GboxClient) -> None:
        response = client.v1.boxes.android.with_raw_response.restart(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_restart(self, client: GboxClient) -> None:
        with client.v1.boxes.android.with_streaming_response.restart(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_restart(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.boxes.android.with_raw_response.restart(
                package_name="com.example.myapp",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_name` but received ''"):
            client.v1.boxes.android.with_raw_response.restart(
                package_name="",
                id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_uninstall(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.uninstall(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_method_uninstall_with_all_params(self, client: GboxClient) -> None:
        android = client.v1.boxes.android.uninstall(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            keep_data=True,
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_uninstall(self, client: GboxClient) -> None:
        response = client.v1.boxes.android.with_raw_response.uninstall(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_uninstall(self, client: GboxClient) -> None:
        with client.v1.boxes.android.with_streaming_response.uninstall(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_uninstall(self, client: GboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.boxes.android.with_raw_response.uninstall(
                package_name="com.example.myapp",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_name` but received ''"):
            client.v1.boxes.android.with_raw_response.uninstall(
                package_name="",
                id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )


class TestAsyncAndroid:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.list(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert_matches_type(AndroidListResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.list(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            app_type="third-party",
            is_running=True,
        )
        assert_matches_type(AndroidListResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.android.with_raw_response.list(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = await response.parse()
        assert_matches_type(AndroidListResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.android.with_streaming_response.list(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = await response.parse()
            assert_matches_type(AndroidListResponse, android, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_close(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.close(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_close(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.android.with_raw_response.close(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = await response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_close(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.android.with_streaming_response.close(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = await response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_close(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.close(
                package_name="com.example.myapp",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_name` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.close(
                package_name="",
                id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_close_all(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.close_all(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_close_all(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.android.with_raw_response.close_all(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = await response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_close_all(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.android.with_streaming_response.close_all(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = await response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_close_all(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.close_all(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.get(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert_matches_type(AndroidApp, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.android.with_raw_response.get(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = await response.parse()
        assert_matches_type(AndroidApp, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.android.with_streaming_response.get(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = await response.parse()
            assert_matches_type(AndroidApp, android, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.get(
                package_name="com.example.myapp",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_name` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.get(
                package_name="",
                id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_connect_address(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.get_connect_address(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert_matches_type(AndroidGetConnectAddressResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_connect_address(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.android.with_raw_response.get_connect_address(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = await response.parse()
        assert_matches_type(AndroidGetConnectAddressResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_connect_address(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.android.with_streaming_response.get_connect_address(
            "c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = await response.parse()
            assert_matches_type(AndroidGetConnectAddressResponse, android, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_connect_address(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.get_connect_address(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_install_overload_1(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.install(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            apk=b"raw file contents",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_install_overload_1(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.android.with_raw_response.install(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            apk=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = await response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_install_overload_1(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.android.with_streaming_response.install(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            apk=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = await response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_install_overload_1(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.install(
                id="",
                apk=b"raw file contents",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_install_overload_2(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.install(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            apk="https://example.com/app.apk",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_install_overload_2(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.android.with_raw_response.install(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            apk="https://example.com/app.apk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = await response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_install_overload_2(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.android.with_streaming_response.install(
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            apk="https://example.com/app.apk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = await response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_install_overload_2(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.install(
                id="",
                apk="https://example.com/app.apk",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_activities(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.list_activities(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert_matches_type(AndroidListActivitiesResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_activities(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.android.with_raw_response.list_activities(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = await response.parse()
        assert_matches_type(AndroidListActivitiesResponse, android, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_activities(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.android.with_streaming_response.list_activities(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = await response.parse()
            assert_matches_type(AndroidListActivitiesResponse, android, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_activities(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.list_activities(
                package_name="com.example.myapp",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_name` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.list_activities(
                package_name="",
                id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_open(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.open(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_open_with_all_params(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.open(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            activity_name="com.android.settings.Settings",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_open(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.android.with_raw_response.open(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = await response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_open(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.android.with_streaming_response.open(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = await response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_open(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.open(
                package_name="com.example.myapp",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_name` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.open(
                package_name="",
                id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_restart(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.restart(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_restart(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.android.with_raw_response.restart(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = await response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_restart(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.android.with_streaming_response.restart(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = await response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_restart(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.restart(
                package_name="com.example.myapp",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_name` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.restart(
                package_name="",
                id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_uninstall(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.uninstall(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_uninstall_with_all_params(self, async_client: AsyncGboxClient) -> None:
        android = await async_client.v1.boxes.android.uninstall(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            keep_data=True,
        )
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_uninstall(self, async_client: AsyncGboxClient) -> None:
        response = await async_client.v1.boxes.android.with_raw_response.uninstall(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        android = await response.parse()
        assert android is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_uninstall(self, async_client: AsyncGboxClient) -> None:
        async with async_client.v1.boxes.android.with_streaming_response.uninstall(
            package_name="com.example.myapp",
            id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            android = await response.parse()
            assert android is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_uninstall(self, async_client: AsyncGboxClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.uninstall(
                package_name="com.example.myapp",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_name` but received ''"):
            await async_client.v1.boxes.android.with_raw_response.uninstall(
                package_name="",
                id="c9bdc193-b54b-4ddb-a035-5ac0c598d32d",
            )
