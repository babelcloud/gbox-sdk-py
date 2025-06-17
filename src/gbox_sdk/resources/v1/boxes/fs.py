# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.boxes import (
    f_info_params,
    f_list_params,
    f_read_params,
    f_write_params,
    f_exists_params,
    f_remove_params,
    f_rename_params,
)
from ....types.v1.boxes.f_info_response import FInfoResponse
from ....types.v1.boxes.f_list_response import FListResponse
from ....types.v1.boxes.f_read_response import FReadResponse
from ....types.v1.boxes.f_write_response import FWriteResponse
from ....types.v1.boxes.f_exists_response import FExistsResponse
from ....types.v1.boxes.f_remove_response import FRemoveResponse
from ....types.v1.boxes.f_rename_response import FRenameResponse

__all__ = ["FsResource", "AsyncFsResource"]


class FsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gbox-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gbox-sdk-python#with_streaming_response
        """
        return FsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        path: str,
        depth: float | NotGiven = NOT_GIVEN,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FListResponse:
        """
        List box files

        Args:
          path: Path to the directory

          depth: Depth of the directory

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/boxes/{id}/fs/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "path": path,
                        "depth": depth,
                        "working_dir": working_dir,
                    },
                    f_list_params.FListParams,
                ),
            ),
            cast_to=FListResponse,
        )

    def exists(
        self,
        id: str,
        *,
        path: str,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FExistsResponse:
        """Check if file exists

        Args:
          path: Path to the file/directory.

        If the path is not start with '/', the
              file/directory will be checked from the working directory

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/boxes/{id}/fs/exists",
            body=maybe_transform(
                {
                    "path": path,
                    "working_dir": working_dir,
                },
                f_exists_params.FExistsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FExistsResponse,
        )

    def info(
        self,
        id: str,
        *,
        path: str,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FInfoResponse:
        """Get file/directory

        Args:
          path: Path to the file/directory.

        If the path is not start with '/', the
              file/directory will be checked from the working directory

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/boxes/{id}/fs/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "path": path,
                        "working_dir": working_dir,
                    },
                    f_info_params.FInfoParams,
                ),
            ),
            cast_to=FInfoResponse,
        )

    def read(
        self,
        id: str,
        *,
        path: str,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FReadResponse:
        """Read box file

        Args:
          path: Path to the file.

        If the path is not start with '/', the file will be read from
              the working directory.

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/boxes/{id}/fs/read",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "path": path,
                        "working_dir": working_dir,
                    },
                    f_read_params.FReadParams,
                ),
            ),
            cast_to=FReadResponse,
        )

    def remove(
        self,
        id: str,
        *,
        path: str,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FRemoveResponse:
        """Delete box file/directory

        Args:
          path: Path to the file/directory.

        If the path is not start with '/', the
              file/directory will be deleted from the working directory

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/boxes/{id}/fs",
            body=maybe_transform(
                {
                    "path": path,
                    "working_dir": working_dir,
                },
                f_remove_params.FRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FRemoveResponse,
        )

    def rename(
        self,
        id: str,
        *,
        new_path: str,
        old_path: str,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FRenameResponse:
        """Rename box file

        Args:
          new_path: New path for the file/directory.

        If the path is not start with '/', the
              file/directory will be renamed to the working directory

          old_path: Old path to the file/directory. If the path is not start with '/', the
              file/directory will be renamed from the working directory

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/boxes/{id}/fs/rename",
            body=maybe_transform(
                {
                    "new_path": new_path,
                    "old_path": old_path,
                    "working_dir": working_dir,
                },
                f_rename_params.FRenameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FRenameResponse,
        )

    def write(
        self,
        id: str,
        *,
        content: str,
        path: str,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FWriteResponse:
        """Creates or overwrites a file.

        Creates necessary directories in the path if they
        don't exist. if the path is a directory, the write will be failed.

        Args:
          content: Content of the file

          path: Path to the file. If the path is not start with '/', the file will be written to
              the working directory

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/boxes/{id}/fs/write",
            body=maybe_transform(
                {
                    "content": content,
                    "path": path,
                    "working_dir": working_dir,
                },
                f_write_params.FWriteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FWriteResponse,
        )


class AsyncFsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gbox-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gbox-sdk-python#with_streaming_response
        """
        return AsyncFsResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        path: str,
        depth: float | NotGiven = NOT_GIVEN,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FListResponse:
        """
        List box files

        Args:
          path: Path to the directory

          depth: Depth of the directory

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/boxes/{id}/fs/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "path": path,
                        "depth": depth,
                        "working_dir": working_dir,
                    },
                    f_list_params.FListParams,
                ),
            ),
            cast_to=FListResponse,
        )

    async def exists(
        self,
        id: str,
        *,
        path: str,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FExistsResponse:
        """Check if file exists

        Args:
          path: Path to the file/directory.

        If the path is not start with '/', the
              file/directory will be checked from the working directory

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/boxes/{id}/fs/exists",
            body=await async_maybe_transform(
                {
                    "path": path,
                    "working_dir": working_dir,
                },
                f_exists_params.FExistsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FExistsResponse,
        )

    async def info(
        self,
        id: str,
        *,
        path: str,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FInfoResponse:
        """Get file/directory

        Args:
          path: Path to the file/directory.

        If the path is not start with '/', the
              file/directory will be checked from the working directory

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/boxes/{id}/fs/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "path": path,
                        "working_dir": working_dir,
                    },
                    f_info_params.FInfoParams,
                ),
            ),
            cast_to=FInfoResponse,
        )

    async def read(
        self,
        id: str,
        *,
        path: str,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FReadResponse:
        """Read box file

        Args:
          path: Path to the file.

        If the path is not start with '/', the file will be read from
              the working directory.

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/boxes/{id}/fs/read",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "path": path,
                        "working_dir": working_dir,
                    },
                    f_read_params.FReadParams,
                ),
            ),
            cast_to=FReadResponse,
        )

    async def remove(
        self,
        id: str,
        *,
        path: str,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FRemoveResponse:
        """Delete box file/directory

        Args:
          path: Path to the file/directory.

        If the path is not start with '/', the
              file/directory will be deleted from the working directory

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/boxes/{id}/fs",
            body=await async_maybe_transform(
                {
                    "path": path,
                    "working_dir": working_dir,
                },
                f_remove_params.FRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FRemoveResponse,
        )

    async def rename(
        self,
        id: str,
        *,
        new_path: str,
        old_path: str,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FRenameResponse:
        """Rename box file

        Args:
          new_path: New path for the file/directory.

        If the path is not start with '/', the
              file/directory will be renamed to the working directory

          old_path: Old path to the file/directory. If the path is not start with '/', the
              file/directory will be renamed from the working directory

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/boxes/{id}/fs/rename",
            body=await async_maybe_transform(
                {
                    "new_path": new_path,
                    "old_path": old_path,
                    "working_dir": working_dir,
                },
                f_rename_params.FRenameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FRenameResponse,
        )

    async def write(
        self,
        id: str,
        *,
        content: str,
        path: str,
        working_dir: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FWriteResponse:
        """Creates or overwrites a file.

        Creates necessary directories in the path if they
        don't exist. if the path is a directory, the write will be failed.

        Args:
          content: Content of the file

          path: Path to the file. If the path is not start with '/', the file will be written to
              the working directory

          working_dir: Working directory. If not provided, the file will be read from the root
              directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/boxes/{id}/fs/write",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "path": path,
                    "working_dir": working_dir,
                },
                f_write_params.FWriteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FWriteResponse,
        )


class FsResourceWithRawResponse:
    def __init__(self, fs: FsResource) -> None:
        self._fs = fs

        self.list = to_raw_response_wrapper(
            fs.list,
        )
        self.exists = to_raw_response_wrapper(
            fs.exists,
        )
        self.info = to_raw_response_wrapper(
            fs.info,
        )
        self.read = to_raw_response_wrapper(
            fs.read,
        )
        self.remove = to_raw_response_wrapper(
            fs.remove,
        )
        self.rename = to_raw_response_wrapper(
            fs.rename,
        )
        self.write = to_raw_response_wrapper(
            fs.write,
        )


class AsyncFsResourceWithRawResponse:
    def __init__(self, fs: AsyncFsResource) -> None:
        self._fs = fs

        self.list = async_to_raw_response_wrapper(
            fs.list,
        )
        self.exists = async_to_raw_response_wrapper(
            fs.exists,
        )
        self.info = async_to_raw_response_wrapper(
            fs.info,
        )
        self.read = async_to_raw_response_wrapper(
            fs.read,
        )
        self.remove = async_to_raw_response_wrapper(
            fs.remove,
        )
        self.rename = async_to_raw_response_wrapper(
            fs.rename,
        )
        self.write = async_to_raw_response_wrapper(
            fs.write,
        )


class FsResourceWithStreamingResponse:
    def __init__(self, fs: FsResource) -> None:
        self._fs = fs

        self.list = to_streamed_response_wrapper(
            fs.list,
        )
        self.exists = to_streamed_response_wrapper(
            fs.exists,
        )
        self.info = to_streamed_response_wrapper(
            fs.info,
        )
        self.read = to_streamed_response_wrapper(
            fs.read,
        )
        self.remove = to_streamed_response_wrapper(
            fs.remove,
        )
        self.rename = to_streamed_response_wrapper(
            fs.rename,
        )
        self.write = to_streamed_response_wrapper(
            fs.write,
        )


class AsyncFsResourceWithStreamingResponse:
    def __init__(self, fs: AsyncFsResource) -> None:
        self._fs = fs

        self.list = async_to_streamed_response_wrapper(
            fs.list,
        )
        self.exists = async_to_streamed_response_wrapper(
            fs.exists,
        )
        self.info = async_to_streamed_response_wrapper(
            fs.info,
        )
        self.read = async_to_streamed_response_wrapper(
            fs.read,
        )
        self.remove = async_to_streamed_response_wrapper(
            fs.remove,
        )
        self.rename = async_to_streamed_response_wrapper(
            fs.rename,
        )
        self.write = async_to_streamed_response_wrapper(
            fs.write,
        )
