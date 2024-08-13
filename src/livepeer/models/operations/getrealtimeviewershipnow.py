"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import realtime_viewership_metric as components_realtime_viewership_metric
from ...models.errors import error as errors_error
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional


class BreakdownBy(str, Enum):
    PLAYBACK_ID = 'playbackId'
    DEVICE = 'device'
    BROWSER = 'browser'
    COUNTRY = 'country'


@dataclasses.dataclass
class GetRealtimeViewershipNowRequest:
    playback_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'playbackId', 'style': 'form', 'explode': True }})
    r"""The playback ID to filter the query results. This can be a canonical
    playback ID from Livepeer assets or streams, or dStorage identifiers
    for assets
    """
    creator_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'creatorId', 'style': 'form', 'explode': True }})
    r"""The creator ID to filter the query results"""
    breakdown_by: Optional[List[BreakdownBy]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'breakdownBy[]', 'style': 'form', 'explode': True }})
    r"""The list of fields to break down the query results. Specify this
    query-string multiple times to break down by multiple fields.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetRealtimeViewershipNowResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    data: Optional[List[components_realtime_viewership_metric.RealtimeViewershipMetric]] = dataclasses.field(default=None)
    r"""A list of Metric objects"""
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Error"""
    

