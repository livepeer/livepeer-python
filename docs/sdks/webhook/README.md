# Webhook

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

<!-- UsageSnippet language="python" operationID="getWebhooks" method="get" path="/webhook" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.webhook.get_all()

    assert res.data is not None

    # Handle response
    print(res.data)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetWebhooksResponse](../../models/operations/getwebhooksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

To create a new webhook, you need to make an API call with the events you want to listen for and the URL that will be called when those events occur.


### Example Usage

<!-- UsageSnippet language="python" operationID="createWebhook" method="post" path="/webhook" -->
```python
from livepeer import Livepeer
from livepeer.models import components


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.webhook.create(request={
        "name": "test_webhook",
        "project_id": "aac12556-4d65-4d34-9fb6-d1f0985eb0a9",
        "events": [
            components.Events.STREAM_STARTED,
            components.Events.STREAM_IDLE,
        ],
        "url": "https://my-service.com/webhook",
        "shared_secret": "my-secret",
        "stream_id": "de7818e7-610a-4057-8f6f-b785dc1e6f88",
    })

    assert res.webhook is not None

    # Handle response
    print(res.webhook)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [components.WebhookInput](../../models/components/webhookinput.md)  | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateWebhookResponse](../../models/operations/createwebhookresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a webhook

### Example Usage

<!-- UsageSnippet language="python" operationID="getWebhook" method="get" path="/webhook/{id}" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.webhook.get(id="<id>")

    assert res.webhook is not None

    # Handle response
    print(res.webhook)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetWebhookResponse](../../models/operations/getwebhookresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Update a webhook

### Example Usage

<!-- UsageSnippet language="python" operationID="updateWebhook" method="put" path="/webhook/{id}" -->
```python
from livepeer import Livepeer
from livepeer.models import components


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.webhook.update(id="<id>", webhook={
        "name": "test_webhook",
        "project_id": "aac12556-4d65-4d34-9fb6-d1f0985eb0a9",
        "events": [
            components.Events.STREAM_STARTED,
            components.Events.STREAM_IDLE,
        ],
        "url": "https://my-service.com/webhook",
        "shared_secret": "my-secret",
        "stream_id": "de7818e7-610a-4057-8f6f-b785dc1e6f88",
    })

    assert res.webhook is not None

    # Handle response
    print(res.webhook)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `webhook`                                                           | [components.WebhookInput](../../models/components/webhookinput.md)  | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.UpdateWebhookResponse](../../models/operations/updatewebhookresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Delete a webhook

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteWebhook" method="delete" path="/webhook/{id}" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.webhook.delete(id="<id>")

    assert res.webhook is not None

    # Handle response
    print(res.webhook)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DeleteWebhookResponse](../../models/operations/deletewebhookresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_logs

Retrieve webhook logs

### Example Usage

<!-- UsageSnippet language="python" operationID="getWebhookLogs" method="get" path="/webhook/{id}/log" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.webhook.get_logs(id="<id>")

    assert res.data is not None

    # Handle response
    print(res.data)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetWebhookLogsResponse](../../models/operations/getwebhooklogsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_log

Retrieve a webhook log

### Example Usage

<!-- UsageSnippet language="python" operationID="getWebhookLog" method="get" path="/webhook/{id}/log/{logId}" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.webhook.get_log(id="<id>", log_id="<id>")

    assert res.webhook_log is not None

    # Handle response
    print(res.webhook_log)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `log_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetWebhookLogResponse](../../models/operations/getwebhooklogresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## resend_log

Use this API to resend the same webhook request. This is useful when
developing and debugging, allowing you to easily repeat the same webhook
to check or fix the behaviour in your handler.


### Example Usage

<!-- UsageSnippet language="python" operationID="resendWebhook" method="post" path="/webhook/{id}/log/{logId}/resend" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.webhook.resend_log(id="<id>", log_id="<id>")

    assert res.webhook_log is not None

    # Handle response
    print(res.webhook_log)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `log_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ResendWebhookResponse](../../models/operations/resendwebhookresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |