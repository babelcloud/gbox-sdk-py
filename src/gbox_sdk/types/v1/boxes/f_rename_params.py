# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FRenameParams"]


class FRenameParams(TypedDict, total=False):
    new_path: Required[Annotated[str, PropertyInfo(alias="newPath")]]
    """New path for the file/directory.

    If the path is not start with '/', the file/directory will be renamed to the
    working directory
    """

    old_path: Required[Annotated[str, PropertyInfo(alias="oldPath")]]
    """Old path to the file/directory.

    If the path is not start with '/', the file/directory will be renamed from the
    working directory
    """

    working_dir: Annotated[str, PropertyInfo(alias="workingDir")]
    """Working directory.

    If not provided, the file will be read from the `box.config.workingDir`
    directory.
    """
