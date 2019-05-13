from flask import Flask, jsonify, request

# print(__name__)
app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def api_hello():
    a = request.headers['A']
    data = {
        'hello': 'world' + a,
        'number': 3
    }
    resp = jsonify(data)
    resp.status_code = 201
    resp.headers['AAA'] = 'asdasdas'

    return resp

