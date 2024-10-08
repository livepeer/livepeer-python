"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .ffmpeg_profile import FfmpegProfile, FfmpegProfileTypedDict
from .input_creator_id import InputCreatorID, InputCreatorIDTypedDict
from .multistream import Multistream, MultistreamTypedDict
from .playback_policy import PlaybackPolicy, PlaybackPolicyTypedDict
from .pull import Pull, PullTypedDict
from .transcode_profile import TranscodeProfile, TranscodeProfileTypedDict
from .usertags import UserTags, UserTagsTypedDict
from livepeer.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class NewStreamPayloadRecordingSpecTypedDict(TypedDict):
    profiles: NotRequired[Nullable[List[TranscodeProfileTypedDict]]]


class NewStreamPayloadRecordingSpec(BaseModel):
    profiles: OptionalNullable[List[TranscodeProfile]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["profiles"]
        nullable_fields = ["profiles"]
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


class NewStreamPayloadTypedDict(TypedDict):
    name: str
    pull: NotRequired[PullTypedDict]
    r"""Configuration for a stream that should be actively pulled from an
    external source, rather than pushed to Livepeer. If specified, the
    stream will not have a streamKey.
    """
    creator_id: NotRequired[InputCreatorIDTypedDict]
    playback_policy: NotRequired[Nullable[PlaybackPolicyTypedDict]]
    r"""Whether the playback policy for an asset or stream is public or signed"""
    profiles: NotRequired[Nullable[List[FfmpegProfileTypedDict]]]
    record: NotRequired[bool]
    r"""Should this stream be recorded? Uses default settings. For more
    customization, create and configure an object store.

    """
    recording_spec: NotRequired[NewStreamPayloadRecordingSpecTypedDict]
    multistream: NotRequired[MultistreamTypedDict]
    user_tags: NotRequired[Dict[str, UserTagsTypedDict]]
    r"""User input tags associated with the stream"""


class NewStreamPayload(BaseModel):
    name: str

    pull: Optional[Pull] = None
    r"""Configuration for a stream that should be actively pulled from an
    external source, rather than pushed to Livepeer. If specified, the
    stream will not have a streamKey.
    """

    creator_id: Annotated[
        Optional[InputCreatorID], pydantic.Field(alias="creatorId")
    ] = None

    playback_policy: Annotated[
        OptionalNullable[PlaybackPolicy], pydantic.Field(alias="playbackPolicy")
    ] = UNSET
    r"""Whether the playback policy for an asset or stream is public or signed"""

    profiles: OptionalNullable[List[FfmpegProfile]] = UNSET

    record: Optional[bool] = None
    r"""Should this stream be recorded? Uses default settings. For more
    customization, create and configure an object store.

    """

    recording_spec: Annotated[
        Optional[NewStreamPayloadRecordingSpec], pydantic.Field(alias="recordingSpec")
    ] = None

    multistream: Optional[Multistream] = None

    user_tags: Annotated[
        Optional[Dict[str, UserTags]], pydantic.Field(alias="userTags")
    ] = None
    r"""User input tags associated with the stream"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "pull",
            "creatorId",
            "playbackPolicy",
            "profiles",
            "record",
            "recordingSpec",
            "multistream",
            "userTags",
        ]
        nullable_fields = ["playbackPolicy", "profiles"]
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
