# Session
(*session*)

### Available Operations

* [get_all_clips](#get_all_clips) - Retrieve clips of a session
* [get_all](#get_all) - Retrieve sessions
* [get](#get) - Retrieve a session
* [get_recorded](#get_recorded) - Retrieve Recorded Sessions

## get_all_clips

Retrieve clips of a session

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.session.get_all_clips(id='string')

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                | Type                     | Required                 | Description              |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `id`                     | *str*                    | :heavy_check_mark:       | ID of the parent session |


### Response

**[operations.GetSessionIDClipsResponse](../../models/operations/getsessionidclipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_all

Retrieve sessions

### Example Usage

```python
import sdk

s = sdk.SDK(
    api_key="",
)


res = s.session.get_all()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetSessionsResponse](../../models/operations/getsessionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get

Retrieve a session

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.session.get(id='string')

if res.session is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | ID of the session  |


### Response

**[operations.GetSessionResponse](../../models/operations/getsessionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_recorded

Retrieve Recorded Sessions

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    api_key="",
)


res = s.session.get_recorded(parent_id='string', record=1)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `parent_id`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | ID of the parent stream                                                |                                                                        |
| `record`                                                               | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | Flag indicating if the response should only include recorded<br/>sessions<br/> | 1                                                                      |


### Response

**[operations.GetRecordedSessionsResponse](../../models/operations/getrecordedsessionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
