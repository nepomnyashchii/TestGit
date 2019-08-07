import requests
import json
import sys

# Prepare Values for test
url = "http://localhost:5000/run"

# Prepare Values for tests

username = "Alec" or "Alex"

# Test 1
print("Starting Test 1")
test_1_response = requests.get(url + "/" + username)
test_1_json = test_1_response.json()
if test_1_json is None:
    sys.exit("Test 1 failed", 1)
print("Test 1 passed")

sys.exit("integration test is done\n\n\n")
