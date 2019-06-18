# curl localhost:5000/echo
# curl -X GET localhost:5000/echo
# curl -X POST localhost:5000/echo
# curl -X PUT localhost:5000/echo
# curl -X DELETE localhost:5000/echo
# curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/echo
# curl -d '{"option": "value", "something": "anothervalue"}' -H "Content-Type: application/json" -X POST http://localhost:5000/echo
# curl -d '{"text":"asdasdasd"}' -H "Content-Type: application/json" -X POST http://localhost:5000/todo
curl -d '{
    "text":"asdasd",
    "done":true
}' -H "Content-Type: application/json" -X PUT http://localhost:5000/todo/64
