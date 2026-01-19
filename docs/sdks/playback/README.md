# Playback

## Overview

Operations related to playback api

### Available Operations

* [get](#get) - Retrieve Playback Info

## get

Retrieve Playback Info

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlaybackInfo" method="get" path="/playback/{id}" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.playback.get(id="<id>")

    assert res.playback_info is not None

    # Handle response
    print(res.playback_info)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | The playback ID from the asset or livestream, e.g. `eaw4nk06ts2d0mzb`. |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[operations.GetPlaybackInfoResponse](../../models/operations/getplaybackinforesponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |