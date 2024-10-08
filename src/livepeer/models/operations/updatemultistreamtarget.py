"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.models.components import (
    httpmetadata as components_httpmetadata,
    multistream_target_patch_payload as components_multistream_target_patch_payload,
)
from livepeer.models.errors import error as errors_error
from livepeer.types import BaseModel
from livepeer.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateMultistreamTargetRequestTypedDict(TypedDict):
    id: str
    r"""ID of the multistream target"""
    multistream_target_patch_payload: components_multistream_target_patch_payload.MultistreamTargetPatchPayloadTypedDict


class UpdateMultistreamTargetRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the multistream target"""

    multistream_target_patch_payload: Annotated[
        components_multistream_target_patch_payload.MultistreamTargetPatchPayload,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class UpdateMultistreamTargetResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    error: NotRequired[errors_error.Error]
    r"""Error"""


class UpdateMultistreamTargetResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    error: Optional[errors_error.Error] = None
    r"""Error"""
