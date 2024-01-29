# SDK


## Overview

Livepeer API Reference: Welcome to the Livepeer API reference docs. Here you will find all the
endpoints exposed on the standard Livepeer API, learn how to use them and
what they return.


### Available Operations

* [get_all](#get_all) - Retrieves signing keys

## get_all

Retrieves signing keys

### Example Usage

```python
import sdk

s = sdk.SDK(
    api_key="",
)


res = s.get_all()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetSigningKeysResponse](../../models/operations/getsigningkeysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
