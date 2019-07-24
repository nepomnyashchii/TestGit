
curl -d '{
    "msg":"success",
    "pin": 1234,
    "exp": 1000
}' -H "Content-Type: application/json" -X POST http://localhost:5000/secret



