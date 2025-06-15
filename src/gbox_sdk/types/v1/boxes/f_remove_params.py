# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FRemoveParams"]


class FRemoveParams(TypedDict, total=False):
    path: Required[str]
    """Path to the file/directory"""
