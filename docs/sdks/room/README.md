# Room
(*room*)

## Overview

Operations related to rooms api

### Available Operations

* [~~create~~](#create) - Create a room :warning: **Deprecated**
* [~~get~~](#get) - Retrieve a room :warning: **Deprecated**
* [~~delete~~](#delete) - Delete a room :warning: **Deprecated**
* [~~start_egress~~](#start_egress) - Start room RTMP egress :warning: **Deprecated**
* [~~stop_egress~~](#stop_egress) - Stop room RTMP egress :warning: **Deprecated**
* [~~create_user~~](#create_user) - Create a room user :warning: **Deprecated**
* [~~get_user~~](#get_user) - Get user details :warning: **Deprecated**
* [~~update_user~~](#update_user) - Update a room user :warning: **Deprecated**
* [~~delete_user~~](#delete_user) - Remove a user from the room :warning: **Deprecated**

## ~~create~~

Create a multiparticipant livestreaming room.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.room.create()

if res.create_room_response is not None:
    # handle response
    pass

```




### Response

**[operations.CreateRoomResponse](../../models/operations/createroomresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## ~~get~~

Retrieve a room

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.room.get(id='<value>')

if res.room is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetRoomResponse](../../models/operations/getroomresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## ~~delete~~

Delete a room

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.room.delete(id='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteRoomResponse](../../models/operations/deleteroomresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## ~~start_egress~~

Create a livestream for your room.
This allows you to leverage livestreaming features like recording and HLS output.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import livepeer
from livepeer.models import components

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.room.start_egress(id='<value>', room_egress_payload=components.RoomEgressPayload(
    stream_id='aac12556-4d65-4d34-9fb6-d1f0985eb0a9',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `room_egress_payload`                                                        | [components.RoomEgressPayload](../../models/components/roomegresspayload.md) | :heavy_check_mark:                                                           | N/A                                                                          |


### Response

**[operations.StartRoomEgressResponse](../../models/operations/startroomegressresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## ~~stop_egress~~

Stop room RTMP egress

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.room.stop_egress(id='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.StopRoomEgressResponse](../../models/operations/stoproomegressresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## ~~create_user~~

Call this endpoint to add a user to a room, specifying a display name at a minimum.
The response will contain a joining URL for Livepeer's default meeting app.
Alternatively the joining token can be used with a custom app.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import livepeer
from livepeer.models import components

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.room.create_user(id='<value>', room_user_payload=components.RoomUserPayload(
    name='name',
    can_publish=True,
    can_publish_data=True,
))

if res.room_user_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `room_user_payload`                                                      | [components.RoomUserPayload](../../models/components/roomuserpayload.md) | :heavy_check_mark:                                                       | N/A                                                                      |


### Response

**[operations.CreateRoomUserResponse](../../models/operations/createroomuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## ~~get_user~~

Get user details

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.room.get_user(id='<value>', user_id='<value>')

if res.get_room_user_response is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetRoomUserResponse](../../models/operations/getroomuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## ~~update_user~~

Update properties for a user.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import livepeer
from livepeer.models import components

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.room.update_user(id='<value>', user_id='<value>', room_user_update_payload=components.RoomUserUpdatePayload(
    can_publish=True,
    can_publish_data=True,
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `user_id`                                                                            | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `room_user_update_payload`                                                           | [components.RoomUserUpdatePayload](../../models/components/roomuserupdatepayload.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |


### Response

**[operations.UpdateRoomUserResponse](../../models/operations/updateroomuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## ~~delete_user~~

Remove a user from the room

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import livepeer

s = livepeer.Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.room.delete_user(id='<value>', user_id='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteRoomUserResponse](../../models/operations/deleteroomuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
