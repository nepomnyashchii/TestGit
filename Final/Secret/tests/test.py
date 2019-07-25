import requests
import json
import sys

url = "http://localhost:5000/secret"
headers = {'Content-Type': "application/json"}

data = {'msg': 'success',
        'pin': 1234,
        'exp': 10000}

payload = json.dumps(data)

test_1_response = requests.post(url, data=payload, headers=headers)
test_1 = test_1_response.json()
print(test_1)
if test_1 is None and "sid" not in test_1.keys() or "pin" not in test_1.keys():
    test_1_response == False
    # sys.exit("test_1 integration test failed")
else:
    test_1_response ==True
    result = test_1
    sid = result["sid"]
    pin = data["pin"]
    print(sid)
    print(pin)


test_2_response = requests.get("http://localhost:5000/secret/" + sid + "/" + str(pin))

test_2 = test_2_response.json()
if test_1_response == True:
    if test_2 is None and "msg" not in test_2.keys():
        test_2_response == False
        sys.exit("test_2 integration test failed")
    else:
        test_2_response == True
        result = test_2
        msg = result["msg"]
        print(msg)

data = {
    "sid": sid,
    "pin": pin}

payload = json.dumps(data)
test_3_response = requests.delete(url, data=payload, headers=headers)
test_3 = test_3_response.json()
if test_2_response == True:
    if test_3 is None and "deleted_id" not in test_3.keys():
        test_3_response == False
        sys.exit("test_3 integration test failed")
    else:
        test_3_response == True
        result = test_3
        deleted_id = result["deleted_id"]
        print(deleted_id)

sys.exit("All integration tests are done")

