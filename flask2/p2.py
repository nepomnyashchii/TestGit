from flask import Flask
from flask import jsonify
import lib

app = Flask(__name__)
@app.route('/ml_2_oz/<float:ml>')
def ml_2_oz(ml):
    return jsonify(lib.ml_to_oz(ml))
    # return lib.ml_to_oz(ml)

# app = Flask(__name__)
# @app.route('/oz_2_ml/<float:oz>')
# def oz_2_ml (oz):
#     return lib.oz_to_ml(oz)

