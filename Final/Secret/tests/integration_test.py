import requests
import json
import sys
from colorama import Fore, Style


print(Fore.YELLOW + "Test Secret" + Style.RESET_ALL)

# Prepare Values for tests
url = "http://localhost:5000/secret"

# Test 1
print("Starting Test 1")
headers = {'Content-Type': "application/json"}
data = {'msg': 'success',
        'pin': 1234,
        'exp': 10000}

payload = json.dumps(data)
test_1_response = requests.post(url, data=payload, headers=headers)
test_1_json = test_1_response.json()
print(test_1_json)

if test_1_json is None or (test_1_json is not None and "sid" not in test_1_json.keys()):
    sys.exit("Test 1 failed", 1)
print(Fore.GREEN + "Test 1 Success" + Style.RESET_ALL)

# Prepare Values for tests
sid = test_1_json["sid"]
pin = data["pin"]


# Test 2
print("Starting Test 2")
test_2_response = requests.get(url + "/" + sid + "/" + str(pin))
test_2_json = test_2_response.json()
if test_2_json is None or (test_2_json is not None and "msg" not in test_2_json.keys()):
    sys.exit("Test 2 failed", 2)
print(Fore.GREEN + "Test 2 Success" + Style.RESET_ALL)


# Prepare Values for tests
data = {"sid": sid, "pin": pin}
payload = json.dumps(data)

# Test 3
print("Starting Test 3")
test_3_response = requests.delete(url, data=payload, headers=headers)
test_3_json = test_3_response.json()

if test_3_json is None or (test_3_json is not None and "deleted_sid" not in test_3_json.keys()):
    sys.exit("Test 3 failed", 3)
deleted_id = test_3_json["deleted_sid"]

print(Fore.GREEN + "Test 3 Success" + Style.RESET_ALL)

sys.exit("All integration tests are done\n\n\n")
