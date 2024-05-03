# Request


## Fields

| Field                               | Type                                | Required                            | Description                         | Example                             |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `url`                               | *Optional[str]*                     | :heavy_minus_sign:                  | URL used for the request            | https://my-service.com/webhook      |
| `method`                            | *Optional[str]*                     | :heavy_minus_sign:                  | HTTP request method                 | POST                                |
| `headers`                           | Dict[str, *str*]                    | :heavy_minus_sign:                  | HTTP request headers                | {<br/>"User-Agent": "livepeer.studio"<br/>} |
| `body`                              | *Optional[str]*                     | :heavy_minus_sign:                  | request body                        | {"event": "stream.started"}         |