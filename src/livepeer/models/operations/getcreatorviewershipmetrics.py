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


class QueryParamTimeStep(str, Enum):
    r"""The time step to aggregate viewership metrics by"""
    HOUR = 'hour'
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    YEAR = 'year'


class GetCreatorViewershipMetricsQueryParamBreakdownBy(str, Enum):
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
    VIEWER_ID = 'viewerId'


@dataclasses.dataclass
class GetCreatorViewershipMetricsRequest:
    from_: Optional[QueryParamFrom] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'from', 'style': 'form', 'explode': True }})
    r"""Start timestamp for the query range (inclusive)"""
    to: Optional[QueryParamTo] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'to', 'style': 'form', 'explode': True }})
    r"""End timestamp for the query range (exclusive)"""
    time_step: Optional[QueryParamTimeStep] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeStep', 'style': 'form', 'explode': True }})
    r"""The time step to aggregate viewership metrics by"""
    asset_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'assetId', 'style': 'form', 'explode': True }})
    r"""The asset ID to filter metrics for"""
    stream_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'streamId', 'style': 'form', 'explode': True }})
    r"""The stream ID to filter metrics for"""
    creator_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'creatorId', 'style': 'form', 'explode': True }})
    r"""The creator ID to filter the query results"""
    breakdown_by: Optional[List[GetCreatorViewershipMetricsQueryParamBreakdownBy]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'breakdownBy[]', 'style': 'form', 'explode': True }})
    r"""The list of fields to break down the query results. Specify this
    query-string multiple times to break down by multiple fields.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCreatorViewershipMetricsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    data: Optional[List[components_viewership_metric.ViewershipMetric]] = dataclasses.field(default=None)
    r"""A list of Metric objects"""
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Error"""
    


QueryParamFrom = Union[datetime, int]

QueryParamTo = Union[datetime, int]
