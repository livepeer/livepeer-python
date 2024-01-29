# SigningKey
(*signing_key*)

### Available Operations

* [create](#create) - Create a signing key
* [delete](#delete) - Delete Signing Key
* [get](#get) - Retrieves a signing key
* [update](#update) - Update a signing key

## create


The publicKey is a representation of the public key, encoded as base 64 and is passed as a string, and  the privateKey is displayed only on creation. This is the only moment where the client can save the private key, otherwise it will be lost. Remember to decode your string when signing JWTs.
Up to 10 signing keys can be generated, after that you must delete at least one signing key to create a new one.


### Example Usage

```python
import sdk

s = sdk.SDK(
    api_key="",
)


res = s.signing_key.create()

if res.signing_key is not None:
    # handle response
    pass
```


### Response

**[operations.CreateSigningKeyResponse](../../models/operations/createsigningkeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete

Delete Signing Key

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.signing_key.delete(key_id='string')

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

## get

Retrieves a signing key

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.signing_key.get(key_id='string')

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

## update

Update a signing key

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.signing_key.update(key_id='string', request_body=operations.UpdateSigningKeyRequestBody())

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
