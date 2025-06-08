# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BoxStartParams"]


class BoxStartParams(TypedDict, total=False):
    api_timeout: Annotated[str, PropertyInfo(alias="timeout")]
    """Timeout for the box operation to be completed, default is 30s"""

    wait: bool
    """Wait for the box operation to be completed, default is true"""
