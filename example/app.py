import livepeer
from livepeer.models import components

s = livepeer.Livepeer(
    api_key="<your-api-key-here>",
)

req = components.NewStreamPayload(
    name='stream from python sdk',
)

res = s.stream.create(req)

print(res)