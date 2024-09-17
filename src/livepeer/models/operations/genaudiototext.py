"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.models.components import (
    httpmetadata as components_httpmetadata,
    textresponse as components_textresponse,
)
from livepeer.models.errors import studio_api_error as errors_studio_api_error
from livepeer.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GenAudioToTextResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    text_response: NotRequired[components_textresponse.TextResponseTypedDict]
    r"""Successful Response"""
    studio_api_error: NotRequired[errors_studio_api_error.StudioAPIError]
    r"""Error"""


class GenAudioToTextResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    text_response: Optional[components_textresponse.TextResponse] = None
    r"""Successful Response"""

    studio_api_error: Optional[errors_studio_api_error.StudioAPIError] = None
    r"""Error"""
