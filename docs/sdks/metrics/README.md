# Metrics
(*metrics*)

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

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.metrics.get_realtime_viewership()

if res.data is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `playback_id`                                                                                                                                         | *Optional[str]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | The playback ID to filter the query results. This can be a canonical<br/>playback ID from Livepeer assets or streams, or dStorage identifiers<br/>for assets<br/> |
| `creator_id`                                                                                                                                          | *Optional[str]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | The creator ID to filter the query results                                                                                                            |
| `breakdown_by`                                                                                                                                        | List[[operations.BreakdownBy](../../models/operations/breakdownby.md)]                                                                                | :heavy_minus_sign:                                                                                                                                    | The list of fields to break down the query results. Specify this<br/>query-string multiple times to break down by multiple fields.<br/>               |


### Response

**[operations.GetRealtimeViewershipNowResponse](../../models/operations/getrealtimeviewershipnowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_viewership

Requires a private (non-CORS) API key to be used.


### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.metrics.get_viewership()

if res.data is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetViewershipMetricsRequest](../../models/operations/getviewershipmetricsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetViewershipMetricsResponse](../../models/operations/getviewershipmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_creator_viewership

Requires a proof of ownership to be sent in the request, which for now is just the assetId or streamId parameters (1 of those must be in the query-string).


### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.metrics.get_creator_viewership()

if res.data is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetCreatorViewershipMetricsRequest](../../models/operations/getcreatorviewershipmetricsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetCreatorViewershipMetricsResponse](../../models/operations/getcreatorviewershipmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_public_viewership

Allows querying for the public metrics for viewership about a video.
This can be called from the frontend with a CORS key, or even
unauthenticated.


### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.metrics.get_public_viewership(playback_id='<value>')

if res.data is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `playback_id`                                                                                                                                         | *str*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | The playback ID to filter the query results. This can be a canonical<br/>playback ID from Livepeer assets or streams, or dStorage identifiers<br/>for assets<br/> |


### Response

**[operations.GetPublicViewershipMetricsResponse](../../models/operations/getpublicviewershipmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_usage

Query usage metrics

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.metrics.get_usage()

if res.usage_metric is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetUsageMetricsRequest](../../models/operations/getusagemetricsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetUsageMetricsResponse](../../models/operations/getusagemetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
