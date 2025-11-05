# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.v1.boxes import snapshot_create_params
from ....types.v1.boxes.snapshot_list_response import SnapshotListResponse
from ....types.v1.boxes.snapshot_create_response import SnapshotCreateResponse

__all__ = ["SnapshotResource", "AsyncSnapshotResource"]


class SnapshotResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SnapshotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/babelcloud/gbox-sdk-py#accessing-raw-response-data-eg-headers
        """
        return SnapshotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SnapshotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/babelcloud/gbox-sdk-py#with_streaming_response
        """
        return SnapshotResourceWithStreamingResponse(self)

    def create(
        self,
        box_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotCreateResponse:
        """Create a snapshot of a running box.

        This snapshot will be saved and can be used
        to restore the box to the state it was in at the time the snapshot was created.

        Args:
          name: Name of the snapshot. This name must be unique within the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not box_id:
            raise ValueError(f"Expected a non-empty value for `box_id` but received {box_id!r}")
        return self._post(
            f"/snapshots/{box_id}",
            body=maybe_transform({"name": name}, snapshot_create_params.SnapshotCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotCreateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotListResponse:
        """List all snapshots for a given box."""
        return self._get(
            "/snapshots",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotListResponse,
        )


class AsyncSnapshotResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSnapshotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/babelcloud/gbox-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSnapshotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSnapshotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/babelcloud/gbox-sdk-py#with_streaming_response
        """
        return AsyncSnapshotResourceWithStreamingResponse(self)

    async def create(
        self,
        box_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotCreateResponse:
        """Create a snapshot of a running box.

        This snapshot will be saved and can be used
        to restore the box to the state it was in at the time the snapshot was created.

        Args:
          name: Name of the snapshot. This name must be unique within the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not box_id:
            raise ValueError(f"Expected a non-empty value for `box_id` but received {box_id!r}")
        return await self._post(
            f"/snapshots/{box_id}",
            body=await async_maybe_transform({"name": name}, snapshot_create_params.SnapshotCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotCreateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotListResponse:
        """List all snapshots for a given box."""
        return await self._get(
            "/snapshots",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotListResponse,
        )


class SnapshotResourceWithRawResponse:
    def __init__(self, snapshot: SnapshotResource) -> None:
        self._snapshot = snapshot

        self.create = to_raw_response_wrapper(
            snapshot.create,
        )
        self.list = to_raw_response_wrapper(
            snapshot.list,
        )


class AsyncSnapshotResourceWithRawResponse:
    def __init__(self, snapshot: AsyncSnapshotResource) -> None:
        self._snapshot = snapshot

        self.create = async_to_raw_response_wrapper(
            snapshot.create,
        )
        self.list = async_to_raw_response_wrapper(
            snapshot.list,
        )


class SnapshotResourceWithStreamingResponse:
    def __init__(self, snapshot: SnapshotResource) -> None:
        self._snapshot = snapshot

        self.create = to_streamed_response_wrapper(
            snapshot.create,
        )
        self.list = to_streamed_response_wrapper(
            snapshot.list,
        )


class AsyncSnapshotResourceWithStreamingResponse:
    def __init__(self, snapshot: AsyncSnapshotResource) -> None:
        self._snapshot = snapshot

        self.create = async_to_streamed_response_wrapper(
            snapshot.create,
        )
        self.list = async_to_streamed_response_wrapper(
            snapshot.list,
        )
