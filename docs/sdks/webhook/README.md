# Webhook
(*webhook*)

## Overview

Operations related to webhook api

### Available Operations

* [get_all](#get_all) - Retrieve a Webhook
* [create](#create) - Create a webhook
* [get](#get) - Retrieve a webhook
* [update](#update) - Update a webhook
* [delete](#delete) - Delete a webhook
* [get_logs](#get_logs) - Retrieve webhook logs
* [get_log](#get_log) - Retrieve a webhook log
* [resend_log](#resend_log) - Resend a webhook

## get_all

Retrieve a Webhook

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
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
| errors.SDKError | 4xx-5xx         | */*             |

## create

To create a new webhook, you need to make an API call with the events you want to listen for and the URL that will be called when those events occur.


### Example Usage

```python
import livepeer
from livepeer.models import components

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.webhook.create(request=components.WebhookInput(
    name='test_webhook',
    url='https://my-service.com/webhook',
    project_id='aac12556-4d65-4d34-9fb6-d1f0985eb0a9',
    events=[
        components.Events.STREAM_STARTED,
        components.Events.STREAM_IDLE,
    ],
    shared_secret='my-secret',
    stream_id='de7818e7-610a-4057-8f6f-b785dc1e6f88',
))

if res.webhook is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [components.WebhookInput](../../models/components/webhookinput.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.CreateWebhookResponse](../../models/operations/createwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get

Retrieve a webhook

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.webhook.get(id='<value>')

if res.webhook is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetWebhookResponse](../../models/operations/getwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update

Update a webhook

### Example Usage

```python
import livepeer
from livepeer.models import components

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.webhook.update(id='<value>', webhook=components.WebhookInput(
    name='test_webhook',
    url='https://my-service.com/webhook',
    project_id='aac12556-4d65-4d34-9fb6-d1f0985eb0a9',
    events=[
        components.Events.STREAM_STARTED,
        components.Events.STREAM_IDLE,
    ],
    shared_secret='my-secret',
    stream_id='de7818e7-610a-4057-8f6f-b785dc1e6f88',
))

if res.webhook is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `webhook`                                                          | [components.WebhookInput](../../models/components/webhookinput.md) | :heavy_check_mark:                                                 | N/A                                                                |


### Response

**[operations.UpdateWebhookResponse](../../models/operations/updatewebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete

Delete a webhook

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.webhook.delete(id='<value>')

if res.webhook is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteWebhookResponse](../../models/operations/deletewebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_logs

Retrieve webhook logs

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.webhook.get_logs(id='<value>')

if res.data is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetWebhookLogsResponse](../../models/operations/getwebhooklogsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_log

Retrieve a webhook log

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.webhook.get_log(id='<value>', log_id='<value>')

if res.webhook_log is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `log_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetWebhookLogResponse](../../models/operations/getwebhooklogresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## resend_log

Use this API to resend the same webhook request. This is useful when
developing and debugging, allowing you to easily repeat the same webhook
to check or fix the behaviour in your handler.


### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.webhook.resend_log(id='<value>', log_id='<value>')

if res.webhook_log is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `log_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.ResendWebhookResponse](../../models/operations/resendwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
