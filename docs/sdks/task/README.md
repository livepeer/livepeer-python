# Task

## Overview

Operations related to tasks api

### Available Operations

* [get_all](#get_all) - Retrieve Tasks
* [get](#get) - Retrieve a Task

## get_all

Retrieve Tasks

### Example Usage

<!-- UsageSnippet language="python" operationID="getTasks" method="get" path="/task" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.task.get_all()

    assert res.data is not None

    # Handle response
    print(res.data)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetTasksResponse](../../models/operations/gettasksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a Task

### Example Usage

<!-- UsageSnippet language="python" operationID="getTask" method="get" path="/task/{taskId}" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.task.get(task_id="<id>")

    assert res.task is not None

    # Handle response
    print(res.task)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | ID of the task                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetTaskResponse](../../models/operations/gettaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |