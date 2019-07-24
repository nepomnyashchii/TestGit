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

response = requests.get("http://localhost:5000/secret/eb3474ac-003e-4dc3-a2f9-47f304b853c7/1234")
response_url = response.text
print(response_url)