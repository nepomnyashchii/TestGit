import requests
import json
import sys

# Prepare Values for test
base_url = "http://localhost:5000/run"

# Prepare Values for tests
username = "Alec" # or "Alex"
flow = "goodmorning"
# Test 1
print("Starting Test")
url = base_url + "/" + username + "/" + flow
print(url)
test_1_response = requests.get()
test_1_json = test_1_response.json()
print(test_1_json)
if test_1_json is None or "data" not in test_1_json.keys():
    sys.exit("Test failed", 1)
print("Test passed")

sys.exit("integration test is done\n\n\n")