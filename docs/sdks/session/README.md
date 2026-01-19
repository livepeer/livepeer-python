# Session

## Overview

Operations related to session api

### Available Operations

* [get_clips](#get_clips) - Retrieve clips of a session
* [get_all](#get_all) - Retrieve sessions
* [get](#get) - Retrieve a session
* [get_recorded](#get_recorded) - Retrieve Recorded Sessions

## get_clips

Retrieve clips of a session

### Example Usage

<!-- UsageSnippet language="python" operationID="getSessionClips" method="get" path="/session/{id}/clips" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.session.get_clips(id="<id>")

    assert res.data is not None

    # Handle response
    print(res.data)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the parent session                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetSessionClipsResponse](../../models/operations/getsessionclipsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_all

Retrieve sessions

### Example Usage

<!-- UsageSnippet language="python" operationID="getSessions" method="get" path="/session" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.session.get_all()

    assert res.data is not None

    # Handle response
    print(res.data)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetSessionsResponse](../../models/operations/getsessionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a session

### Example Usage

<!-- UsageSnippet language="python" operationID="getSession" method="get" path="/session/{id}" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.session.get(id="<id>")

    assert res.session is not None

    # Handle response
    print(res.session)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the session                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetSessionResponse](../../models/operations/getsessionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_recorded

Retrieve Recorded Sessions

### Example Usage

<!-- UsageSnippet language="python" operationID="getRecordedSessions" method="get" path="/stream/{parentId}/sessions" -->
```python
from livepeer import Livepeer


with Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
) as l_client:

    res = l_client.session.get_recorded(parent_id="<id>", record=True)

    assert res.data is not None

    # Handle response
    print(res.data)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `parent_id`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | ID of the parent stream                                                |                                                                        |
| `record`                                                               | [Optional[operations.Record]](../../models/operations/record.md)       | :heavy_minus_sign:                                                     | Flag indicating if the response should only include recorded<br/>sessions<br/> | true                                                                   |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |                                                                        |

### Response

**[operations.GetRecordedSessionsResponse](../../models/operations/getrecordedsessionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |