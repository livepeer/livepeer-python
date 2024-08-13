# AccessControl
(*access_control*)

## Overview

Operations related to access control/signing keys api

### Available Operations

* [create](#create) - Create a signing key
* [get_all](#get_all) - Retrieves signing keys
* [delete](#delete) - Delete Signing Key
* [get](#get) - Retrieves a signing key
* [update](#update) - Update a signing key

## create

The publicKey is a representation of the public key, encoded as base 64 and is passed as a string, and  the privateKey is displayed only on creation. This is the only moment where the client can save the private key, otherwise it will be lost. Remember to decode your string when signing JWTs.
Up to 10 signing keys can be generated, after that you must delete at least one signing key to create a new one.


### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.access_control.create()

if res.signing_key is not None:
    # handle response
    pass

```




### Response

**[operations.CreateSigningKeyResponse](../../models/operations/createsigningkeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_all

Retrieves signing keys

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.access_control.get_all()

if res.data is not None:
    # handle response
    pass

```




### Response

**[operations.GetSigningKeysResponse](../../models/operations/getsigningkeysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete

Delete Signing Key

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.access_control.delete(key_id='<value>')

if res is not None:
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
| errors.SDKError | 4xx-5xx         | */*             |

## get

Retrieves a signing key

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.access_control.get(key_id='<value>')

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
| errors.SDKError | 4xx-5xx         | */*             |

## update

Update a signing key

### Example Usage

```python
import livepeer
from livepeer.models import operations

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.access_control.update(key_id='<value>', request_body=operations.UpdateSigningKeyRequestBody())

if res is not None:
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
| errors.SDKError | 4xx-5xx         | */*             |
