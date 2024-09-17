"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer import utils
from livepeer.models.components import (
    httpmetadata as components_httpmetadata,
    validationerror as components_validationerror,
)
from livepeer.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated


class HTTPValidationErrorData(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    http_meta1: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    http_meta2: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    http_meta3: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    http_meta4: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    http_meta5: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    detail: Optional[List[components_validationerror.ValidationError]] = None


class HTTPValidationError(Exception):
    data: HTTPValidationErrorData

    def __init__(self, data: HTTPValidationErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, HTTPValidationErrorData)
