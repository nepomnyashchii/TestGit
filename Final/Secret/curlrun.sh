
curl -d '{
    "msg":"success",
    "pin": 1234,
    "exp": 1000
}' -H "Content-Type: application/json" -X POST http://localhost:5000/secret

# pin = 1234
# sid = 1012e8c1-8fe7-491a-9050-554b115ce46a

#  curl -H "Content-Type: application/json" -X GET http://localhost:5000/secret/sid/pin

#  curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/secret/sid/pin