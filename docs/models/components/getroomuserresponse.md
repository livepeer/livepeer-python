# GetRoomUserResponse


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `id`                                                    | *Optional[str]*                                         | :heavy_minus_sign:                                      | The ID of the user                                      | d32ae9e6-c459-4931-9898-e86e2f5e7e16                    |
| `joined_at`                                             | *Optional[int]*                                         | :heavy_minus_sign:                                      | Timestamp (in milliseconds) at which the user joined    | 1687517025261                                           |
| `name`                                                  | *Optional[str]*                                         | :heavy_minus_sign:                                      | The display name of the user                            | name                                                    |
| `is_publisher`                                          | *Optional[bool]*                                        | :heavy_minus_sign:                                      | Whether a user is allowed to publish audio/video tracks | true                                                    |
| `metadata`                                              | *Optional[str]*                                         | :heavy_minus_sign:                                      | User defined payload to store for the participant       |                                                         |