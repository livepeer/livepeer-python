"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .media import Media, MediaTypedDict
from livepeer.types import BaseModel
from typing import List, TypedDict


class VideoResponseTypedDict(TypedDict):
    r"""Response model for image generation."""

    images: List[MediaTypedDict]
    r"""The generated images."""


class VideoResponse(BaseModel):
    r"""Response model for image generation."""

    images: List[Media]
    r"""The generated images."""
