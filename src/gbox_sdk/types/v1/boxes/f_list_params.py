# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FListParams"]


class FListParams(TypedDict, total=False):
    depth: Required[float]
    """Depth of the directory"""

    path: Required[str]
    """Path to the directory"""
