# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["FWriteParams", "WriteFile", "WriteFileByBinary"]


class WriteFile(TypedDict, total=False):
    content: Required[str]
    """Content of the file (Max size: 512MB)"""

    path: Required[str]
    """Path to the file.

    If the path is not start with '/', the file will be written to the working
    directory
    """

    working_dir: Annotated[str, PropertyInfo(alias="workingDir")]
    """Working directory.

    If not provided, the file will be read from the `box.config.workingDir`
    directory.
    """


class WriteFileByBinary(TypedDict, total=False):
    content: Required[FileTypes]
    """Binary content of the file (Max file size: 512MB)"""

    path: Required[str]
    """Path to the file.

    If the path is not start with '/', the file will be written to the working
    directory
    """

    working_dir: Annotated[str, PropertyInfo(alias="workingDir")]
    """Working directory.

    If not provided, the file will be read from the `box.config.workingDir`
    directory.
    """


FWriteParams: TypeAlias = Union[WriteFile, WriteFileByBinary]
