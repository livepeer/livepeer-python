# CreateRoomUserResponse


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `http_meta`                                                                          | [components.HTTPMetadata](../../models/components/httpmetadata.md)                   | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `room_user_response`                                                                 | [Optional[components.RoomUserResponse]](../../models/components/roomuserresponse.md) | :heavy_minus_sign:                                                                   | Success                                                                              |
| `error`                                                                              | *Optional[errors.Error]*                                                             | :heavy_minus_sign:                                                                   | Error                                                                                |