from flask import Flask, jsonify
import lib

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

print("\n\n\n\n\n\n\n\n\n\n")


@app.route('/')
def index():
    return 'Flow Runner :)'


@app.route('/todo')
def get_todo():
    data = lib.get_todo()
    print(data)
    return str(data)

# data = lib.get_todo()
# print(data)