import requests
import json


url = "http://localhost:5000/secret"
headers = {'Content-Type': "application/json"}

# payload = '{"msg":"ggg", "pin": 12345,"exp": 10000}'

data = {'msg': 'success',
         'pin': 1234,
         'exp': 10000}

payload = json.dumps(data)


response = requests.post(url, data=payload ,headers=headers)
print(response.text)


sid = "69e90627-e82d-481a-9818-b5b7b63e33bd"
msg = 1234
# URL = "http://localhost:5000/secret/sid/msg"

response = requests.get("http://localhost:5000/secret/sid/str(pin)")
response_url = response.text
print(response_url)
# print(response.json())
