# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AndroidAppiumURLParams"]


class AndroidAppiumURLParams(TypedDict, total=False):
    expires_in: Annotated[str, PropertyInfo(alias="expiresIn")]
    """The Appium connection url will be alive for the given duration

    Supported time units: ms (milliseconds), s (seconds), m (minutes), h (hours)
    Example formats: "500ms", "30s", "5m", "1h" Default: 120m
    """
