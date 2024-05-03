# UsageMetric

An individual metric about usage of a user.



## Fields

| Field                                     | Type                                      | Required                                  | Description                               | Example                                   |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `user_id`                                 | *Optional[str]*                           | :heavy_minus_sign:                        | The user ID associated with the metric    | 1bde4o2i6xycudoy                          |
| `creator_id`                              | *Optional[str]*                           | :heavy_minus_sign:                        | The creator ID associated with the metric | john@doe.com                              |
| `delivery_usage_mins`                     | *Optional[float]*                         | :heavy_minus_sign:                        | Total minutes of delivery usage.          | 100                                       |
| `total_usage_mins`                        | *Optional[float]*                         | :heavy_minus_sign:                        | Total transcoded minutes.                 | 100                                       |
| `storage_usage_mins`                      | *Optional[float]*                         | :heavy_minus_sign:                        | Total minutes of storage usage.           | 100                                       |