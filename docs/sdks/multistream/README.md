# Multistream
(*multistream*)

## Overview

Operations related to multistream api

### Available Operations

* [get_all](#get_all) - Retrieve Multistream Targets
* [create](#create) - Create a multistream target
* [get](#get) - Retrieve a multistream target
* [update](#update) - Update Multistream Target
* [delete](#delete) - Delete a multistream target

## get_all

Retrieve Multistream Targets

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.multistream.get_all()

if res.data is not None:
    # handle response
    pass

```


### Response

**[operations.GetMultistreamTargetsResponse](../../models/operations/getmultistreamtargetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create

Create a multistream target

### Example Usage

```python
import livepeer
from livepeer.models import components

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.multistream.create(request=components.MultistreamTargetInput(
    url='rtmps://live.my-service.tv/channel/secretKey',
))

if res.multistream_target is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.MultistreamTargetInput](../../models/components/multistreamtargetinput.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateMultistreamTargetResponse](../../models/operations/createmultistreamtargetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get

Retrieve a multistream target

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.multistream.get(id='<value>')

if res.multistream_target is not None:
    # handle response
    pass

```

### Parameters

| Parameter                    | Type                         | Required                     | Description                  |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `id`                         | *str*                        | :heavy_check_mark:           | ID of the multistream target |


### Response

**[operations.GetMultistreamTargetResponse](../../models/operations/getmultistreamtargetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update

Update Multistream Target

### Example Usage

```python
import livepeer
from livepeer.models import components

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.multistream.update(id='<value>', multistream_target_patch_payload=components.MultistreamTargetPatchPayload(
    url='rtmps://live.my-service.tv/channel/secretKey',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `id`                                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | ID of the multistream target                                                                         |
| `multistream_target_patch_payload`                                                                   | [components.MultistreamTargetPatchPayload](../../models/components/multistreamtargetpatchpayload.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |


### Response

**[operations.UpdateMultistreamTargetResponse](../../models/operations/updatemultistreamtargetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete

Make sure to remove any references to the target on existing
streams before actually deleting it from the API.


### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.multistream.delete(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                    | Type                         | Required                     | Description                  |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `id`                         | *str*                        | :heavy_check_mark:           | ID of the multistream target |


### Response

**[operations.DeleteMultistreamTargetResponse](../../models/operations/deletemultistreamtargetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
