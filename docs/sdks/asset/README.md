# Asset
(*asset*)

## Overview

Operations related to asset/vod api

### Available Operations

* [get_all](#get_all) - Retrieve assets
* [create](#create) - Upload an asset
* [create_via_url](#create_via_url) - Upload asset via URL
* [get](#get) - Retrieves an asset
* [update](#update) - Patch an asset
* [delete](#delete) - Delete an asset

## get_all

Retrieve assets

### Example Usage

```python
from livepeer import Livepeer

with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.asset.get_all()

    assert res.data is not None

    # Handle response
    print(res.data)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetAssetsResponse](../../models/operations/getassetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

To upload an asset, your first need to request for a direct upload URL
and only then actually upload the contents of the asset.
\
\
Once you created a upload link, you have 2 options, resumable or direct
upload. For a more reliable experience, you should use resumable uploads
which will work better for users with unreliable or slow network
connections. If you want a simpler implementation though, you should
just use a direct upload.


## Direct Upload
For a direct upload, make a PUT request to the URL received in the url
field of the response above, with the raw video file as the request
body. response above:


## Resumable Upload
Livepeer supports resumable uploads via Tus. This section provides a
simple example of how to use tus-js-client to upload a video file.
\
\
From the previous section, we generated a URL to upload a video file to
Livepeer on POST /api/asset/request-upload. You should use the
tusEndpoint field of the response to upload the video file and track the
progress:

```
# This assumes there is an `input` element of `type="file"` with id
`fileInput` in the HTML


const input = document.getElementById('fileInput');

const file = input.files[0];

const upload = new tus.Upload(file, {
  endpoint: tusEndpoint, // URL from `tusEndpoint` field in the
`/request-upload` response
  metadata: {
    filename,
    filetype: 'video/mp4',
  },
  uploadSize: file.size,
  onError(err) {
    console.error('Error uploading file:', err);
  },
  onProgress(bytesUploaded, bytesTotal) {
    const percentage = ((bytesUploaded / bytesTotal) * 100).toFixed(2);
    console.log('Uploaded ' + percentage + '%');
  },
  onSuccess() {
    console.log('Upload finished:', upload.url);
  },
});

const previousUploads = await upload.findPreviousUploads();

if (previousUploads.length > 0) {
  upload.resumeFromPreviousUpload(previousUploads[0]);
}

upload.start();

```

> Note: If you are using tus from node.js, you need to add a custom URL
storage to enable resuming from previous uploads. On the browser, this
is enabled by default using local storage. In node.js, add urlStorage:
new tus.FileUrlStorage("path/to/tmp/file"), to the UploadFile object
definition above.


### Example Usage

```python
from livepeer import Livepeer
from livepeer.models import components

with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.asset.create(request={
        "name": "filename.mp4",
        "static_mp4": True,
        "playback_policy": {
            "type": components.Type.WEBHOOK,
            "webhook_id": "1bde4o2i6xycudoy",
            "webhook_context": {
                "streamerId": "my-custom-id",
            },
            "refresh_interval": 600,
        },
        "profiles": [
            {
                "bitrate": 3000000,
                "width": 1280,
                "name": "720p",
                "height": 720,
                "quality": 23,
                "fps": 30,
                "fps_den": 1,
                "gop": "2",
                "profile": components.TranscodeProfileProfile.H264_BASELINE,
                "encoder": components.TranscodeProfileEncoder.H_264,
            },
            {
                "bitrate": 3000000,
                "width": 1280,
                "name": "720p",
                "height": 720,
                "quality": 23,
                "fps": 30,
                "fps_den": 1,
                "gop": "2",
                "profile": components.TranscodeProfileProfile.H264_BASELINE,
                "encoder": components.TranscodeProfileEncoder.H_264,
            },
        ],
    })

    assert res.data is not None

    # Handle response
    print(res.data)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [components.NewAssetPayload](../../models/components/newassetpayload.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.RequestUploadResponse](../../models/operations/requestuploadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_via_url

Upload asset via URL

### Example Usage

```python
from livepeer import Livepeer
from livepeer.models import components

with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.asset.create_via_url(request={
        "name": "filename.mp4",
        "url": "https://s3.amazonaws.com/my-bucket/path/filename.mp4",
        "static_mp4": True,
        "playback_policy": {
            "type": components.Type.WEBHOOK,
            "webhook_id": "1bde4o2i6xycudoy",
            "webhook_context": {
                "streamerId": "my-custom-id",
            },
            "refresh_interval": 600,
        },
        "profiles": [
            {
                "bitrate": 3000000,
                "width": 1280,
                "name": "720p",
                "height": 720,
                "quality": 23,
                "fps": 30,
                "fps_den": 1,
                "gop": "2",
                "profile": components.TranscodeProfileProfile.H264_BASELINE,
                "encoder": components.TranscodeProfileEncoder.H_264,
            },
            {
                "bitrate": 3000000,
                "width": 1280,
                "name": "720p",
                "height": 720,
                "quality": 23,
                "fps": 30,
                "fps_den": 1,
                "gop": "2",
                "profile": components.TranscodeProfileProfile.H264_BASELINE,
                "encoder": components.TranscodeProfileEncoder.H_264,
            },
        ],
    })

    assert res.two_hundred_application_json_data is not None

    # Handle response
    print(res.two_hundred_application_json_data)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.NewAssetFromURLPayload](../../models/components/newassetfromurlpayload.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UploadAssetResponse](../../models/operations/uploadassetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Retrieves an asset

### Example Usage

```python
from livepeer import Livepeer

with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.asset.get(asset_id="<id>")

    assert res.asset is not None

    # Handle response
    print(res.asset)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `asset_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the asset                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetAssetResponse](../../models/operations/getassetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Patch an asset

### Example Usage

```python
from livepeer import Livepeer
from livepeer.models import components

with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.asset.update(asset_id="<id>", asset_patch_payload={
        "name": "filename.mp4",
        "playback_policy": {
            "type": components.Type.WEBHOOK,
            "webhook_id": "1bde4o2i6xycudoy",
            "webhook_context": {
                "streamerId": "my-custom-id",
            },
            "refresh_interval": 600,
        },
    })

    assert res.asset is not None

    # Handle response
    print(res.asset)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `asset_id`                                                                   | *str*                                                                        | :heavy_check_mark:                                                           | ID of the asset                                                              |
| `asset_patch_payload`                                                        | [components.AssetPatchPayload](../../models/components/assetpatchpayload.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.UpdateAssetResponse](../../models/operations/updateassetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Delete an asset

### Example Usage

```python
from livepeer import Livepeer

with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.asset.delete(asset_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `asset_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the asset                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DeleteAssetResponse](../../models/operations/deleteassetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |