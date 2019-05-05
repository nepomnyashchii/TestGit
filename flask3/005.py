<<<<<<< HEAD
from flask import Flask
# from flask import Response
from flask import jsonify
=======
from flask import Flask, jsonify, request
>>>>>>> 2d0851eb39afeb91810c051a308c137d3c3b2567

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
<<<<<<< HEAD


=======
>>>>>>> 2d0851eb39afeb91810c051a308c137d3c3b2567
