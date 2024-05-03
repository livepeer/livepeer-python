# RoomUserPayload


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `name`                                                         | *str*                                                          | :heavy_check_mark:                                             | Display name                                                   | name                                                           |
| `can_publish`                                                  | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Whether a user is allowed to publish audio/video tracks        | true                                                           |
| `can_publish_data`                                             | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Whether a user is allowed to publish data messages to the room | true                                                           |
| `metadata`                                                     | *Optional[str]*                                                | :heavy_minus_sign:                                             | User defined payload to store for the participant              |                                                                |