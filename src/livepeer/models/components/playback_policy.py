"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from livepeer import utils
from typing import Any, Dict, List, Optional


class Type(str, Enum):
    PUBLIC = 'public'
    JWT = 'jwt'
    WEBHOOK = 'webhook'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PlaybackPolicy:
    r"""Whether the playback policy for an asset or stream is public or signed"""
    type: Type = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    webhook_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhookId'), 'exclude': lambda f: f is None }})
    r"""ID of the webhook to use for playback policy"""
    webhook_context: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhookContext'), 'exclude': lambda f: f is None }})
    r"""User-defined webhook context"""
    refresh_interval: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refreshInterval'), 'exclude': lambda f: f is None }})
    r"""Interval (in seconds) at which the playback policy should be
    refreshed (default 600 seconds)
    """
    allowed_origins: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowedOrigins'), 'exclude': lambda f: f is None }})
    r"""List of allowed origins for CORS playback (<scheme>://<hostname>:<port>, <scheme>://<hostname>)"""
    

