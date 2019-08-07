import requests
import json
import sys

# Prepare Values for test
url = "http://localhost:5000/run"

# Prepare Values for tests

username = "Alec" or "Alex"
# Test 1
print("Starting Test")
test_1_response = requests.get(url + "/" + username)
test_1_json = test_1_response.json()
print(test_1_json)
if test_1_json is None or "error" or "status" in test_1_json.keys():
    sys.exit("Test failed", 2)
print("Test passed")

sys.exit("integration test is done\n\n\n")
