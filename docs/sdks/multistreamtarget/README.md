# MultistreamTarget
(*multistream_target*)

### Available Operations

* [get_all](#get_all) - Retrieve Multistream Targets
* [create](#create) - Create a multistream target
* [delete](#delete) - Delete a multistream target
* [get](#get) - Retrieve a multistream target
* [update](#update) - Update Multistream Target

## get_all

Retrieve Multistream Targets

### Example Usage

```python
import sdk

s = sdk.SDK(
    api_key="",
)


res = s.multistream_target.get_all()

if res.data is not None:
    # handle response
    pass
```


### Response

**[operations.GetMultistreamTargetsResponse](../../models/operations/getmultistreamtargetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create

Create a multistream target

### Example Usage

```python
import sdk
from sdk.models import components

s = sdk.SDK(
    api_key="",
)

req = components.MultistreamTargetInput(
    name='My Multistream Target',
    url='rtmps://live.my-service.tv/channel/secretKey',
)

res = s.multistream_target.create(req)

if res.classes is not None:
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
| errors.SDKError | 400-600         | */*             |

## delete

Delete a multistream target

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.multistream_target.delete(id='string')

if res.status_code == 200:
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
| errors.SDKError | 400-600         | */*             |

## get

Retrieve a multistream target

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.multistream_target.get(id='string')

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
| errors.SDKError | 400-600         | */*             |

## update

Update Multistream Target

### Example Usage

```python
import sdk
from sdk.models import components, operations

s = sdk.SDK(
    api_key="",
)


res = s.multistream_target.update(id='string', multistream_target_patch_payload=components.MultistreamTargetPatchPayload(
    name='My Multistream Target',
    url='rtmps://live.my-service.tv/channel/secretKey',
))

if res.status_code == 200:
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
| errors.SDKError | 400-600         | */*             |
