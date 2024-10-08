"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.models.components import (
    httpmetadata as components_httpmetadata,
    webhook_log as components_webhook_log,
)
from livepeer.models.errors import error as errors_error
from livepeer.types import BaseModel
from livepeer.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetWebhookLogRequestTypedDict(TypedDict):
    id: str
    log_id: str


class GetWebhookLogRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    log_id: Annotated[
        str,
        pydantic.Field(alias="logId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]


class GetWebhookLogResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    webhook_log: NotRequired[components_webhook_log.WebhookLogTypedDict]
    r"""Success"""
    error: NotRequired[errors_error.Error]
    r"""Error"""


class GetWebhookLogResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    webhook_log: Optional[components_webhook_log.WebhookLog] = None
    r"""Success"""

    error: Optional[errors_error.Error] = None
    r"""Error"""
