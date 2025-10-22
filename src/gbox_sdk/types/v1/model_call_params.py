# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ModelCallParams"]


class ModelCallParams(TypedDict, total=False):
    action: Required[object]
    """Structured action object (click or drag)"""

    screenshot: Required[str]
    """HTTP(S) URL to screenshot image"""

    model: Literal["gbox-handy-1"]
    """Model to use"""
