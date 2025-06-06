# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from ...._types import FileTypes

__all__ = ["AndroidInstallParams", "InstallAndroidAppByFile", "InstallAndroidAppByURLDto"]


class InstallAndroidAppByFile(TypedDict, total=False):
    apk: Required[FileTypes]
    """APK file to install (max file size: 200MB)"""


class InstallAndroidAppByURLDto(TypedDict, total=False):
    apk: Required[str]
    """HTTP URL to download APK file (max file size: 200MB)"""


AndroidInstallParams: TypeAlias = Union[InstallAndroidAppByFile, InstallAndroidAppByURLDto]
