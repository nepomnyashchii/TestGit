from flask import Flask

app = Flask(__name__)
@app.route('/Hello/Poka')
def index():
    return "zenit champion"