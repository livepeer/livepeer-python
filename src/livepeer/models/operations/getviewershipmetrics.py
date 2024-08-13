"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import viewership_metric as components_viewership_metric
from ...models.errors import error as errors_error
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import List, Optional, Union


class TimeStep(str, Enum):
    r"""The time step to aggregate viewership metrics by"""
    HOUR = 'hour'
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    YEAR = 'year'


class QueryParamBreakdownBy(str, Enum):
    PLAYBACK_ID = 'playbackId'
    DEVICE_TYPE = 'deviceType'
    DEVICE = 'device'
    CPU = 'cpu'
    OS = 'os'
    BROWSER = 'browser'
    BROWSER_ENGINE = 'browserEngine'
    CONTINENT = 'continent'
    COUNTRY = 'country'
    SUBDIVISION = 'subdivision'
    TIMEZONE = 'timezone'
    GEOHASH = 'geohash'
    VIEWER_ID = 'viewerId'
    CREATOR_ID = 'creatorId'


@dataclasses.dataclass
class GetViewershipMetricsRequest:
    playback_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'playbackId', 'style': 'form', 'explode': True }})
    r"""The playback ID to filter the query results. This can be a canonical
    playback ID from Livepeer assets or streams, or dStorage identifiers
    for assets
    """
    from_: Optional[From] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'from', 'style': 'form', 'explode': True }})
    r"""Start timestamp for the query range (inclusive)"""
    to: Optional[To] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'to', 'style': 'form', 'explode': True }})
    r"""End timestamp for the query range (exclusive)"""
    time_step: Optional[TimeStep] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeStep', 'style': 'form', 'explode': True }})
    r"""The time step to aggregate viewership metrics by"""
    asset_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'assetId', 'style': 'form', 'explode': True }})
    r"""The asset ID to filter metrics for"""
    stream_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'streamId', 'style': 'form', 'explode': True }})
    r"""The stream ID to filter metrics for"""
    creator_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'creatorId', 'style': 'form', 'explode': True }})
    r"""The creator ID to filter the query results"""
    breakdown_by: Optional[List[QueryParamBreakdownBy]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'breakdownBy[]', 'style': 'form', 'explode': True }})
    r"""The list of fields to break down the query results. Specify this
    query-string multiple times to break down by multiple fields.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetViewershipMetricsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    data: Optional[List[components_viewership_metric.ViewershipMetric]] = dataclasses.field(default=None)
    r"""A list of Metric objects"""
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Error"""
    


From = Union[datetime, int]

To = Union[datetime, int]
