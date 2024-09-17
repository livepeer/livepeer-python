# Generate
(*generate*)

## Overview

Operations related to AI generate api

### Available Operations

* [text_to_image](#text_to_image) - Text To Image
* [image_to_image](#image_to_image) - Image To Image
* [image_to_video](#image_to_video) - Image To Video
* [upscale](#upscale) - Upscale
* [audio_to_text](#audio_to_text) - Audio To Text
* [segment_anything2](#segment_anything2) - Segment Anything 2

## text_to_image

Generate images from text prompts.

### Example Usage

```python
from livepeer import Livepeer
from livepeer.models import operations

s = Livepeer()

res = s.generate.text_to_image(security=operations.GenTextToImageSecurity(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
), request={
    "prompt": "<value>",
})

if res.image_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.TextToImageParams](../../models/components/texttoimageparams.md)           | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GenTextToImageSecurity](../../models/operations/gentexttoimagesecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GenTextToImageResponse](../../models/operations/gentexttoimageresponse.md)**

### Errors

| Error Object                                         | Status Code                                          | Content Type                                         |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| errors.GenTextToImageResponseBody                    | 400                                                  | application/json                                     |
| errors.GenTextToImageGenerateResponseBody            | 401                                                  | application/json                                     |
| errors.GenTextToImageGenerateResponseResponseBody    | 422                                                  | application/json                                     |
| errors.GenTextToImageGenerateResponse500ResponseBody | 500                                                  | application/json                                     |
| errors.SDKError                                      | 4xx-5xx                                              | */*                                                  |


## image_to_image

Apply image transformations to a provided image.

### Example Usage

```python
from livepeer import Livepeer
from livepeer.models import operations

s = Livepeer()

res = s.generate.image_to_image(security=operations.GenImageToImageSecurity(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
), request={
    "prompt": "<value>",
    "image": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
})

if res.image_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.BodyGenImageToImage](../../models/components/bodygenimagetoimage.md)         | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GenImageToImageSecurity](../../models/operations/genimagetoimagesecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GenImageToImageResponse](../../models/operations/genimagetoimageresponse.md)**

### Errors

| Error Object                                          | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| errors.GenImageToImageResponseBody                    | 400                                                   | application/json                                      |
| errors.GenImageToImageGenerateResponseBody            | 401                                                   | application/json                                      |
| errors.GenImageToImageGenerateResponseResponseBody    | 422                                                   | application/json                                      |
| errors.GenImageToImageGenerateResponse500ResponseBody | 500                                                   | application/json                                      |
| errors.SDKError                                       | 4xx-5xx                                               | */*                                                   |


## image_to_video

Generate a video from a provided image.

### Example Usage

```python
from livepeer import Livepeer
from livepeer.models import operations

s = Livepeer()

res = s.generate.image_to_video(security=operations.GenImageToVideoSecurity(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
), request={
    "image": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
})

if res.video_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.BodyGenImageToVideo](../../models/components/bodygenimagetovideo.md)         | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GenImageToVideoSecurity](../../models/operations/genimagetovideosecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GenImageToVideoResponse](../../models/operations/genimagetovideoresponse.md)**

### Errors

| Error Object                                          | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| errors.GenImageToVideoResponseBody                    | 400                                                   | application/json                                      |
| errors.GenImageToVideoGenerateResponseBody            | 401                                                   | application/json                                      |
| errors.GenImageToVideoGenerateResponseResponseBody    | 422                                                   | application/json                                      |
| errors.GenImageToVideoGenerateResponse500ResponseBody | 500                                                   | application/json                                      |
| errors.SDKError                                       | 4xx-5xx                                               | */*                                                   |


## upscale

Upscale an image by increasing its resolution.

### Example Usage

```python
from livepeer import Livepeer
from livepeer.models import operations

s = Livepeer()

res = s.generate.upscale(security=operations.GenUpscaleSecurity(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
), request={
    "prompt": "<value>",
    "image": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
})

if res.image_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.BodyGenUpscale](../../models/components/bodygenupscale.md)         | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.GenUpscaleSecurity](../../models/operations/genupscalesecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GenUpscaleResponse](../../models/operations/genupscaleresponse.md)**

### Errors

| Error Object                                     | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| errors.GenUpscaleResponseBody                    | 400                                              | application/json                                 |
| errors.GenUpscaleGenerateResponseBody            | 401                                              | application/json                                 |
| errors.GenUpscaleGenerateResponseResponseBody    | 422                                              | application/json                                 |
| errors.GenUpscaleGenerateResponse500ResponseBody | 500                                              | application/json                                 |
| errors.SDKError                                  | 4xx-5xx                                          | */*                                              |


## audio_to_text

Transcribe audio files to text.

### Example Usage

```python
from livepeer import Livepeer
from livepeer.models import operations

s = Livepeer()

res = s.generate.audio_to_text(security=operations.GenAudioToTextSecurity(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
), request={
    "audio": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
})

if res.text_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.BodyGenAudioToText](../../models/components/bodygenaudiototext.md)         | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GenAudioToTextSecurity](../../models/operations/genaudiototextsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GenAudioToTextResponse](../../models/operations/genaudiototextresponse.md)**

### Errors

| Error Object                                         | Status Code                                          | Content Type                                         |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| errors.GenAudioToTextResponseBody                    | 400                                                  | application/json                                     |
| errors.GenAudioToTextGenerateResponseBody            | 401                                                  | application/json                                     |
| errors.GenAudioToTextGenerateResponseResponseBody    | 413                                                  | application/json                                     |
| errors.GenAudioToTextGenerateResponse422ResponseBody | 422                                                  | application/json                                     |
| errors.GenAudioToTextGenerateResponse500ResponseBody | 500                                                  | application/json                                     |
| errors.SDKError                                      | 4xx-5xx                                              | */*                                                  |


## segment_anything2

Segment objects in an image.

### Example Usage

```python
from livepeer import Livepeer
from livepeer.models import operations

s = Livepeer()

res = s.generate.segment_anything2(security=operations.GenSegmentAnything2Security(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
), request={
    "image": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
})

if res.masks_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.BodyGenSegmentAnything2](../../models/components/bodygensegmentanything2.md)         | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GenSegmentAnything2Security](../../models/operations/gensegmentanything2security.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GenSegmentAnything2Response](../../models/operations/gensegmentanything2response.md)**

### Errors

| Error Object                                              | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| errors.GenSegmentAnything2ResponseBody                    | 400                                                       | application/json                                          |
| errors.GenSegmentAnything2GenerateResponseBody            | 401                                                       | application/json                                          |
| errors.GenSegmentAnything2GenerateResponseResponseBody    | 422                                                       | application/json                                          |
| errors.GenSegmentAnything2GenerateResponse500ResponseBody | 500                                                       | application/json                                          |
| errors.SDKError                                           | 4xx-5xx                                                   | */*                                                       |
