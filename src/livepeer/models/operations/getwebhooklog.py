"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import webhook_log as components_webhook_log
from ...models.errors import error as errors_error
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class GetWebhookLogRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    log_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'logId', 'style': 'simple', 'explode': False }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetWebhookLogResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    webhook_log: Optional[components_webhook_log.WebhookLog] = dataclasses.field(default=None)
    r"""Success"""
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Error"""
    

