# Asset
(*asset*)

### Available Operations

* [get_all](#get_all) - Retrieve assets
* [create](#create) - Upload an asset
* [create_via_url](#create_via_url) - Upload asset via URL
* [delete](#delete) - Delete an asset
* [get](#get) - Retrieves an asset
* [update](#update) - Update an asset

## get_all

Retrieve assets

### Example Usage

```python
import sdk

s = sdk.SDK(
    api_key="",
)


res = s.asset.get_all()

if res.data is not None:
    # handle response
    pass
```


### Response

**[operations.GetAssetsResponse](../../models/operations/getassetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create

Upload an asset

### Example Usage

```python
import sdk
from sdk.models import components

s = sdk.SDK(
    api_key="",
)

req = components.NewAssetPayload(
    name='filename.mp4',
    static_mp4=True,
    playback_policy=components.PlaybackPolicy(
        type=components.Type.JWT,
        webhook_id='3e02c844-d364-4d48-b401-24b2773b5d6c',
        webhook_context={
            "foo": 'string',
        },
    ),
    components.CreatorID1(
        type=components.CreatorIDType.UNVERIFIED,
        value='string',
    ),
    storage=components.NewAssetPayloadStorage(
    False,
    ),
    url='https://s3.amazonaws.com/my-bucket/path/filename.mp4',
    encryption=components.NewAssetPayloadEncryption(
        encrypted_key='string',
    ),
)

res = s.asset.create(req)

if res.data is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [components.NewAssetPayload](../../models/components/newassetpayload.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.RequestUploadResponse](../../models/operations/requestuploadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_via_url

Upload asset via URL

### Example Usage

```python
import sdk
from sdk.models import components

s = sdk.SDK(
    api_key="",
)

req = components.NewAssetPayload(
    name='filename.mp4',
    static_mp4=True,
    playback_policy=components.PlaybackPolicy(
        type=components.Type.WEBHOOK,
        webhook_id='3e02c844-d364-4d48-b401-24b2773b5d6c',
        webhook_context={
            "foo": 'string',
        },
    ),
'string',
    storage=components.NewAssetPayloadStorage(
        components.NewAssetPayload1(
            spec=components.Spec(
                nft_metadata=components.SpecNftMetadata(),
            ),
        ),
    ),
    url='https://s3.amazonaws.com/my-bucket/path/filename.mp4',
    encryption=components.NewAssetPayloadEncryption(
        encrypted_key='string',
    ),
)

res = s.asset.create_via_url(req)

if res.data is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [components.NewAssetPayload](../../models/components/newassetpayload.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.UploadAssetViaURLResponse](../../models/operations/uploadassetviaurlresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete

Delete an asset

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.asset.delete(asset_id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `asset_id`         | *str*              | :heavy_check_mark: | ID of the asset    |


### Response

**[operations.DeleteAssetResponse](../../models/operations/deleteassetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get

Retrieves an asset

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.asset.get(asset_id='string')

if res.asset is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `asset_id`         | *str*              | :heavy_check_mark: | ID of the asset    |


### Response

**[operations.GetAssetResponse](../../models/operations/getassetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update

Update an asset

### Example Usage

```python
import sdk
from sdk.models import components, operations

s = sdk.SDK(
    api_key="",
)


res = s.asset.update(asset_id='string', asset_patch_payload=components.AssetPatchPayload(
    name='filename.mp4',
'string',
    playback_policy=components.PlaybackPolicy(
        type=components.Type.PUBLIC,
        webhook_id='3e02c844-d364-4d48-b401-24b2773b5d6c',
        webhook_context={
            "foo": 'string',
        },
    ),
    storage=components.Storage(
    False,
    ),
))

if res.asset is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `asset_id`                                                                   | *str*                                                                        | :heavy_check_mark:                                                           | ID of the asset                                                              |
| `asset_patch_payload`                                                        | [components.AssetPatchPayload](../../models/components/assetpatchpayload.md) | :heavy_check_mark:                                                           | N/A                                                                          |


### Response

**[operations.PatchAssetAssetIDResponse](../../models/operations/patchassetassetidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
