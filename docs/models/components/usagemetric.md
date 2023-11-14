# UsageMetric

An individual metric about usage of a user.



## Fields

| Field                                     | Type                                      | Required                                  | Description                               | Example                                   |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `user_id`                                 | *str*                                     | :heavy_check_mark:                        | The user ID associated with the metric    | 3e02c844-d364-4d48-b401-24b2773b5d6c      |
| `creator_id`                              | *str*                                     | :heavy_check_mark:                        | The creator ID associated with the metric | 3e02c844-d364-4d48-b401-24b2773b5d6c      |
| `delivery_usage_mins`                     | *float*                                   | :heavy_check_mark:                        | The number of minutes of delivery usage   | 10                                        |
| `total_usage_mins`                        | *float*                                   | :heavy_check_mark:                        | The number of minutes of total usage      | 10                                        |
| `storage_usage_mins`                      | *float*                                   | :heavy_check_mark:                        | The number of minutes of storage usage    | 10                                        |