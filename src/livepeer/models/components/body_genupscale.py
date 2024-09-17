"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import io
from livepeer.types import BaseModel
from livepeer.utils import FieldMetadata, MultipartFormMetadata
import pydantic
from typing import IO, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class BodyGenUpscaleImageTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, IO[bytes], io.BufferedReader]
    content_type: NotRequired[str]


class BodyGenUpscaleImage(BaseModel):
    file_name: Annotated[
        str, pydantic.Field(alias="image"), FieldMetadata(multipart=True)
    ]

    content: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader],
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(content=True)),
    ]

    content_type: Annotated[
        Optional[str],
        pydantic.Field(alias="Content-Type"),
        FieldMetadata(multipart=True),
    ] = None


class BodyGenUpscaleTypedDict(TypedDict):
    prompt: str
    r"""Text prompt(s) to guide upscaled image generation."""
    image: BodyGenUpscaleImageTypedDict
    r"""Uploaded image to modify with the pipeline."""
    model_id: NotRequired[str]
    r"""Hugging Face model ID used for upscaled image generation."""
    safety_check: NotRequired[bool]
    r"""Perform a safety check to estimate if generated images could be offensive or harmful."""
    seed: NotRequired[int]
    r"""Seed for random number generation."""
    num_inference_steps: NotRequired[int]
    r"""Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength."""


class BodyGenUpscale(BaseModel):
    prompt: Annotated[str, FieldMetadata(multipart=True)]
    r"""Text prompt(s) to guide upscaled image generation."""

    image: Annotated[
        BodyGenUpscaleImage,
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(file=True)),
    ]
    r"""Uploaded image to modify with the pipeline."""

    model_id: Annotated[Optional[str], FieldMetadata(multipart=True)] = (
        "stabilityai/stable-diffusion-x4-upscaler"
    )
    r"""Hugging Face model ID used for upscaled image generation."""

    safety_check: Annotated[Optional[bool], FieldMetadata(multipart=True)] = True
    r"""Perform a safety check to estimate if generated images could be offensive or harmful."""

    seed: Annotated[Optional[int], FieldMetadata(multipart=True)] = None
    r"""Seed for random number generation."""

    num_inference_steps: Annotated[Optional[int], FieldMetadata(multipart=True)] = 75
    r"""Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength."""