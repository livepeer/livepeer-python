"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import usage_metric as components_usage_metric
from ...models.errors import error as errors_error
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional


class GetUsageMetricsQueryParamTimeStep(str, Enum):
    r"""The time step to aggregate viewership metrics by"""
    HOUR = 'hour'
    DAY = 'day'


class GetUsageMetricsQueryParamBreakdownBy(str, Enum):
    CREATOR_ID = 'creatorId'


@dataclasses.dataclass
class GetUsageMetricsRequest:
    from_: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'from', 'style': 'form', 'explode': True }})
    r"""Start millis timestamp for the query range (inclusive)"""
    to: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'to', 'style': 'form', 'explode': True }})
    r"""End millis timestamp for the query range (exclusive)"""
    time_step: Optional[GetUsageMetricsQueryParamTimeStep] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeStep', 'style': 'form', 'explode': True }})
    r"""The time step to aggregate viewership metrics by"""
    creator_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'creatorId', 'style': 'form', 'explode': True }})
    r"""The creator ID to filter the query results"""
    breakdown_by: Optional[List[GetUsageMetricsQueryParamBreakdownBy]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'breakdownBy[]', 'style': 'form', 'explode': True }})
    r"""The list of fields to break down the query results. Currently the
    only supported breakdown is by `creatorId`.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUsageMetricsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    usage_metric: Optional[components_usage_metric.UsageMetric] = dataclasses.field(default=None)
    r"""A Usage Metric object"""
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Error"""
    

