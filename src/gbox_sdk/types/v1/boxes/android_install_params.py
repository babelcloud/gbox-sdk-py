# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from ...._types import FileTypes

__all__ = ["AndroidInstallParams", "InstallAndroidAppByFile", "InstallAndroidAppByURL"]


class InstallAndroidAppByFile(TypedDict, total=False):
    apk: Required[FileTypes]
    """APK file to install (max file size: 512MB)"""


class InstallAndroidAppByURL(TypedDict, total=False):
    apk: Required[str]
    """HTTP URL to download APK file (max file size: 512MB)"""


AndroidInstallParams: TypeAlias = Union[InstallAndroidAppByFile, InstallAndroidAppByURL]
