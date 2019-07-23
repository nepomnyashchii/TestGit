curl -d '{
    "msg":"success",
    "pin": 1234,
    "exp": 1000
}' -H "Content-Type: application/json" -X POST http://localhost:5000/secret

# todo/id POST Request (add asdasdasd inside the table in the column text): We use Body as a request (letter d is from there)
# curl -d '{"text":"asdasdasd"}' -H "Content-Type: application/json" -X POST http://localhost:5000/todo