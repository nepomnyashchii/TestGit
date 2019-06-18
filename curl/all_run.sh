# curl localhost:5000/echo
# curl -X GET localhost:5000/echo
# curl -X POST localhost:5000/echo
# curl -X PUT localhost:5000/echo
# curl -X DELETE localhost:5000/echo
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/echo