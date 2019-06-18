curl -H "Content-Type: application/json" -X GET http://localhost:5000/

curl -H "Content-Type: application/json" -X GET http://localhost:5000/todo

curl -H "Content-Type: application/json" -X GET http://localhost:5000/todo/64

curl -d '{"text":"asdasdasd"}' -H "Content-Type: application/json" -X POST http://localhost:5000/tod

curl -d '{
    "text":"asdasd",
    "done":true
}' -H "Content-Type: application/json" -X PUT http://localhost:5000/todo/64

curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/todo/64



