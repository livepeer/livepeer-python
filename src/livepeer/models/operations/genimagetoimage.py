"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.models.components import (
    httpmetadata as components_httpmetadata,
    imageresponse as components_imageresponse,
)
from livepeer.models.errors import studio_api_error as errors_studio_api_error
from livepeer.types import BaseModel
from livepeer.utils import FieldMetadata, SecurityMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GenImageToImageSecurityTypedDict(TypedDict):
    http_bearer: str


class GenImageToImageSecurity(BaseModel):
    http_bearer: Annotated[
        str,
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="http",
                sub_type="bearer",
                field_name="Authorization",
            )
        ),
    ]


class GenImageToImageResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    image_response: NotRequired[components_imageresponse.ImageResponseTypedDict]
    r"""Successful Response"""
    studio_api_error: NotRequired[errors_studio_api_error.StudioAPIError]
    r"""Error"""


class GenImageToImageResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    image_response: Optional[components_imageresponse.ImageResponse] = None
    r"""Successful Response"""

    studio_api_error: Optional[errors_studio_api_error.StudioAPIError] = None
    r"""Error"""
