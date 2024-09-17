"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.models.components import (
    httpmetadata as components_httpmetadata,
    masksresponse as components_masksresponse,
)
from livepeer.models.errors import studio_api_error as errors_studio_api_error
from livepeer.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GenSegmentAnything2ResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    masks_response: NotRequired[components_masksresponse.MasksResponseTypedDict]
    r"""Successful Response"""
    studio_api_error: NotRequired[errors_studio_api_error.StudioAPIError]
    r"""Error"""


class GenSegmentAnything2Response(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    masks_response: Optional[components_masksresponse.MasksResponse] = None
    r"""Successful Response"""

    studio_api_error: Optional[errors_studio_api_error.StudioAPIError] = None
    r"""Error"""
