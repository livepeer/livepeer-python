"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import io
from livepeer.types import BaseModel
from livepeer.utils import FieldMetadata, MultipartFormMetadata
import pydantic
from typing import IO, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class ImageTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, IO[bytes], io.BufferedReader]
    content_type: NotRequired[str]


class Image(BaseModel):
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


class BodyGenImageToImageTypedDict(TypedDict):
    prompt: str
    r"""Text prompt(s) to guide image generation."""
    image: ImageTypedDict
    r"""Uploaded image to modify with the pipeline."""
    model_id: NotRequired[str]
    r"""Hugging Face model ID used for image generation."""
    strength: NotRequired[float]
    r"""Degree of transformation applied to the reference image (0 to 1)."""
    guidance_scale: NotRequired[float]
    r"""Encourages model to generate images closely linked to the text prompt (higher values may reduce image quality)."""
    image_guidance_scale: NotRequired[float]
    r"""Degree to which the generated image is pushed towards the initial image."""
    negative_prompt: NotRequired[str]
    r"""Text prompt(s) to guide what to exclude from image generation. Ignored if guidance_scale < 1."""
    safety_check: NotRequired[bool]
    r"""Perform a safety check to estimate if generated images could be offensive or harmful."""
    seed: NotRequired[int]
    r"""Seed for random number generation."""
    num_inference_steps: NotRequired[int]
    r"""Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength."""
    num_images_per_prompt: NotRequired[int]
    r"""Number of images to generate per prompt."""


class BodyGenImageToImage(BaseModel):
    prompt: Annotated[str, FieldMetadata(multipart=True)]
    r"""Text prompt(s) to guide image generation."""

    image: Annotated[
        Image,
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(file=True)),
    ]
    r"""Uploaded image to modify with the pipeline."""

    model_id: Annotated[Optional[str], FieldMetadata(multipart=True)] = (
        "timbrooks/instruct-pix2pix"
    )
    r"""Hugging Face model ID used for image generation."""

    strength: Annotated[Optional[float], FieldMetadata(multipart=True)] = 0.8
    r"""Degree of transformation applied to the reference image (0 to 1)."""

    guidance_scale: Annotated[Optional[float], FieldMetadata(multipart=True)] = 7.5
    r"""Encourages model to generate images closely linked to the text prompt (higher values may reduce image quality)."""

    image_guidance_scale: Annotated[Optional[float], FieldMetadata(multipart=True)] = (
        1.5
    )
    r"""Degree to which the generated image is pushed towards the initial image."""

    negative_prompt: Annotated[Optional[str], FieldMetadata(multipart=True)] = ""
    r"""Text prompt(s) to guide what to exclude from image generation. Ignored if guidance_scale < 1."""

    safety_check: Annotated[Optional[bool], FieldMetadata(multipart=True)] = True
    r"""Perform a safety check to estimate if generated images could be offensive or harmful."""

    seed: Annotated[Optional[int], FieldMetadata(multipart=True)] = None
    r"""Seed for random number generation."""

    num_inference_steps: Annotated[Optional[int], FieldMetadata(multipart=True)] = 100
    r"""Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength."""

    num_images_per_prompt: Annotated[Optional[int], FieldMetadata(multipart=True)] = 1
    r"""Number of images to generate per prompt."""