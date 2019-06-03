from flask import Flask, jsonify
import lib

app = Flask(__name__)


@app.route("/")
def root():
    return jsonify(answer="Hello World1!")


@app.route("/a")
def hello():
    return "Hello a!"


@app.route('/ml_2_oz/<float:ml>')
def ml_2_oz(ml):
    return jsonify(answer=lib.ml_to_oz(ml))


@app.route('/oz_2_ml/<float:oz>')
def oz_2_ml(oz):
    return jsonify(answer=lib.oz_to_ml(oz))


@app.route('/ml_2_oz/<int:ml>')
def ml_2_oz_int(ml):
    return jsonify(answer=lib.ml_to_oz(ml))


@app.route('/oz_2_ml/<int:oz>')
def oz_2_ml_int(oz):
    return jsonify(answer=lib.oz_to_ml(oz))
