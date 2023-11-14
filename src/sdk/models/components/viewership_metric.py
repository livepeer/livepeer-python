"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ViewershipMetric:
    r"""An individual metric about viewership of an asset. Necessarily, at least
    1 of playbackId and dStorageUrl will be present, depending on the query.
    """
    playtime_mins: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playtimeMins') }})
    r"""The total playtime in minutes for the asset"""
    view_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('viewCount') }})
    r"""The number of views for the asset"""
    browser: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('browser'), 'exclude': lambda f: f is None }})
    r"""The browser used by the viewer"""
    browser_engine: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('browserEngine'), 'exclude': lambda f: f is None }})
    r"""The browser engine used by the viewer's browser"""
    continent: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('continent'), 'exclude': lambda f: f is None }})
    r"""The continent where the viewer is located"""
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""The country where the viewer is located"""
    cpu: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cpu'), 'exclude': lambda f: f is None }})
    r"""The CPU used by the viewer's device"""
    creator_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creatorId'), 'exclude': lambda f: f is None }})
    r"""The ID of the creator associated with the metric"""
    device: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('device'), 'exclude': lambda f: f is None }})
    r"""The device used by the viewer"""
    device_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deviceType'), 'exclude': lambda f: f is None }})
    r"""The type of the device used by the viewer"""
    d_storage_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dStorageUrl'), 'exclude': lambda f: f is None }})
    r"""The URL of the distributed storage used for the asset"""
    error_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorRate'), 'exclude': lambda f: f is None }})
    r"""The error rate for the asset"""
    exits_before_start: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exitsBeforeStart'), 'exclude': lambda f: f is None }})
    r"""The percentage of sessions that existed before the asset started
    playing
    """
    geohas: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('geohas'), 'exclude': lambda f: f is None }})
    r"""Geographic encoding of the viewers location. Accurate to 3 digits."""
    os: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('os'), 'exclude': lambda f: f is None }})
    r"""The operating system used by the viewer"""
    playback_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackId'), 'exclude': lambda f: f is None }})
    r"""The playback ID associated with the metric"""
    rebuffer_ratio: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rebufferRatio'), 'exclude': lambda f: f is None }})
    r"""The rebuffering ratio for the asset"""
    subdivision: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subdivision'), 'exclude': lambda f: f is None }})
    r"""The subdivision (e.g., state or province) where the viewer is
    located
    """
    timestamp: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp'), 'exclude': lambda f: f is None }})
    r"""Timestamp (in milliseconds) when the metric was recorded. If the
    query contains a time step, this timestamp will point to the
    beginning of the time step period.
    """
    timezone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timezone'), 'exclude': lambda f: f is None }})
    r"""The timezone where the viewer is located"""
    ttff_ms: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ttffMs'), 'exclude': lambda f: f is None }})
    r"""The time-to-first-frame (TTFF) in milliseconds"""
    viewer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('viewerId'), 'exclude': lambda f: f is None }})
    r"""The ID of the viewer associated with the metric"""
    

