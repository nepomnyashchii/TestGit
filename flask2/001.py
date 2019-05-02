from flask import Flask
import lib

app = Flask(__name__)



@app.route('/')
def index():
    return 'Index Page'

@app.route('/ml_2_oz/<float:ml>')
def ml_2_oz(ml):
    return str(lib.ml_to_oz(ml))

app = Flask(__name__)
@app.route('/oz_2_ml/<float:oz>')
def oz_2_ml(oz):
    return str(lib.oz_to_ml(oz))

