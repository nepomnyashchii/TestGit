import requests

url = "https://postman-echo.com/get"

querystring = {"foo500":["bar20","bar20%0A%0A"]}

payload = "{\n\t\"mama\":\"people\"\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.11.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "2f50452e-57c6-4e73-bed4-1cd7c1c64c35,1a405581-befe-45e3-93cc-170b007d4e37",
    'Host': "postman-echo.com",
    'cookie': "sails.sid=s%3AqR72ZaTP9GryoSruh4ecVmf57mqmaOtM.%2FaW4GpG2rNFHcMOLYdiU7nPIgGXzioDlL09UylrxiTQ",
    'accept-encoding': "gzip, deflate",
    'content-length': "20",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)