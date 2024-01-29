# UsageMetric

An individual metric about usage of a user.



## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `user_id`                                 | *str*                                     | :heavy_check_mark:                        | The user ID associated with the metric    |
| `creator_id`                              | *str*                                     | :heavy_check_mark:                        | The creator ID associated with the metric |
| `delivery_usage_mins`                     | *float*                                   | :heavy_check_mark:                        | The number of minutes of delivery usage   |
| `total_usage_mins`                        | *float*                                   | :heavy_check_mark:                        | The number of minutes of total usage      |
| `storage_usage_mins`                      | *float*                                   | :heavy_check_mark:                        | The number of minutes of storage usage    |