# Task
(*task*)

## Overview

Operations related to tasks api

### Available Operations

* [get_all](#get_all) - Retrieve Tasks
* [get](#get) - Retrieve a Task

## get_all

Retrieve Tasks

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.task.get_all()

if res.data is not None:
    # handle response
    pass

```




### Response

**[operations.GetTasksResponse](../../models/operations/gettasksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get

Retrieve a Task

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.task.get(task_id='<value>')

if res.task is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `task_id`          | *str*              | :heavy_check_mark: | ID of the task     |


### Response

**[operations.GetTaskResponse](../../models/operations/gettaskresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
