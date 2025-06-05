# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .create_box_config_param import CreateBoxConfigParam

__all__ = ["BoxCreateParams", "CreateLinuxBox", "CreateAndroidBox"]


class CreateLinuxBox(TypedDict, total=False):
    type: Required[Literal["linux"]]
    """Box type is Linux"""

    config: CreateBoxConfigParam
    """Configuration for a Linux box instance"""

    api_timeout: Annotated[str, PropertyInfo(alias="timeout")]
    """Timeout for the box operation to be completed, default is 30s"""

    wait: bool
    """Wait for the box operation to be completed, default is true"""


class CreateAndroidBox(TypedDict, total=False):
    type: Required[Literal["android"]]
    """Box type is Android"""

    config: CreateBoxConfigParam
    """Configuration for an Android box instance"""

    api_timeout: Annotated[str, PropertyInfo(alias="timeout")]
    """Timeout for the box operation to be completed, default is 30s"""

    wait: bool
    """Wait for the box operation to be completed, default is true"""


BoxCreateParams: TypeAlias = Union[CreateLinuxBox, CreateAndroidBox]
