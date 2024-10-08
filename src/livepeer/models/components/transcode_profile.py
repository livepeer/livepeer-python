"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from livepeer.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class TranscodeProfileProfile(str, Enum):
    H264_BASELINE = "H264Baseline"
    H264_MAIN = "H264Main"
    H264_HIGH = "H264High"
    H264_CONSTRAINED_HIGH = "H264ConstrainedHigh"


class TranscodeProfileEncoder(str, Enum):
    H_264 = "H.264"
    HEVC = "HEVC"
    VP8 = "VP8"
    VP9 = "VP9"


class TranscodeProfileTypedDict(TypedDict):
    r"""Transcode API profile"""

    bitrate: int
    width: NotRequired[int]
    name: NotRequired[str]
    height: NotRequired[int]
    quality: NotRequired[int]
    r"""Restricts the size of the output video using the constant quality feature. Increasing this value will result in a lower quality video. Note that this parameter might not work if the transcoder lacks support for it.

    """
    fps: NotRequired[int]
    fps_den: NotRequired[int]
    gop: NotRequired[str]
    profile: NotRequired[TranscodeProfileProfile]
    encoder: NotRequired[TranscodeProfileEncoder]


class TranscodeProfile(BaseModel):
    r"""Transcode API profile"""

    bitrate: int

    width: Optional[int] = None

    name: Optional[str] = None

    height: Optional[int] = None

    quality: Optional[int] = None
    r"""Restricts the size of the output video using the constant quality feature. Increasing this value will result in a lower quality video. Note that this parameter might not work if the transcoder lacks support for it.

    """

    fps: Optional[int] = None

    fps_den: Annotated[Optional[int], pydantic.Field(alias="fpsDen")] = None

    gop: Optional[str] = None

    profile: Optional[TranscodeProfileProfile] = None

    encoder: Optional[TranscodeProfileEncoder] = None
