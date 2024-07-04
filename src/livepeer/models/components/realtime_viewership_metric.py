"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from livepeer import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RealtimeViewershipMetric:
    r"""An individual metric about realtime viewership of a stream/asset."""
    view_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('viewCount') }})
    r"""The number of views for the stream/asset."""
    error_rate: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorRate') }})
    r"""The error rate for the stream/asset."""
    playback_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackId'), 'exclude': lambda f: f is None }})
    r"""The playback ID associated with the metric."""
    device: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('device'), 'exclude': lambda f: f is None }})
    r"""The device used by the viewer."""
    browser: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('browser'), 'exclude': lambda f: f is None }})
    r"""The browser used by the viewer."""
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""The country where the viewer is located."""
    

