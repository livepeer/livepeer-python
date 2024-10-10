"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.models.components import (
    httpmetadata as components_httpmetadata,
    llmresponse as components_llmresponse,
)
from livepeer.models.errors import studio_api_error as errors_studio_api_error
from livepeer.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GenLLMResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    llm_response: NotRequired[components_llmresponse.LLMResponseTypedDict]
    r"""Successful Response"""
    studio_api_error: NotRequired[errors_studio_api_error.StudioAPIError]
    r"""Error"""


class GenLLMResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    llm_response: Optional[components_llmresponse.LLMResponse] = None
    r"""Successful Response"""

    studio_api_error: Optional[errors_studio_api_error.StudioAPIError] = None
    r"""Error"""