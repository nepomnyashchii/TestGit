import requests
import json
import sys
base_url = "http://localhost:5000/run"


# Prepare Values for test 1
username = "alex"
flow = "goodmorning"
url = base_url + "/" + username + "/" + flow

print("Starting Test 1")
test_1_response = requests.get(url)
if (test_1_response.status_code != 200):
    sys.exit("Test 1 failed status = " + str(test_1_response.status_code))
try:
    test_1_json = test_1_response.json()
except ValueError:
    sys.exit("Test 1 failed no json in response")

if (test_1_json is None) or ("data" not in test_1_json.keys()):
    sys.exit("Test failed bed response data")
print("Test 1 Success")




# Prepare Values for test 2
username = "Fake user Name"
flow = "goodmorning"
url = base_url + "/" + username + "/" + flow

print("Starting Test 2")
test_2_response = requests.get(url)
if (test_2_response.status_code == 404):
    print("Test 2 Success")
else:
    sys.exit("Test 2 failed status = " + str(test_2_response.status_code))




# Prepare Values for test 3
username = "alex"
flow = "Fake Flow Name"
url = base_url + "/" + username + "/" + flow

print("Starting Test 3")
test_3_response = requests.get(url)
if (test_3_response.status_code == 404):
    print("Test 3 Success")
else:
    sys.exit("Test 3 failed status = " + str(test_3_response.status_code))


sys.exit("integration test is done\n\n\n")
