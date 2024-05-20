# Transcode
(*transcode*)

## Overview

Operations related to transcode api

### Available Operations

* [create](#create) - Transcode a video

## create

`POST /transcode` transcodes a video file and uploads the results to the
specified storage service.
\
\
Transcoding is asynchronous so you will need to check the status of the
task in order to determine when transcoding is complete. The `id` field
in the response is the unique ID for the transcoding `Task`. The task
status can be queried using the [GET tasks
endpoint](https://docs.livepeer.org/reference/api/get-tasks):
\
\
When `status.phase` is `completed`,  transcoding will be complete and
the results will be stored in the storage service and the specified
output location.
\
\
The results will be available under `params.outputs.hls.path` and
`params.outputs.mp4.path` in the specified storage service.
## Input
\
This endpoint currently supports the following inputs:
- HTTP
- S3 API Compatible Service
\
\
**HTTP**
\
A public HTTP URL can be used to read a video file.
```json
{
    "url": "https://www.example.com/video.mp4"
}
```
| Name | Type   | Description                          |
| ---- | ------ | ------------------------------------ |
| url  | string | A public HTTP URL for the video file. |

Note: For IPFS HTTP gateway URLs, the API currently only supports “path
style” URLs and does not support “subdomain style” URLs. The API will
support both styles of URLs in a future update.
\
\
**S3 API Compatible Service**
\
\
S3 credentials can be used to authenticate with a S3 API compatible
service to read a video file.

```json
{
    "type": "s3",
    "endpoint": "https://gateway.storjshare.io",
    "credentials": {
        "accessKeyId": "$ACCESS_KEY_ID",
        "secretAccessKey": "$SECRET_ACCESS_KEY"
    },
    "bucket": "inbucket",
    "path": "/video/source.mp4"
}
```


## Storage
\
This endpoint currently supports the following storage services:
- S3 API Compatible Service
- Web3 Storage
\
\
**S3 API Compatible Service**
```json
{
  "type": "s3",
    "endpoint": "https://gateway.storjshare.io",
    "credentials": {
        "accessKeyId": "$ACCESS_KEY_ID",
        "secretAccessKey": "$SECRET_ACCESS_KEY"
    },
    "bucket": "mybucket"
}
```

**Web3 Storage**

```json
{
  "type": "web3.storage",
    "credentials": {
        "proof": "$UCAN_DELEGATION_PROOF",
    }
}
```



## Outputs
\
This endpoint currently supports the following output types:
- HLS
- MP4

**HLS**

```json
{
  "hls": {
        "path": "/samplevideo/hls"
    }
}
```


**MP4**

```json
{
  "mp4": {
        "path": "/samplevideo/mp4"
    }
}
```


### Example Usage

```python
import livepeer
from livepeer.models import components

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.transcode.create(request=components.TranscodePayload(
    input=components.Input1(
        url='https://s3.amazonaws.com/bucket/file.mp4',
    ),
    storage=components.Storage1(
        type=components.StorageType.S3,
        endpoint='https://gateway.storjshare.io',
        bucket='outputbucket',
        credentials=components.StorageCredentials(
            access_key_id='AKIAIOSFODNN7EXAMPLE',
            secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
        ),
    ),
    outputs=components.Outputs(
        hls=components.Hls(
            path='/samplevideo/hls',
        ),
        mp4=components.Mp4(
            path='/samplevideo/mp4',
        ),
        fmp4=components.Fmp4(
            path='/samplevideo/fmp4',
        ),
    ),
    profiles=[
        components.TranscodeProfile(
            bitrate=3000000,
            width=1280,
            name='720p',
            quality=23,
            fps=30,
            fps_den=1,
            gop='2',
            profile=components.TranscodeProfileProfile.H264_BASELINE,
            encoder=components.TranscodeProfileEncoder.H_264,
        ),
    ],
))

if res.task is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [components.TranscodePayload](../../models/components/transcodepayload.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.TranscodeVideoResponse](../../models/operations/transcodevideoresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
