"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.models.components import httpmetadata as components_httpmetadata
from livepeer.models.errors import error as errors_error
from livepeer.types import BaseModel
from livepeer.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class DeleteAssetRequestTypedDict(TypedDict):
    asset_id: str
    r"""ID of the asset"""


class DeleteAssetRequest(BaseModel):
    asset_id: Annotated[
        str,
        pydantic.Field(alias="assetId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the asset"""


class DeleteAssetResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    error: NotRequired[errors_error.Error]
    r"""Error"""


class DeleteAssetResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    error: Optional[errors_error.Error] = None
    r"""Error"""
