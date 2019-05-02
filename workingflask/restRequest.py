import http.client

conn = http.client.HTTPConnection("5000-f731954c-233a-4c2a-b948-35aa66e8bf06.ws-us0.gitpod.io:443")

payload = "{\n    \"login\": \"Hello sdfsdfData\",\n    \"password\": \"This is maeesage1\"\n}"

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "3bf00d27-cb3b-4829-90c9-3fc2525683c6"
    }

conn.request("POST", "postdata", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))