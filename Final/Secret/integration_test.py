import requests

response = requests.get(
"https://5000-c2d101ea-6ebb-45c7-aa95-fd28b9062de9.ws-us0.gitpod.io/secret")

if response.json():
    print("Program is working fine")
else:
    print("There is an error")


