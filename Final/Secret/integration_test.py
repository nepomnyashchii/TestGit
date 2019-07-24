import requests

data = {
    "msg" :"success",
    "pin": 1234,
    "exp": 1000
}

API_ENDPOINT = "https://5000-c2d101ea-6ebb-45c7-aa95-fd28b9062de9.ws-us0.gitpod.io/secret"
response = requests.post(url = API_ENDPOINT, data=data)


response_url = response.text
print(response_url)

