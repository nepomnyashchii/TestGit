# introductory note
# curl -H "Content-Type: application/json" -X GET http://localhost:5000/

# todo (get from the table data)
# curl -H "Content-Type: application/json" -X GET http://localhost:5000/todo

# todo/id (get from the table data with certain id)
# curl -H "Content-Type: application/json" -X GET http://localhost:5000/todo/64

# todo/id POST Request (add asdasdasd inside the table in the column text): We use Body as a request (letter d is from there)
# curl -d '{"text":"asdasdasd"}' -H "Content-Type: application/json" -X POST http://localhost:5000/todo

# # todo/id PUT Request (add from the dictionary text to text and to done:TRUE): We use Body as a request
# curl -d '{
#     "text":"asdasd",
#     "done":true
# }' -H "Content-Type: application/json" -X PUT http://localhost:5000/todo/64

# #todo/id DELETE Request (delete from the dictionary the data with certain id)
# curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/todo/64

curl -d '{
    "msg":"success",
    "pin": 1234,
    "exp": 1000
}' -H "Content-Type: application/json" -X POST http://localhost:5000/secret



