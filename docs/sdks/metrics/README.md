# Metrics

## Overview

Operations related to metrics api

### Available Operations

* [get_realtime_viewership](#get_realtime_viewership) - Query realtime viewership
* [get_viewership](#get_viewership) - Query viewership metrics
* [get_creator_viewership](#get_creator_viewership) - Query creator viewership metrics
* [get_public_viewership](#get_public_viewership) - Query public total views metrics
* [get_usage](#get_usage) - Query usage metrics

## get_realtime_viewership

Requires a private (non-CORS) API key to be used.


### Example Usage

<!-- UsageSnippet language="python" operationID="getRealtimeViewershipNow" method="get" path="/data/views/now" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.metrics.get_realtime_viewership()

    assert res.data is not None

    # Handle response
    print(res.data)

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `playback_id`                                                                                                                                         | *Optional[str]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | The playback ID to filter the query results. This can be a canonical<br/>playback ID from Livepeer assets or streams, or dStorage identifiers<br/>for assets<br/> |
| `creator_id`                                                                                                                                          | *Optional[str]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | The creator ID to filter the query results                                                                                                            |
| `breakdown_by`                                                                                                                                        | List[[operations.BreakdownBy](../../models/operations/breakdownby.md)]                                                                                | :heavy_minus_sign:                                                                                                                                    | The list of fields to break down the query results. Specify this<br/>query-string multiple times to break down by multiple fields.<br/>               |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |

### Response

**[operations.GetRealtimeViewershipNowResponse](../../models/operations/getrealtimeviewershipnowresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_viewership

Requires a private (non-CORS) API key to be used.


### Example Usage

<!-- UsageSnippet language="python" operationID="getViewershipMetrics" method="get" path="/data/views/query" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.metrics.get_viewership(request={})

    assert res.data is not None

    # Handle response
    print(res.data)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetViewershipMetricsRequest](../../models/operations/getviewershipmetricsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetViewershipMetricsResponse](../../models/operations/getviewershipmetricsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_creator_viewership

Requires a proof of ownership to be sent in the request, which for now is just the assetId or streamId parameters (1 of those must be in the query-string).


### Example Usage

<!-- UsageSnippet language="python" operationID="getCreatorViewershipMetrics" method="get" path="/data/views/query/creator" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.metrics.get_creator_viewership(request={})

    assert res.data is not None

    # Handle response
    print(res.data)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetCreatorViewershipMetricsRequest](../../models/operations/getcreatorviewershipmetricsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.GetCreatorViewershipMetricsResponse](../../models/operations/getcreatorviewershipmetricsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_public_viewership

Allows querying for the public metrics for viewership about a video.
This can be called from the frontend with a CORS key, or even
unauthenticated.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPublicViewershipMetrics" method="get" path="/data/views/query/total/{playbackId}" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.metrics.get_public_viewership(playback_id="<id>")

    assert res.data is not None

    # Handle response
    print(res.data)

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `playback_id`                                                                                                                                         | *str*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | The playback ID to filter the query results. This can be a canonical<br/>playback ID from Livepeer assets or streams, or dStorage identifiers<br/>for assets<br/> |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |

### Response

**[operations.GetPublicViewershipMetricsResponse](../../models/operations/getpublicviewershipmetricsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_usage

Query usage metrics

### Example Usage

<!-- UsageSnippet language="python" operationID="getUsageMetrics" method="get" path="/data/usage/query" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.metrics.get_usage(request={})

    assert res.usage_metric is not None

    # Handle response
    print(res.usage_metric)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetUsageMetricsRequest](../../models/operations/getusagemetricsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetUsageMetricsResponse](../../models/operations/getusagemetricsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |