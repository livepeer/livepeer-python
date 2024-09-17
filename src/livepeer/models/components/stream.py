"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .creator_id import CreatorID, CreatorIDTypedDict
from .ffmpeg_profile import FfmpegProfile, FfmpegProfileTypedDict
from .playback_policy import PlaybackPolicy, PlaybackPolicyTypedDict
from .target_output import TargetOutput, TargetOutputTypedDict
from .transcode_profile import TranscodeProfile, TranscodeProfileTypedDict
from enum import Enum
from livepeer.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


ThreeTypedDict = Union[str, float]


Three = Union[str, float]


StreamUserTagsTypedDict = Union[str, float, List[ThreeTypedDict]]


StreamUserTags = Union[str, float, List[Three]]


class IsMobile1(int, Enum):
    r"""0: not mobile, 1: mobile screen share, 2: mobile camera."""

    ZERO = 0
    ONE = 1
    TWO = 2


StreamIsMobileTypedDict = Union[IsMobile1, bool]
r"""Indicates whether the stream will be pulled from a mobile source."""


StreamIsMobile = Union[IsMobile1, bool]
r"""Indicates whether the stream will be pulled from a mobile source."""


class StreamLocationTypedDict(TypedDict):
    r"""Approximate location of the pull source. The location is used to
    determine the closest Livepeer region to pull the stream from.
    """

    lat: float
    r"""Latitude of the pull source in degrees. North is positive,
    south is negative.
    """
    lon: float
    r"""Longitude of the pull source in degrees. East is positive,
    west is negative.
    """


class StreamLocation(BaseModel):
    r"""Approximate location of the pull source. The location is used to
    determine the closest Livepeer region to pull the stream from.
    """

    lat: float
    r"""Latitude of the pull source in degrees. North is positive,
    south is negative.
    """

    lon: float
    r"""Longitude of the pull source in degrees. East is positive,
    west is negative.
    """


class StreamPullTypedDict(TypedDict):
    r"""Configuration for a stream that should be actively pulled from an
    external source, rather than pushed to Livepeer. If specified, the
    stream will not have a streamKey.
    """

    source: str
    r"""URL from which to pull from."""
    headers: NotRequired[Dict[str, str]]
    r"""Headers to be sent with the request to the pull source."""
    is_mobile: NotRequired[StreamIsMobileTypedDict]
    r"""Indicates whether the stream will be pulled from a mobile source."""
    location: NotRequired[StreamLocationTypedDict]
    r"""Approximate location of the pull source. The location is used to
    determine the closest Livepeer region to pull the stream from.
    """


class StreamPull(BaseModel):
    r"""Configuration for a stream that should be actively pulled from an
    external source, rather than pushed to Livepeer. If specified, the
    stream will not have a streamKey.
    """

    source: str
    r"""URL from which to pull from."""

    headers: Optional[Dict[str, str]] = None
    r"""Headers to be sent with the request to the pull source."""

    is_mobile: Annotated[Optional[StreamIsMobile], pydantic.Field(alias="isMobile")] = (
        None
    )
    r"""Indicates whether the stream will be pulled from a mobile source."""

    location: Optional[StreamLocation] = None
    r"""Approximate location of the pull source. The location is used to
    determine the closest Livepeer region to pull the stream from.
    """


class StreamRecordingSpecTypedDict(TypedDict):
    r"""Configuration for recording the stream. This can only be set if
    `record` is true.

    """

    profiles: NotRequired[List[TranscodeProfileTypedDict]]
    r"""Profiles to process the recording of this stream into. If not
    specified, default profiles will be derived based on the stream
    input. Keep in mind that the source rendition is always kept.

    """


class StreamRecordingSpec(BaseModel):
    r"""Configuration for recording the stream. This can only be set if
    `record` is true.

    """

    profiles: Optional[List[TranscodeProfile]] = None
    r"""Profiles to process the recording of this stream into. If not
    specified, default profiles will be derived based on the stream
    input. Keep in mind that the source rendition is always kept.

    """


class StreamMultistreamTypedDict(TypedDict):
    targets: NotRequired[List[TargetOutputTypedDict]]
    r"""References to targets where this stream will be simultaneously
    streamed to

    """


class StreamMultistream(BaseModel):
    targets: Optional[List[TargetOutput]] = None
    r"""References to targets where this stream will be simultaneously
    streamed to

    """


class RenditionsTypedDict(TypedDict):
    pass


class Renditions(BaseModel):
    pass


class StreamTypedDict(TypedDict):
    name: str
    id: NotRequired[str]
    kind: NotRequired[str]
    creator_id: NotRequired[CreatorIDTypedDict]
    user_tags: NotRequired[Dict[str, StreamUserTagsTypedDict]]
    r"""User input tags associated with the stream"""
    last_seen: NotRequired[float]
    source_segments: NotRequired[float]
    transcoded_segments: NotRequired[float]
    source_segments_duration: NotRequired[float]
    r"""Duration of all the source segments, sec"""
    transcoded_segments_duration: NotRequired[float]
    r"""Duration of all the transcoded segments, sec"""
    source_bytes: NotRequired[float]
    transcoded_bytes: NotRequired[float]
    ingest_rate: NotRequired[float]
    r"""Rate at which sourceBytes increases (bytes/second)"""
    outgoing_rate: NotRequired[float]
    r"""Rate at which transcodedBytes increases (bytes/second)"""
    is_active: NotRequired[bool]
    r"""If currently active"""
    is_healthy: NotRequired[Nullable[bool]]
    r"""Indicates whether the stream is healthy or not."""
    issues: NotRequired[Nullable[List[str]]]
    r"""A string array of human-readable errors describing issues affecting the stream, if any."""
    created_by_token_name: NotRequired[str]
    r"""Name of the token used to create this object"""
    created_at: NotRequired[float]
    r"""Timestamp (in milliseconds) at which stream object was created"""
    parent_id: NotRequired[str]
    r"""Points to parent stream object"""
    stream_key: NotRequired[str]
    r"""Used to form RTMP ingest URL"""
    pull: NotRequired[StreamPullTypedDict]
    r"""Configuration for a stream that should be actively pulled from an
    external source, rather than pushed to Livepeer. If specified, the
    stream will not have a streamKey.
    """
    playback_id: NotRequired[str]
    r"""The playback ID to use with the Playback Info endpoint to retrieve playback URLs."""
    playback_policy: NotRequired[Nullable[PlaybackPolicyTypedDict]]
    r"""Whether the playback policy for an asset or stream is public or signed"""
    profiles: NotRequired[List[FfmpegProfileTypedDict]]
    r"""Profiles to transcode the stream into. If not specified, a default
    set of profiles will be used with 240p, 360p, 480p and 720p
    resolutions. Keep in mind that the source rendition is always kept.

    """
    project_id: NotRequired[str]
    r"""The ID of the project"""
    record: NotRequired[bool]
    r"""Should this stream be recorded? Uses default settings. For more
    customization, create and configure an object store.

    """
    recording_spec: NotRequired[StreamRecordingSpecTypedDict]
    r"""Configuration for recording the stream. This can only be set if
    `record` is true.

    """
    multistream: NotRequired[StreamMultistreamTypedDict]
    suspended: NotRequired[bool]
    r"""If currently suspended"""
    last_terminated_at: NotRequired[Nullable[float]]
    r"""Timestamp (in milliseconds) when the stream was last terminated"""
    user_id: NotRequired[str]
    renditions: NotRequired[RenditionsTypedDict]


class Stream(BaseModel):
    name: str

    id: Optional[str] = None

    kind: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None

    creator_id: Annotated[Optional[CreatorID], pydantic.Field(alias="creatorId")] = None

    user_tags: Annotated[
        Optional[Dict[str, StreamUserTags]], pydantic.Field(alias="userTags")
    ] = None
    r"""User input tags associated with the stream"""

    last_seen: Annotated[Optional[float], pydantic.Field(alias="lastSeen")] = None

    source_segments: Annotated[
        Optional[float], pydantic.Field(alias="sourceSegments")
    ] = None

    transcoded_segments: Annotated[
        Optional[float], pydantic.Field(alias="transcodedSegments")
    ] = None

    source_segments_duration: Annotated[
        Optional[float], pydantic.Field(alias="sourceSegmentsDuration")
    ] = None
    r"""Duration of all the source segments, sec"""

    transcoded_segments_duration: Annotated[
        Optional[float], pydantic.Field(alias="transcodedSegmentsDuration")
    ] = None
    r"""Duration of all the transcoded segments, sec"""

    source_bytes: Annotated[Optional[float], pydantic.Field(alias="sourceBytes")] = None

    transcoded_bytes: Annotated[
        Optional[float], pydantic.Field(alias="transcodedBytes")
    ] = None

    ingest_rate: Annotated[Optional[float], pydantic.Field(alias="ingestRate")] = None
    r"""Rate at which sourceBytes increases (bytes/second)"""

    outgoing_rate: Annotated[Optional[float], pydantic.Field(alias="outgoingRate")] = (
        None
    )
    r"""Rate at which transcodedBytes increases (bytes/second)"""

    is_active: Annotated[Optional[bool], pydantic.Field(alias="isActive")] = None
    r"""If currently active"""

    is_healthy: Annotated[OptionalNullable[bool], pydantic.Field(alias="isHealthy")] = (
        UNSET
    )
    r"""Indicates whether the stream is healthy or not."""

    issues: OptionalNullable[List[str]] = UNSET
    r"""A string array of human-readable errors describing issues affecting the stream, if any."""

    created_by_token_name: Annotated[
        Optional[str], pydantic.Field(alias="createdByTokenName")
    ] = None
    r"""Name of the token used to create this object"""

    created_at: Annotated[Optional[float], pydantic.Field(alias="createdAt")] = None
    r"""Timestamp (in milliseconds) at which stream object was created"""

    parent_id: Annotated[Optional[str], pydantic.Field(alias="parentId")] = None
    r"""Points to parent stream object"""

    stream_key: Annotated[Optional[str], pydantic.Field(alias="streamKey")] = None
    r"""Used to form RTMP ingest URL"""

    pull: Optional[StreamPull] = None
    r"""Configuration for a stream that should be actively pulled from an
    external source, rather than pushed to Livepeer. If specified, the
    stream will not have a streamKey.
    """

    playback_id: Annotated[Optional[str], pydantic.Field(alias="playbackId")] = None
    r"""The playback ID to use with the Playback Info endpoint to retrieve playback URLs."""

    playback_policy: Annotated[
        OptionalNullable[PlaybackPolicy], pydantic.Field(alias="playbackPolicy")
    ] = UNSET
    r"""Whether the playback policy for an asset or stream is public or signed"""

    profiles: Optional[List[FfmpegProfile]] = None
    r"""Profiles to transcode the stream into. If not specified, a default
    set of profiles will be used with 240p, 360p, 480p and 720p
    resolutions. Keep in mind that the source rendition is always kept.

    """

    project_id: Annotated[Optional[str], pydantic.Field(alias="projectId")] = None
    r"""The ID of the project"""

    record: Optional[bool] = None
    r"""Should this stream be recorded? Uses default settings. For more
    customization, create and configure an object store.

    """

    recording_spec: Annotated[
        Optional[StreamRecordingSpec], pydantic.Field(alias="recordingSpec")
    ] = None
    r"""Configuration for recording the stream. This can only be set if
    `record` is true.

    """

    multistream: Optional[StreamMultistream] = None

    suspended: Optional[bool] = None
    r"""If currently suspended"""

    last_terminated_at: Annotated[
        OptionalNullable[float], pydantic.Field(alias="lastTerminatedAt")
    ] = UNSET
    r"""Timestamp (in milliseconds) when the stream was last terminated"""

    user_id: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="userId",
        ),
    ] = None

    renditions: Optional[Renditions] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "kind",
            "creatorId",
            "userTags",
            "lastSeen",
            "sourceSegments",
            "transcodedSegments",
            "sourceSegmentsDuration",
            "transcodedSegmentsDuration",
            "sourceBytes",
            "transcodedBytes",
            "ingestRate",
            "outgoingRate",
            "isActive",
            "isHealthy",
            "issues",
            "createdByTokenName",
            "createdAt",
            "parentId",
            "streamKey",
            "pull",
            "playbackId",
            "playbackPolicy",
            "profiles",
            "projectId",
            "record",
            "recordingSpec",
            "multistream",
            "suspended",
            "lastTerminatedAt",
            "userId",
            "renditions",
        ]
        nullable_fields = ["isHealthy", "issues", "playbackPolicy", "lastTerminatedAt"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
