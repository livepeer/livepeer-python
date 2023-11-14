# Metrics
(*metrics*)

### Available Operations

* [get_viewership](#get_viewership) - Query viewership metrics
* [get_creator_viewership](#get_creator_viewership) - Query creator viewership metrics
* [get_public_total_views](#get_public_total_views) - Query public total views metrics
* [get_usage](#get_usage) - Query usage metrics

## get_viewership

Query viewership metrics

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)

req = operations.GetViewershipsMetricsRequest(
980301,
366854,
    breakdown_by=[
        operations.BreakdownBy.PLAYBACK_ID,
    ],
)

res = s.metrics.get_viewership(req)

if res.data is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetViewershipsMetricsRequest](../../models/operations/getviewershipsmetricsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetViewershipsMetricsResponse](../../models/operations/getviewershipsmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_creator_viewership

Query creator viewership metrics

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)

req = operations.GetCreatorMetricsRequest(
dateutil.parser.isoparse('2021-06-16T23:48:30.007Z'),
702371,
    breakdown_by=[
        operations.QueryParamBreakdownBy.DEVICE_TYPE,
    ],
)

res = s.metrics.get_creator_viewership(req)

if res.data is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetCreatorMetricsRequest](../../models/operations/getcreatormetricsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetCreatorMetricsResponse](../../models/operations/getcreatormetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_public_total_views

Query public total views metrics

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.metrics.get_public_total_views(playback_id='string')

if res.data is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `playback_id`                                                                                                                                         | *str*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | The playback ID to filter the query results. This can be a canonical<br/>playback ID from Livepeer assets or streams, or dStorage identifiers<br/>for assets<br/> |


### Response

**[operations.GetPublicTotalViewsMetricsResponse](../../models/operations/getpublictotalviewsmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_usage

Query usage metrics

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.metrics.get_usage(from_=224089, to=231125, time_step=operations.GetUsageMetricsQueryParamTimeStep.DAY, creator_id='string')

if res.usage_metric is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                | *Optional[int]*                                                                                                        | :heavy_minus_sign:                                                                                                     | Start millis timestamp for the query range (inclusive)<br/>                                                            |
| `to`                                                                                                                   | *Optional[int]*                                                                                                        | :heavy_minus_sign:                                                                                                     | End millis timestamp for the query range (exclusive)<br/>                                                              |
| `time_step`                                                                                                            | [Optional[operations.GetUsageMetricsQueryParamTimeStep]](../../models/operations/getusagemetricsqueryparamtimestep.md) | :heavy_minus_sign:                                                                                                     | The time step to aggregate viewership metrics by<br/>                                                                  |
| `creator_id`                                                                                                           | *Optional[str]*                                                                                                        | :heavy_minus_sign:                                                                                                     | The creator ID to filter the query results<br/>                                                                        |


### Response

**[operations.GetUsageMetricsResponse](../../models/operations/getusagemetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
