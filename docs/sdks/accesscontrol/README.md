# AccessControl
(*access_control*)

### Available Operations

* [get_signing_keys](#get_signing_keys) - Retrieves signing keys
* [create_signing_key](#create_signing_key) - Create a signing key
* [delete_signing_key](#delete_signing_key) - Delete Signing Key
* [get_signing_key](#get_signing_key) - Retrieves a signing key
* [update_signing_key](#update_signing_key) - Update a signing key

## get_signing_keys

Retrieves signing keys

### Example Usage

```python
import sdk

s = sdk.SDK(
    api_key="",
)


res = s.access_control.get_signing_keys()

if res.data is not None:
    # handle response
    pass
```


### Response

**[operations.GetSigningKeysResponse](../../models/operations/getsigningkeysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_signing_key

Create a signing key

### Example Usage

```python
import sdk

s = sdk.SDK(
    api_key="",
)


res = s.access_control.create_signing_key()

if res.signing_key_response_payload is not None:
    # handle response
    pass
```


### Response

**[operations.CreateSigningKeyResponse](../../models/operations/createsigningkeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete_signing_key

Delete Signing Key

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.access_control.delete_signing_key(key_id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter             | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `key_id`              | *str*                 | :heavy_check_mark:    | ID of the signing key |


### Response

**[operations.DeleteSigningKeyResponse](../../models/operations/deletesigningkeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_signing_key

Retrieves a signing key

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.access_control.get_signing_key(key_id='string')

if res.signing_key is not None:
    # handle response
    pass
```

### Parameters

| Parameter             | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `key_id`              | *str*                 | :heavy_check_mark:    | ID of the signing key |


### Response

**[operations.GetSigningKeyResponse](../../models/operations/getsigningkeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_signing_key

Update a signing key

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.access_control.update_signing_key(key_id='string', request_body=operations.UpdateSigningKeyRequestBody())

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `key_id`                                                                                         | *str*                                                                                            | :heavy_check_mark:                                                                               | ID of the signing key                                                                            |
| `request_body`                                                                                   | [operations.UpdateSigningKeyRequestBody](../../models/operations/updatesigningkeyrequestbody.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |


### Response

**[operations.UpdateSigningKeyResponse](../../models/operations/updatesigningkeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
