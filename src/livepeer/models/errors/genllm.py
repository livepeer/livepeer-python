"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httperror import HTTPErrorData
from .httpvalidationerror import HTTPValidationErrorData
from .studio_api_error import StudioAPIErrorData
from livepeer import utils
from typing import Union


GenLLMGenerateResponse500ResponseBodyUnion = Union[HTTPErrorData, StudioAPIErrorData]
r"""Internal Server Error"""


class GenLLMGenerateResponse500ResponseBody(Exception):
    r"""Internal Server Error"""

    data: GenLLMGenerateResponse500ResponseBodyUnion

    def __init__(self, data: GenLLMGenerateResponse500ResponseBodyUnion):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GenLLMGenerateResponse500ResponseBodyUnion)


GenLLMGenerateResponseResponseBodyUnion = Union[
    HTTPValidationErrorData, StudioAPIErrorData
]
r"""Validation Error"""


class GenLLMGenerateResponseResponseBody(Exception):
    r"""Validation Error"""

    data: GenLLMGenerateResponseResponseBodyUnion

    def __init__(self, data: GenLLMGenerateResponseResponseBodyUnion):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GenLLMGenerateResponseResponseBodyUnion)


GenLLMGenerateResponseBodyUnion = Union[HTTPErrorData, StudioAPIErrorData]
r"""Unauthorized"""


class GenLLMGenerateResponseBody(Exception):
    r"""Unauthorized"""

    data: GenLLMGenerateResponseBodyUnion

    def __init__(self, data: GenLLMGenerateResponseBodyUnion):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GenLLMGenerateResponseBodyUnion)


GenLLMResponseBodyUnion = Union[HTTPErrorData, StudioAPIErrorData]
r"""Bad Request"""


class GenLLMResponseBody(Exception):
    r"""Bad Request"""

    data: GenLLMResponseBodyUnion

    def __init__(self, data: GenLLMResponseBodyUnion):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GenLLMResponseBodyUnion)