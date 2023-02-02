import json
import requests

output = requests.post("http://127.0.0.1:2222/method", data=json.dumps({})).text

output = json.loads(output)

print(output)
