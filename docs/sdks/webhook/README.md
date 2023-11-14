# Webhook
(*webhook*)

### Available Operations

* [get_all](#get_all) - Retrieve a Webhook
* [create](#create) - Create a webhook
* [delete](#delete) - Delete a webhook
* [get](#get) - Retrieve a webhook
* [update](#update) - Update a webhook

## get_all

Retrieve a Webhook

### Example Usage

```python
import sdk

s = sdk.SDK(
    api_key="",
)


res = s.webhook.get_all()

if res.data is not None:
    # handle response
    pass
```


### Response

**[operations.GetWebhooksResponse](../../models/operations/getwebhooksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create

Create a webhook

### Example Usage

```python
import sdk

s = sdk.SDK(
    api_key="",
)


res = s.webhook.create()

if res.webhook is not None:
    # handle response
    pass
```


### Response

**[operations.CreateWebhookResponse](../../models/operations/createwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete

Delete a webhook

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.webhook.delete(id='string')

if res.webhook is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | ID of the webhook  |


### Response

**[operations.DeleteWebhookResponse](../../models/operations/deletewebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get

Retrieve a webhook

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.webhook.get(id='string')

if res.webhook is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | ID of the webhook  |


### Response

**[operations.GetWebhookResponse](../../models/operations/getwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update

Update a webhook

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.webhook.update(id='string')

if res.webhook is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | ID of the webhook  |


### Response

**[operations.UpdateWebhookResponse](../../models/operations/updatewebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
