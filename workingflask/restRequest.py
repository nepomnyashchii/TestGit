import http.client

conn = http.client.HTTPConnection("api,icndb,com")

payload = ""

headers = {'Content-Type': "application/json"}

conn.request("GET", "jokes,random", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
