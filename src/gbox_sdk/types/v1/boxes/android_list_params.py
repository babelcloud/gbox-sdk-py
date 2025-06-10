# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AndroidListParams"]


class AndroidListParams(TypedDict, total=False):
    app_type: Annotated[Literal["system", "third-party"], PropertyInfo(alias="appType")]
    """Application type: system or third-party, default is all"""

    is_running: Annotated[bool, PropertyInfo(alias="isRunning")]
    """Whether to include running apps, default is all"""
