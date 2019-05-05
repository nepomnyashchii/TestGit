from flask import Flask
# from flask import Response
from flask import jsonify

# print(__name__)
app = Flask(__name__)


@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers['Link'] = 'http://luisrei.com'

    return resp


