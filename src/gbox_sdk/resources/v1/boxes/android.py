# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from ...._utils import extract_files, required_args, maybe_transform, deepcopy_minimal, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.boxes import android_list_params, android_install_params, android_uninstall_params
from ....types.v1.boxes.android_app import AndroidApp
from ....types.v1.boxes.android_list_response import AndroidListResponse

__all__ = ["AndroidResource", "AsyncAndroidResource"]


class AndroidResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AndroidResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gbox-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AndroidResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AndroidResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gbox-sdk-python#with_streaming_response
        """
        return AndroidResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        app_type: Literal["system", "third-party"] | NotGiven = NOT_GIVEN,
        is_running: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AndroidListResponse:
        """
        List android app

        Args:
          app_type: Application type: system or third-party, default is all

          is_running: Whether to include running apps, default is all

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/boxes/{id}/android/apps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_type": app_type,
                        "is_running": is_running,
                    },
                    android_list_params.AndroidListParams,
                ),
            ),
            cast_to=AndroidListResponse,
        )

    def get(
        self,
        package_name: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AndroidApp:
        """
        Get android app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        return self._get(
            f"/boxes/{id}/android/apps/{package_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AndroidApp,
        )

    @overload
    def install(
        self,
        id: str,
        *,
        apk: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Install android app

        Args:
          apk: APK file to install (max file size: 200MB)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def install(
        self,
        id: str,
        *,
        apk: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Install android app

        Args:
          apk: HTTP URL to download APK file (max file size: 200MB)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["apk"])
    def install(
        self,
        id: str,
        *,
        apk: FileTypes | str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal({"apk": apk})
        files = extract_files(cast(Mapping[str, object], body), paths=[["apk"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._post(
            f"/boxes/{id}/android/apps",
            body=maybe_transform(body, android_install_params.AndroidInstallParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def uninstall(
        self,
        package_name: str,
        *,
        id: str,
        keep_data: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Uninstall android app

        Args:
          keep_data: uninstalls the application while retaining the data/cache

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/boxes/{id}/android/apps/{package_name}",
            body=maybe_transform({"keep_data": keep_data}, android_uninstall_params.AndroidUninstallParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAndroidResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAndroidResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gbox-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAndroidResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAndroidResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gbox-sdk-python#with_streaming_response
        """
        return AsyncAndroidResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        app_type: Literal["system", "third-party"] | NotGiven = NOT_GIVEN,
        is_running: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AndroidListResponse:
        """
        List android app

        Args:
          app_type: Application type: system or third-party, default is all

          is_running: Whether to include running apps, default is all

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/boxes/{id}/android/apps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "app_type": app_type,
                        "is_running": is_running,
                    },
                    android_list_params.AndroidListParams,
                ),
            ),
            cast_to=AndroidListResponse,
        )

    async def get(
        self,
        package_name: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AndroidApp:
        """
        Get android app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        return await self._get(
            f"/boxes/{id}/android/apps/{package_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AndroidApp,
        )

    @overload
    async def install(
        self,
        id: str,
        *,
        apk: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Install android app

        Args:
          apk: APK file to install (max file size: 200MB)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def install(
        self,
        id: str,
        *,
        apk: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Install android app

        Args:
          apk: HTTP URL to download APK file (max file size: 200MB)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["apk"])
    async def install(
        self,
        id: str,
        *,
        apk: FileTypes | str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal({"apk": apk})
        files = extract_files(cast(Mapping[str, object], body), paths=[["apk"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._post(
            f"/boxes/{id}/android/apps",
            body=await async_maybe_transform(body, android_install_params.AndroidInstallParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def uninstall(
        self,
        package_name: str,
        *,
        id: str,
        keep_data: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Uninstall android app

        Args:
          keep_data: uninstalls the application while retaining the data/cache

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/boxes/{id}/android/apps/{package_name}",
            body=await async_maybe_transform({"keep_data": keep_data}, android_uninstall_params.AndroidUninstallParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AndroidResourceWithRawResponse:
    def __init__(self, android: AndroidResource) -> None:
        self._android = android

        self.list = to_raw_response_wrapper(
            android.list,
        )
        self.get = to_raw_response_wrapper(
            android.get,
        )
        self.install = to_raw_response_wrapper(
            android.install,
        )
        self.uninstall = to_raw_response_wrapper(
            android.uninstall,
        )


class AsyncAndroidResourceWithRawResponse:
    def __init__(self, android: AsyncAndroidResource) -> None:
        self._android = android

        self.list = async_to_raw_response_wrapper(
            android.list,
        )
        self.get = async_to_raw_response_wrapper(
            android.get,
        )
        self.install = async_to_raw_response_wrapper(
            android.install,
        )
        self.uninstall = async_to_raw_response_wrapper(
            android.uninstall,
        )


class AndroidResourceWithStreamingResponse:
    def __init__(self, android: AndroidResource) -> None:
        self._android = android

        self.list = to_streamed_response_wrapper(
            android.list,
        )
        self.get = to_streamed_response_wrapper(
            android.get,
        )
        self.install = to_streamed_response_wrapper(
            android.install,
        )
        self.uninstall = to_streamed_response_wrapper(
            android.uninstall,
        )


class AsyncAndroidResourceWithStreamingResponse:
    def __init__(self, android: AsyncAndroidResource) -> None:
        self._android = android

        self.list = async_to_streamed_response_wrapper(
            android.list,
        )
        self.get = async_to_streamed_response_wrapper(
            android.get,
        )
        self.install = async_to_streamed_response_wrapper(
            android.install,
        )
        self.uninstall = async_to_streamed_response_wrapper(
            android.uninstall,
        )
