from flask import Flask
import lib

app = Flask(__name__)


# @app.route('/')
# def index():
#     return 'Super muoer cool web service'


@app.route('/put/<msg>/<int:pin>/<int:exp>')
def put(msg, pin, exp):
    return lib.put_secret(msg, pin, exp)


@app.route('/get/<sid>/<int:pin>')
def get(sid, pin):
    msg = lib.get_secret(sid, pin)
    if len(msg) > 0:
        return '{ "msg": "' + msg + '"}'
    else:
        return '{"error":"not found"}'
