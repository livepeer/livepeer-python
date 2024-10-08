"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.models.components import (
    asset as components_asset,
    httpmetadata as components_httpmetadata,
)
from livepeer.models.errors import error as errors_error
from livepeer.types import BaseModel
from livepeer.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetClipsRequestTypedDict(TypedDict):
    id: str
    r"""ID of the parent stream or playbackId of parent stream"""


class GetClipsRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the parent stream or playbackId of parent stream"""


class GetClipsResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    data: NotRequired[List[components_asset.AssetTypedDict]]
    r"""Success"""
    error: NotRequired[errors_error.Error]
    r"""Error"""


class GetClipsResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    data: Optional[List[components_asset.Asset]] = None
    r"""Success"""

    error: Optional[errors_error.Error] = None
    r"""Error"""
