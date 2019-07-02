from flask import Flask, jsonify
import libget2

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

print("\n\n\n\n\n\n\n\n\n\n")


@app.route('/')
def index():
    return 'Flow Runner :)'


@app.route('/todo/<int:id>')
def get_todo(id):
    data = libget2.get_todo(id)
    print(data)
    return str(data)
