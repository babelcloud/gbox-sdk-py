# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BoxLiveViewURLParams"]


class BoxLiveViewURLParams(TypedDict, total=False):
    expires_in: Annotated[str, PropertyInfo(alias="expiresIn")]
    """The live view will be alive for the given duration (e.g.

    '10m' or '1h'). Default is 180m.
    """
