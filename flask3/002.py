from flask import Flask
from flask import request
# print(__name__)
app = Flask(__name__)
@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    # elif request.method == 'POST':
    #     return "ECHO: POST\n"

    # elif request.method == 'PATCH':
    #     return "ECHO: PACTH\n"

    # elif request.method == 'PUT':
    #     return "ECHO: PUT\n"

    # elif request.method == 'DELETE':
    #     return "ECHO: DELETE"