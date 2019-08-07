import requests
import json
import sys
from colorama import Fore, Style
base_url = "http://localhost:5000/run"


print(Fore.YELLOW + "Test flows APIs " + Style.RESET_ALL)

# # Prepare Values for test 1
# username = "alex"
# flow = "goodmorning"
# url = base_url + "/" + username + "/" + flow

# print("Starting Test 1")
# test_1_response = requests.get(url)
# if (test_1_response.status_code != 200):
#     sys.exit("Test 1 failed status = " + str(test_1_response.status_code))
# try:
#     test_1_json = test_1_response.json()
# except ValueError:
#     sys.exit("Test 1 failed no json in response")

# if (test_1_json is None) or ("data" not in test_1_json.keys()):
#     sys.exit("Test failed bed response data")
# print(Fore.GREEN + "Test 1 Success" + Style.RESET_ALL)


# # Prepare Values for test 2
# username = "Fake user Name"
# flow = "goodmorning"
# url = base_url + "/" + username + "/" + flow

# print("Starting Test 2")
# test_2_response = requests.get(url)
# if (test_2_response.status_code == 404):
#     print(Fore.GREEN + "Test 2 Success" + Style.RESET_ALL)
# else:
#     sys.exit("Test 2 failed status = " + str(test_2_response.status_code))


# # Prepare Values for test 3
# username = "alex"
# flow = "Fake Flow Name"
# url = base_url + "/" + username + "/" + flow

# print("Starting Test 3")
# test_3_response = requests.get(url)
# if (test_3_response.status_code == 404):
#     print(Fore.GREEN + "Test 3 Success" + Style.RESET_ALL)
# else:
#     sys.exit("Test 3 failed status = " + str(test_3_response.status_code))


# Prepare Values for test 4
username = "alex"
url = base_url + "/" + username

print("Starting Test 4")
test_4_response = requests.get(url)
if (test_4_response.status_code != 200):
    sys.exit("Test 4 failed status = " + str(test_4_response.status_code))
try:
    test_4_json = test_4_response.json()
except ValueError:
    sys.exit("Test 4 failed no json in response")

print (test_4_json)
# if (test_4_json is None) or ("data" not in test_4_json.keys()):
#     sys.exit("Test failed bed response data")
print(Fore.GREEN + "Test 4 Success" + Style.RESET_ALL)



sys.exit("integration test is done\n\n\n")
