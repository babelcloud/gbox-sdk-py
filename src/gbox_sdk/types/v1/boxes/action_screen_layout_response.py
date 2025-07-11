# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ActionScreenLayoutResponse"]


class ActionScreenLayoutResponse(BaseModel):
    content: str
    """Screen layout content.

    For Android boxes, this is XML content containing the UI hierarchy with detailed
    element information including bounds, text, resource IDs, and other properties.
    The format may vary for different box types.
    """
