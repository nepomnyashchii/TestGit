import requests

data = {
    "msg":"success",
    "pin": 1234,
    "exp": 1000
}

API_ENDPOINT = "http://localhost:5000/secret"
response = requests.post(url = API_ENDPOINT, data=data)


response_url = response.text
print(response_url)

sid = "69e90627-e82d-481a-9818-b5b7b63e33bd"
msg = 1234
URL = "http://localhost:5000/secret/sid/msg"

response = requests.get("http://localhost:5000/secret/69e90627-e82d-481a-9818-b5b7b63e33bd/1234")
response_url = response.text
print(response_url)