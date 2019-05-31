import requests

url = "http://api.icndb.com/jokes/random"

querystring = {"firstName":"John","amp":"","lastName":"Nor"}

payload = ""
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.11.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "8252934d-f975-4f8d-94dd-1726085ee194,cf47d34b-8e07-414c-8f91-efe6c15f69df",
    'Host': "api.icndb.com",
    'cookie': "__cfduid=d9d72428bf8889612b97dc082e89fab511556835413",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)