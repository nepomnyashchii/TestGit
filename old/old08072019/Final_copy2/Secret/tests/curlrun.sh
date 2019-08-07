
curl -d '{
    "msg":"success",
    "pin": 1234,
    "exp": 1000
}' -H "Content-Type: application/json" -X POST http://localhost:5000/secret

pin = 1234
sid = 83c30c7d-3571-4dbb-b64e-e888d12d7300

 curl -H "Content-Type: application/json" -X GET http://localhost:5000/secret/sid/pin

 curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/secret/sid/pin

curl - d '{
    "pin": 1234,
    "sid" : "83c30c7d-3571-4dbb-b64e-e888d12d7300"
}'
-H "Content-Type: application/json" -X DELETE http://localhost:5000/secret/sid/pin