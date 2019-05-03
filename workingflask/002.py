from flask import request, Flask, jsonify, json


app = Flask(__name__)

# /hello?login=asd&password=asdxcv&password2=asdxcv
@app.route('/hello')
def api_hello():
    if 'login' in request.args:
        return jsonify(status="ok", answer='Hello ' + request.args['login'] + " " + request.args['password'])
    else:
        return jsonify(status="failed", answer='Hello')


@app.route('/req')
def api_req():
    print(request)
    return jsonify(username="aaa",
                   email="asd@asd.asd",
                   id="234")


@app.route('/echo', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE', 'PURGE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"
    return "ECHO: UDEFIND METHOD"


@app.route('/messages', methods=['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"


@app.route('/postdata', methods=['POST'])
def api_postdata():
    # from url request.args[]
    # data from body request.json
    # return request.args['aaa']
    # messages = json.loads(request.json)
    # messages = request.json
    print(request.is_json)
    return jsonify(data=request.json, urlparams=request.args)
