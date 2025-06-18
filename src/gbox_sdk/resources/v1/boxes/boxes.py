# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, cast
from typing_extensions import Literal

import httpx

from .fs import (
    FsResource,
    AsyncFsResource,
    FsResourceWithRawResponse,
    AsyncFsResourceWithRawResponse,
    FsResourceWithStreamingResponse,
    AsyncFsResourceWithStreamingResponse,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from .android import (
    AndroidResource,
    AsyncAndroidResource,
    AndroidResourceWithRawResponse,
    AsyncAndroidResourceWithRawResponse,
    AndroidResourceWithStreamingResponse,
    AsyncAndroidResourceWithStreamingResponse,
)
from .browser import (
    BrowserResource,
    AsyncBrowserResource,
    BrowserResourceWithRawResponse,
    AsyncBrowserResourceWithRawResponse,
    BrowserResourceWithStreamingResponse,
    AsyncBrowserResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import (
    box_list_params,
    box_stop_params,
    box_start_params,
    box_delete_params,
    box_run_code_params,
    box_create_linux_params,
    box_create_android_params,
    box_execute_commands_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.linux_box import LinuxBox
from ....types.v1.android_box import AndroidBox
from ....types.v1.box_list_response import BoxListResponse
from ....types.v1.box_stop_response import BoxStopResponse
from ....types.v1.box_start_response import BoxStartResponse
from ....types.v1.box_retrieve_response import BoxRetrieveResponse
from ....types.v1.box_run_code_response import BoxRunCodeResponse
from ....types.v1.create_box_config_param import CreateBoxConfigParam
from ....types.v1.box_execute_commands_response import BoxExecuteCommandsResponse

__all__ = ["BoxesResource", "AsyncBoxesResource"]


class BoxesResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def fs(self) -> FsResource:
        return FsResource(self._client)

    @cached_property
    def browser(self) -> BrowserResource:
        return BrowserResource(self._client)

    @cached_property
    def android(self) -> AndroidResource:
        return AndroidResource(self._client)

    @cached_property
    def with_raw_response(self) -> BoxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gbox-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BoxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BoxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gbox-sdk-python#with_streaming_response
        """
        return BoxesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BoxRetrieveResponse:
        """
        Get box

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            BoxRetrieveResponse,
            self._get(
                f"/boxes/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, BoxRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        labels: object | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BoxListResponse:
        """
        List box

        Args:
          labels: Filter boxes by their labels, default is all

          page: Page number

          page_size: Page size

          status: Filter boxes by their current status (pending, running, stopped, error, deleted)

          type: Filter boxes by their type (linux, android etc.) , default is all

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/boxes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "labels": labels,
                        "page": page,
                        "page_size": page_size,
                        "status": status,
                        "type": type,
                    },
                    box_list_params.BoxListParams,
                ),
            ),
            cast_to=BoxListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        wait: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete box

        Args:
          wait: Wait for the box operation to be completed, default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/boxes/{id}",
            body=maybe_transform({"wait": wait}, box_delete_params.BoxDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_android(
        self,
        *,
        config: CreateBoxConfigParam | NotGiven = NOT_GIVEN,
        wait: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AndroidBox:
        """
        Create android box

        Args:
          config: Configuration for a box instance

          wait: Wait for the box operation to be completed, default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/boxes/android",
            body=maybe_transform(
                {
                    "config": config,
                    "wait": wait,
                },
                box_create_android_params.BoxCreateAndroidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AndroidBox,
        )

    def create_linux(
        self,
        *,
        config: CreateBoxConfigParam | NotGiven = NOT_GIVEN,
        wait: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinuxBox:
        """
        Create linux box

        Args:
          config: Configuration for a box instance

          wait: Wait for the box operation to be completed, default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/boxes/linux",
            body=maybe_transform(
                {
                    "config": config,
                    "wait": wait,
                },
                box_create_linux_params.BoxCreateLinuxParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinuxBox,
        )

    def execute_commands(
        self,
        id: str,
        *,
        commands: Union[str, List[str]],
        envs: object | NotGiven = NOT_GIVEN,
        api_timeout: str | NotGiven = NOT_GIVEN,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BoxExecuteCommandsResponse:
        """Exec command

        Args:
          commands: The command to run.

        Can be a single string or an array of strings

          envs: The environment variables to run the command

          api_timeout: The timeout of the command. e.g. '30s' or '1m' or '1h'. If the command times
              out, the exit code will be 124. For example: 'timeout 5s sleep 10s' will result
              in exit code 124.

          working_dir: The working directory of the command

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/boxes/{id}/commands",
            body=maybe_transform(
                {
                    "commands": commands,
                    "envs": envs,
                    "api_timeout": api_timeout,
                    "working_dir": working_dir,
                },
                box_execute_commands_params.BoxExecuteCommandsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BoxExecuteCommandsResponse,
        )

    def run_code(
        self,
        id: str,
        *,
        code: str,
        argv: List[str] | NotGiven = NOT_GIVEN,
        envs: object | NotGiven = NOT_GIVEN,
        language: Literal["bash", "python3", "typescript"] | NotGiven = NOT_GIVEN,
        api_timeout: str | NotGiven = NOT_GIVEN,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BoxRunCodeResponse:
        """
        Run code on the box

        Args:
          code: The code to run

          argv: The arguments to run the code. For example, if you want to run "python index.py
              --help", you should pass ["--help"] as arguments.

          envs: The environment variables to run the code

          language: The language of the code.

          api_timeout: The timeout of the code execution. e.g. "30s" or "1m" or "1h". If the code
              execution times out, the exit code will be 124.

          working_dir: The working directory of the code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/boxes/{id}/run-code",
            body=maybe_transform(
                {
                    "code": code,
                    "argv": argv,
                    "envs": envs,
                    "language": language,
                    "api_timeout": api_timeout,
                    "working_dir": working_dir,
                },
                box_run_code_params.BoxRunCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BoxRunCodeResponse,
        )

    def start(
        self,
        id: str,
        *,
        wait: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BoxStartResponse:
        """
        Start box

        Args:
          wait: Wait for the box operation to be completed, default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            BoxStartResponse,
            self._post(
                f"/boxes/{id}/start",
                body=maybe_transform({"wait": wait}, box_start_params.BoxStartParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, BoxStartResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def stop(
        self,
        id: str,
        *,
        wait: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BoxStopResponse:
        """
        Stop box

        Args:
          wait: Wait for the box operation to be completed, default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            BoxStopResponse,
            self._post(
                f"/boxes/{id}/stop",
                body=maybe_transform({"wait": wait}, box_stop_params.BoxStopParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, BoxStopResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncBoxesResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def fs(self) -> AsyncFsResource:
        return AsyncFsResource(self._client)

    @cached_property
    def browser(self) -> AsyncBrowserResource:
        return AsyncBrowserResource(self._client)

    @cached_property
    def android(self) -> AsyncAndroidResource:
        return AsyncAndroidResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBoxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gbox-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBoxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBoxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gbox-sdk-python#with_streaming_response
        """
        return AsyncBoxesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BoxRetrieveResponse:
        """
        Get box

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            BoxRetrieveResponse,
            await self._get(
                f"/boxes/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, BoxRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        labels: object | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BoxListResponse:
        """
        List box

        Args:
          labels: Filter boxes by their labels, default is all

          page: Page number

          page_size: Page size

          status: Filter boxes by their current status (pending, running, stopped, error, deleted)

          type: Filter boxes by their type (linux, android etc.) , default is all

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/boxes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "labels": labels,
                        "page": page,
                        "page_size": page_size,
                        "status": status,
                        "type": type,
                    },
                    box_list_params.BoxListParams,
                ),
            ),
            cast_to=BoxListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        wait: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete box

        Args:
          wait: Wait for the box operation to be completed, default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/boxes/{id}",
            body=await async_maybe_transform({"wait": wait}, box_delete_params.BoxDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_android(
        self,
        *,
        config: CreateBoxConfigParam | NotGiven = NOT_GIVEN,
        wait: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AndroidBox:
        """
        Create android box

        Args:
          config: Configuration for a box instance

          wait: Wait for the box operation to be completed, default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/boxes/android",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "wait": wait,
                },
                box_create_android_params.BoxCreateAndroidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AndroidBox,
        )

    async def create_linux(
        self,
        *,
        config: CreateBoxConfigParam | NotGiven = NOT_GIVEN,
        wait: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinuxBox:
        """
        Create linux box

        Args:
          config: Configuration for a box instance

          wait: Wait for the box operation to be completed, default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/boxes/linux",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "wait": wait,
                },
                box_create_linux_params.BoxCreateLinuxParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinuxBox,
        )

    async def execute_commands(
        self,
        id: str,
        *,
        commands: Union[str, List[str]],
        envs: object | NotGiven = NOT_GIVEN,
        api_timeout: str | NotGiven = NOT_GIVEN,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BoxExecuteCommandsResponse:
        """Exec command

        Args:
          commands: The command to run.

        Can be a single string or an array of strings

          envs: The environment variables to run the command

          api_timeout: The timeout of the command. e.g. '30s' or '1m' or '1h'. If the command times
              out, the exit code will be 124. For example: 'timeout 5s sleep 10s' will result
              in exit code 124.

          working_dir: The working directory of the command

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/boxes/{id}/commands",
            body=await async_maybe_transform(
                {
                    "commands": commands,
                    "envs": envs,
                    "api_timeout": api_timeout,
                    "working_dir": working_dir,
                },
                box_execute_commands_params.BoxExecuteCommandsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BoxExecuteCommandsResponse,
        )

    async def run_code(
        self,
        id: str,
        *,
        code: str,
        argv: List[str] | NotGiven = NOT_GIVEN,
        envs: object | NotGiven = NOT_GIVEN,
        language: Literal["bash", "python3", "typescript"] | NotGiven = NOT_GIVEN,
        api_timeout: str | NotGiven = NOT_GIVEN,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BoxRunCodeResponse:
        """
        Run code on the box

        Args:
          code: The code to run

          argv: The arguments to run the code. For example, if you want to run "python index.py
              --help", you should pass ["--help"] as arguments.

          envs: The environment variables to run the code

          language: The language of the code.

          api_timeout: The timeout of the code execution. e.g. "30s" or "1m" or "1h". If the code
              execution times out, the exit code will be 124.

          working_dir: The working directory of the code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/boxes/{id}/run-code",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "argv": argv,
                    "envs": envs,
                    "language": language,
                    "api_timeout": api_timeout,
                    "working_dir": working_dir,
                },
                box_run_code_params.BoxRunCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BoxRunCodeResponse,
        )

    async def start(
        self,
        id: str,
        *,
        wait: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BoxStartResponse:
        """
        Start box

        Args:
          wait: Wait for the box operation to be completed, default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            BoxStartResponse,
            await self._post(
                f"/boxes/{id}/start",
                body=await async_maybe_transform({"wait": wait}, box_start_params.BoxStartParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, BoxStartResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def stop(
        self,
        id: str,
        *,
        wait: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BoxStopResponse:
        """
        Stop box

        Args:
          wait: Wait for the box operation to be completed, default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            BoxStopResponse,
            await self._post(
                f"/boxes/{id}/stop",
                body=await async_maybe_transform({"wait": wait}, box_stop_params.BoxStopParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, BoxStopResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class BoxesResourceWithRawResponse:
    def __init__(self, boxes: BoxesResource) -> None:
        self._boxes = boxes

        self.retrieve = to_raw_response_wrapper(
            boxes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            boxes.list,
        )
        self.delete = to_raw_response_wrapper(
            boxes.delete,
        )
        self.create_android = to_raw_response_wrapper(
            boxes.create_android,
        )
        self.create_linux = to_raw_response_wrapper(
            boxes.create_linux,
        )
        self.execute_commands = to_raw_response_wrapper(
            boxes.execute_commands,
        )
        self.run_code = to_raw_response_wrapper(
            boxes.run_code,
        )
        self.start = to_raw_response_wrapper(
            boxes.start,
        )
        self.stop = to_raw_response_wrapper(
            boxes.stop,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._boxes.actions)

    @cached_property
    def fs(self) -> FsResourceWithRawResponse:
        return FsResourceWithRawResponse(self._boxes.fs)

    @cached_property
    def browser(self) -> BrowserResourceWithRawResponse:
        return BrowserResourceWithRawResponse(self._boxes.browser)

    @cached_property
    def android(self) -> AndroidResourceWithRawResponse:
        return AndroidResourceWithRawResponse(self._boxes.android)


class AsyncBoxesResourceWithRawResponse:
    def __init__(self, boxes: AsyncBoxesResource) -> None:
        self._boxes = boxes

        self.retrieve = async_to_raw_response_wrapper(
            boxes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            boxes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            boxes.delete,
        )
        self.create_android = async_to_raw_response_wrapper(
            boxes.create_android,
        )
        self.create_linux = async_to_raw_response_wrapper(
            boxes.create_linux,
        )
        self.execute_commands = async_to_raw_response_wrapper(
            boxes.execute_commands,
        )
        self.run_code = async_to_raw_response_wrapper(
            boxes.run_code,
        )
        self.start = async_to_raw_response_wrapper(
            boxes.start,
        )
        self.stop = async_to_raw_response_wrapper(
            boxes.stop,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._boxes.actions)

    @cached_property
    def fs(self) -> AsyncFsResourceWithRawResponse:
        return AsyncFsResourceWithRawResponse(self._boxes.fs)

    @cached_property
    def browser(self) -> AsyncBrowserResourceWithRawResponse:
        return AsyncBrowserResourceWithRawResponse(self._boxes.browser)

    @cached_property
    def android(self) -> AsyncAndroidResourceWithRawResponse:
        return AsyncAndroidResourceWithRawResponse(self._boxes.android)


class BoxesResourceWithStreamingResponse:
    def __init__(self, boxes: BoxesResource) -> None:
        self._boxes = boxes

        self.retrieve = to_streamed_response_wrapper(
            boxes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            boxes.list,
        )
        self.delete = to_streamed_response_wrapper(
            boxes.delete,
        )
        self.create_android = to_streamed_response_wrapper(
            boxes.create_android,
        )
        self.create_linux = to_streamed_response_wrapper(
            boxes.create_linux,
        )
        self.execute_commands = to_streamed_response_wrapper(
            boxes.execute_commands,
        )
        self.run_code = to_streamed_response_wrapper(
            boxes.run_code,
        )
        self.start = to_streamed_response_wrapper(
            boxes.start,
        )
        self.stop = to_streamed_response_wrapper(
            boxes.stop,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._boxes.actions)

    @cached_property
    def fs(self) -> FsResourceWithStreamingResponse:
        return FsResourceWithStreamingResponse(self._boxes.fs)

    @cached_property
    def browser(self) -> BrowserResourceWithStreamingResponse:
        return BrowserResourceWithStreamingResponse(self._boxes.browser)

    @cached_property
    def android(self) -> AndroidResourceWithStreamingResponse:
        return AndroidResourceWithStreamingResponse(self._boxes.android)


class AsyncBoxesResourceWithStreamingResponse:
    def __init__(self, boxes: AsyncBoxesResource) -> None:
        self._boxes = boxes

        self.retrieve = async_to_streamed_response_wrapper(
            boxes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            boxes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            boxes.delete,
        )
        self.create_android = async_to_streamed_response_wrapper(
            boxes.create_android,
        )
        self.create_linux = async_to_streamed_response_wrapper(
            boxes.create_linux,
        )
        self.execute_commands = async_to_streamed_response_wrapper(
            boxes.execute_commands,
        )
        self.run_code = async_to_streamed_response_wrapper(
            boxes.run_code,
        )
        self.start = async_to_streamed_response_wrapper(
            boxes.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            boxes.stop,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._boxes.actions)

    @cached_property
    def fs(self) -> AsyncFsResourceWithStreamingResponse:
        return AsyncFsResourceWithStreamingResponse(self._boxes.fs)

    @cached_property
    def browser(self) -> AsyncBrowserResourceWithStreamingResponse:
        return AsyncBrowserResourceWithStreamingResponse(self._boxes.browser)

    @cached_property
    def android(self) -> AsyncAndroidResourceWithStreamingResponse:
        return AsyncAndroidResourceWithStreamingResponse(self._boxes.android)
