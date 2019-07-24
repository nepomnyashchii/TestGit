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
print(response.json())
print(response.text)

result = response.json()

sid = result["sid"]
pin = data["pin"]


URL = "http://localhost:5000/secret/" + sid + "/" + str(pin)

response = requests.get(URL)
response_url = response.text
print(response_url)


# print(response.json())
