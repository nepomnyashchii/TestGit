import requests
import json

url = "http://localhost:5000/secret"
headers = {'Content-Type': "application/json"}

# payload = '{"msg":"ggg", "pin": 12345,"exp": 10000}'

data = {'msg': 'success',
        'pin': 1234,
        'exp': 10000}

payload = json.dumps(data)

response = requests.post(url, data=payload, headers=headers)

if response.json() is None:
    print("There is no information from the post_request")
else:
    response.json()
    print("Information for post_method succesfully received")
    print(response.json())


result = response.json()

sid = result["sid"]
pin = data["pin"]

print(sid)
print(pin)

URL = "http://localhost:5000/secret/" + sid + "/" + str(pin)

response = requests.get(URL)

if response.json() is None:
    print("There is no information from the get_request")
else:
    response.json()
    print("Information for post_method succesfully received")
    print(response.json())

result = response.json()
msg = result["msg"]
print(msg)

data = {
    "sid": sid,
    "pin": pin}

payload = json.dumps(data)
response = requests.delete(url, data=payload, headers=headers)

if response.json() is None:
    print("There is no information from the delete_request")
else:
    response.json()
    print("Information for post_method succesfully received")
    print(response.json())

result = response.json()
deleted_id = result["deleted_id"]


# print(response.json())

