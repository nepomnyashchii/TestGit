from flask import Flask
import lib

app = Flask(__name__)
@app.route('/put/<int:ml>/')
def put(ml):
    return lib.oz_to_ml(ml)