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


URLA = "http://localhost:5000/secret/" + sid + "/" + str(pin)

response = requests.get(URLA)
response_url = response.text
print(response_url)

data = {
    "sid" : sid,
    "pin": pin}

payload = json.dumps(data)
response = requests.delete(url, data = payload, headers =headers)
print(response.text)
print(response.json())




# print(response.json())
