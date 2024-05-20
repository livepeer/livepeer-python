# Playback
(*playback*)

## Overview

Operations related to playback api

### Available Operations

* [get](#get) - Retrieve Playback Info

## get

Retrieve Playback Info

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.playback.get(id='<value>')

if res.playback_info is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | The playback ID from the asset or livestream, e.g. `eaw4nk06ts2d0mzb`. |


### Response

**[operations.GetPlaybackInfoResponse](../../models/operations/getplaybackinforesponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
