"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creator_id import CreatorID
from .ffmpeg_profile import FfmpegProfile
from .playback_policy import PlaybackPolicy
from .target_output import TargetOutput
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from livepeer import utils
from typing import Dict, List, Optional, Union


class IsMobile1(int, Enum):
    r"""0: not mobile, 1: mobile screen share, 2: mobile camera."""
    ZERO = 0
    ONE = 1
    TWO = 2


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StreamLocation:
    r"""Approximate location of the pull source. The location is used to
    determine the closest Livepeer region to pull the stream from.
    """
    lat: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lat') }})
    r"""Latitude of the pull source in degrees. North is positive,
    south is negative.
    """
    lon: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lon') }})
    r"""Longitude of the pull source in degrees. East is positive,
    west is negative.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StreamPull:
    r"""Configuration for a stream that should be actively pulled from an
    external source, rather than pushed to Livepeer. If specified, the
    stream will not have a streamKey.
    """
    source: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    r"""URL from which to pull from."""
    headers: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('headers'), 'exclude': lambda f: f is None }})
    r"""Headers to be sent with the request to the pull source."""
    is_mobile: Optional[StreamIsMobile] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isMobile'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the stream will be pulled from a mobile source."""
    location: Optional[StreamLocation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location'), 'exclude': lambda f: f is None }})
    r"""Approximate location of the pull source. The location is used to
    determine the closest Livepeer region to pull the stream from.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StreamRecordingSpec:
    r"""Configuration for recording the stream. This can only be set if
    `record` is true.
    """
    profiles: Optional[List[FfmpegProfile]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('profiles'), 'exclude': lambda f: f is None }})
    r"""Profiles to record the stream in. If not specified, the stream
    will be recorded in the same profiles as the stream itself. Keep
    in mind that the source rendition will always be recorded.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StreamMultistream:
    targets: Optional[List[TargetOutput]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('targets'), 'exclude': lambda f: f is None }})
    r"""References to targets where this stream will be simultaneously
    streamed to
    """
    



@dataclasses.dataclass
class Renditions:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Stream:
    UNSET='__SPEAKEASY_UNSET__'
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    kind: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kind'), 'exclude': lambda f: f is None }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    creator_id: Optional[CreatorID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creatorId'), 'exclude': lambda f: f is None }})
    user_tags: Optional[Dict[str, StreamUserTags]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userTags'), 'exclude': lambda f: f is None }})
    r"""User input tags associated with the stream"""
    last_seen: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastSeen'), 'exclude': lambda f: f is None }})
    source_segments: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceSegments'), 'exclude': lambda f: f is None }})
    transcoded_segments: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transcodedSegments'), 'exclude': lambda f: f is None }})
    source_segments_duration: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceSegmentsDuration'), 'exclude': lambda f: f is None }})
    r"""Duration of all the source segments, sec"""
    transcoded_segments_duration: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transcodedSegmentsDuration'), 'exclude': lambda f: f is None }})
    r"""Duration of all the transcoded segments, sec"""
    source_bytes: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceBytes'), 'exclude': lambda f: f is None }})
    transcoded_bytes: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transcodedBytes'), 'exclude': lambda f: f is None }})
    ingest_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ingestRate'), 'exclude': lambda f: f is None }})
    r"""Rate at which sourceBytes increases (bytes/second)"""
    outgoing_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outgoingRate'), 'exclude': lambda f: f is None }})
    r"""Rate at which transcodedBytes increases (bytes/second)"""
    is_active: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isActive'), 'exclude': lambda f: f is None }})
    r"""If currently active"""
    is_healthy: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isHealthy'), 'exclude': lambda f: f is Stream.UNSET }})
    r"""Indicates whether the stream is healthy or not."""
    issues: Optional[List[str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issues'), 'exclude': lambda f: f is Stream.UNSET }})
    r"""A string array of human-readable errors describing issues affecting the stream, if any."""
    created_by_token_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdByTokenName'), 'exclude': lambda f: f is None }})
    r"""Name of the token used to create this object"""
    created_at: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'exclude': lambda f: f is None }})
    r"""Timestamp (in milliseconds) at which stream object was created"""
    parent_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parentId'), 'exclude': lambda f: f is None }})
    r"""Points to parent stream object"""
    stream_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamKey'), 'exclude': lambda f: f is None }})
    r"""Used to form RTMP ingest URL"""
    pull: Optional[StreamPull] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pull'), 'exclude': lambda f: f is None }})
    r"""Configuration for a stream that should be actively pulled from an
    external source, rather than pushed to Livepeer. If specified, the
    stream will not have a streamKey.
    """
    playback_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackId'), 'exclude': lambda f: f is None }})
    r"""The playback ID to use with the Playback Info endpoint to retrieve playback URLs."""
    playback_policy: Optional[PlaybackPolicy] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playbackPolicy'), 'exclude': lambda f: f is Stream.UNSET }})
    r"""Whether the playback policy for an asset or stream is public or signed"""
    profiles: Optional[List[FfmpegProfile]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('profiles'), 'exclude': lambda f: f is None }})
    project_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projectId'), 'exclude': lambda f: f is None }})
    r"""The ID of the project"""
    record: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('record'), 'exclude': lambda f: f is None }})
    r"""Should this stream be recorded? Uses default settings. For more
    customization, create and configure an object store.
    """
    recording_spec: Optional[StreamRecordingSpec] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordingSpec'), 'exclude': lambda f: f is None }})
    r"""Configuration for recording the stream. This can only be set if
    `record` is true.
    """
    multistream: Optional[StreamMultistream] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('multistream'), 'exclude': lambda f: f is None }})
    suspended: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('suspended'), 'exclude': lambda f: f is None }})
    r"""If currently suspended"""
    last_terminated_at: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastTerminatedAt'), 'exclude': lambda f: f is Stream.UNSET }})
    r"""Timestamp (in milliseconds) when the stream was last terminated"""
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userId'), 'exclude': lambda f: f is None }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    renditions: Optional[Renditions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('renditions'), 'exclude': lambda f: f is None }})
    


Three = Union[str, float]

StreamUserTags = Union[str, float, List[Three]]

StreamIsMobile = Union[IsMobile1, bool]
