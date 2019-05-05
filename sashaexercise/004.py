import requests

url = "https://api.nasa.gov/planetary/apod"

querystring = {"api_key":"NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo"}

payload = "{\n\t\"mama\":\"people\"\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.11.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "31abc1ce-c1bc-4b7d-bbbd-14a9116cd68a,d47c960f-8100-4544-9deb-a8ef75c512aa",
    'Host': "api.nasa.gov",
    'accept-encoding': "gzip, deflate",
    'content-length': "20",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)