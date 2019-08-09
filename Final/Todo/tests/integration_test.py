import requests
import json
import sys
from colorama import Fore, Style

# Prepare Values for tests
url = "http://localhost:5000/todo"

# Test 1
print("Starting Test 1")
headers = {'Content-Type': "application/json"}
data = {
    "text": "asdasd",
    "username": "alex",
    "done": 1
}

payload = json.dumps(data)
test_1_response = requests.post(url, data=payload, headers=headers)
test_1_json = test_1_response.json()
print(test_1_json)

if test_1_json is None or (test_1_json is not None and "id" not in test_1_json.keys()):
    sys.exit("Test 1 failed", 1)
print(Fore.GREEN + "Test 1 Success" + Style.RESET_ALL)


# # Test 2
print("Starting Test 2")
test_2_response = requests.get(url)
test_2_json = test_2_response.json()
print(test_2_json)
if test_2_json is None or (test_2_json is not None and "data" not in test_2_json.keys()):
    sys.exit("Test 2 failed", 2)
print(Fore.GREEN + "Test 2 Success" + Style.RESET_ALL)


# # Prepare Values for tests

id = 79

# # Test 3
print("Starting Test 3")
test_3_response = requests.get(url + "/" + str(id))
test_3_json = test_3_response.json()
print(test_3_json)
if test_3_json is None or (test_3_json is not None and "data" not in test_3_json.keys()):
    sys.exit("Test 3 failed", 3)
print(Fore.GREEN + "Test 3 Success" + Style.RESET_ALL)

# Test 4
print("Starting Test 4")
headers = {'Content-Type': "application/json"}
data = {"text": "asdasdasd"}
payload = json.dumps(data)
test_4_response = requests.post(url, data=payload, headers=headers)
test_4_json = test_1_response.json()
print(test_4_json)

if test_4_json is None or (test_4_json is not None and "id" not in test_4_json.keys()):
    sys.exit("Test 1 failed", 4)
print(Fore.GREEN + "Test 4 Success" + Style.RESET_ALL)

id = 87
# # Test 5
print("Starting Test 5")
test_5_response = requests.delete(url + "/" + str(id))
test_5_json = test_5_response.json()
print(test_5_json)
if test_5_json is None or (test_5_json is not None and "id" not in test_5_json.keys()):
    sys.exit("Test 5 failed", 5)
print(Fore.GREEN + "Test 5 Success" + Style.RESET_ALL)

sys.exit("All integration tests are done\n\n\n")
