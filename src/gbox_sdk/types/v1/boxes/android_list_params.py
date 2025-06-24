# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AndroidListParams"]


class AndroidListParams(TypedDict, total=False):
    app_type: Annotated[List[Literal["system", "thirdParty"]], PropertyInfo(alias="appType")]
    """Application type: system or third-party, default is third-party"""

    running_filter: Annotated[List[Literal["running", "notRunning"]], PropertyInfo(alias="runningFilter")]
    """
    Filter apps by running status: running (show only running apps), notRunning
    (show only non-running apps). Default is all
    """
