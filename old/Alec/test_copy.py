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
if response.json() is None or response.json () is not None and "sid" not in response.json.keys() or "pin" not in response.json.keys():
    print("There is an error in the file")
else:
    response.json()
    print("Information for post_method succesfully received")
    print(response.json())


sid = response["sid"]
pin = data["pin"]
URL = "http://localhost:5000/secret/" + sid + "/" + str(pin)
response = requests.get(URL)

if response.json() is None or response.json() is not None and "msg" not in response.json.keys():
    print("There is an error in requests_get")
else:
    response.json()
    print("Information for get_method succesfully received")
    print(response.json())

data = {
    "sid": sid,
    "pin": pin}

payload = json.dumps(data)
response = requests.delete(url, data=payload, headers=headers)
if response.json() is None or response.json() is not None and "deleted_sid" not in response.json.keys():
    
print(response.json())


# print(response.json())
