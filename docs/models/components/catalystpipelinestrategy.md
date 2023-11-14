# CatalystPipelineStrategy

Force to use a specific strategy in the Catalyst pipeline. If not specified, the default strategy that Catalyst is configured for will be used. This field only available for admin users, and is only used for E2E testing.


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `CATALYST`            | catalyst              |
| `CATALYST_FFMPEG`     | catalyst_ffmpeg       |
| `BACKGROUND_EXTERNAL` | background_external   |
| `BACKGROUND_MIST`     | background_mist       |
| `FALLBACK_EXTERNAL`   | fallback_external     |
| `EXTERNAL`            | external              |