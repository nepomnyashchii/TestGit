import requests
import json


url = "http://localhost:5000/secret"
headers = {'Content-Type': "application/json"}

# payload = '{"msg":"ggg", "pin": 12345,"exp": 10000}'

data = {'msg': 'Secret Message',
         'exp': 6000,
         'pin': 12345}
payload = json.dumps(data)


response = requests.post(url, data=payload ,headers=headers)
print(response.text)
# print(response.json())
