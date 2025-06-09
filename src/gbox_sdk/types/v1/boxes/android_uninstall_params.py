# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AndroidUninstallParams"]


class AndroidUninstallParams(TypedDict, total=False):
    id: Required[str]

    keep_data: Required[Annotated[bool, PropertyInfo(alias="keepData")]]
    """uninstalls the application while retaining the data/cache"""
