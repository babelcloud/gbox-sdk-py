# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .create_box_config_param import CreateBoxConfigParam

__all__ = ["CreateLinuxBoxParam"]


class CreateLinuxBoxParam(TypedDict, total=False):
    type: Required[Literal["linux"]]
    """Box type is Linux"""

    config: CreateBoxConfigParam
    """Configuration for a box instance"""

    timeout: str
    """Timeout for the box operation to be completed, default is 30s"""

    wait: bool
    """Wait for the box operation to be completed, default is true"""
