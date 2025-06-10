# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ActionTypeParams"]


class ActionTypeParams(TypedDict, total=False):
    text: Required[str]
    """Text to type"""

    delay: str
    """Time to wait between key presses. Defaults to 0ms."""

    output_format: Annotated[Literal["base64", "storageKey"], PropertyInfo(alias="outputFormat")]
    """Type of the URI"""
