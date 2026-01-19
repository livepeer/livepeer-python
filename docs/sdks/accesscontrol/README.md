# AccessControl

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

<!-- UsageSnippet language="python" operationID="createSigningKey" method="post" path="/access-control/signing-key" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.access_control.create()

    assert res.signing_key is not None

    # Handle response
    print(res.signing_key)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateSigningKeyResponse](../../models/operations/createsigningkeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_all

Retrieves signing keys

### Example Usage

<!-- UsageSnippet language="python" operationID="getSigningKeys" method="get" path="/access-control/signing-key" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.access_control.get_all()

    assert res.data is not None

    # Handle response
    print(res.data)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetSigningKeysResponse](../../models/operations/getsigningkeysresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Delete Signing Key

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSigningKey" method="delete" path="/access-control/signing-key/{keyId}" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.access_control.delete(key_id="<id>")

    assert res.error is not None

    # Handle response
    print(res.error)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `key_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the signing key                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DeleteSigningKeyResponse](../../models/operations/deletesigningkeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Retrieves a signing key

### Example Usage

<!-- UsageSnippet language="python" operationID="getSigningKey" method="get" path="/access-control/signing-key/{keyId}" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.access_control.get(key_id="<id>")

    assert res.signing_key is not None

    # Handle response
    print(res.signing_key)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `key_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the signing key                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetSigningKeyResponse](../../models/operations/getsigningkeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Update a signing key

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSigningKey" method="patch" path="/access-control/signing-key/{keyId}" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.access_control.update(key_id="<id>", request_body={})

    assert res.error is not None

    # Handle response
    print(res.error)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `key_id`                                                                                         | *str*                                                                                            | :heavy_check_mark:                                                                               | ID of the signing key                                                                            |
| `request_body`                                                                                   | [operations.UpdateSigningKeyRequestBody](../../models/operations/updatesigningkeyrequestbody.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateSigningKeyResponse](../../models/operations/updatesigningkeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |