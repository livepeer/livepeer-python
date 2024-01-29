# PlaybackPolicy

Whether the playback policy for a asset or stream is public or signed


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `type`                                             | [components.Type](../../models/components/type.md) | :heavy_check_mark:                                 | N/A                                                |
| `webhook_id`                                       | *Optional[str]*                                    | :heavy_minus_sign:                                 | ID of the webhook to use for playback policy       |
| `webhook_context`                                  | Dict[str, *Any*]                                   | :heavy_minus_sign:                                 | User-defined webhook context                       |