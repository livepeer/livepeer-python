"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer.models.components import (
    httpmetadata as components_httpmetadata,
    webhook as components_webhook,
)
from livepeer.models.errors import error as errors_error
from livepeer.types import BaseModel
from livepeer.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class DeleteWebhookRequestTypedDict(TypedDict):
    id: str


class DeleteWebhookRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class DeleteWebhookResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    webhook: NotRequired[components_webhook.WebhookTypedDict]
    r"""Success"""
    error: NotRequired[errors_error.Error]
    r"""Error"""


class DeleteWebhookResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    webhook: Optional[components_webhook.Webhook] = None
    r"""Success"""

    error: Optional[errors_error.Error] = None
    r"""Error"""
