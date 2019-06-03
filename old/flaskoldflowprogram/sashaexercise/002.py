import requests

url = "http://api.icndb.com/jokes/random/1"

payload = "{\n\t\"mama\":\"people\"\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.11.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "a841295a-0811-44c4-a5a9-c8b66426c5a5,ad490760-522e-443c-87a5-18a94edca8b3",
    'Host': "api.icndb.com",
    'cookie': "__cfduid=d9d72428bf8889612b97dc082e89fab511556835413",
    'accept-encoding': "gzip, deflate",
    'content-length': "20",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)