# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .create_box_config_param import CreateBoxConfigParam

__all__ = ["BoxCreateAndroidParams"]


class BoxCreateAndroidParams(TypedDict, total=False):
    type: Required[Literal["android"]]
    """Box type is Android"""

    config: CreateBoxConfigParam
    """Configuration for an Android box instance"""

    api_timeout: Annotated[str, PropertyInfo(alias="timeout")]
    """Timeout for the box operation to be completed, default is 30s"""

    wait: bool
    """Wait for the box operation to be completed, default is true"""
