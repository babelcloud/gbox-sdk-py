# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .create_box_config_param import CreateBoxConfigParam

__all__ = ["BoxCreateAndroidParams"]


class BoxCreateAndroidParams(TypedDict, total=False):
    config: CreateBoxConfigParam
    """Configuration for a box instance"""

    wait: bool
    """Wait for the box operation to be completed, default is true"""
