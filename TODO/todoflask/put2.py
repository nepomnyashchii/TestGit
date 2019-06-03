from flask import Flask, jsonify, request
import libput2

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

print("\n\n\n\n\n\n\n\n\n\n")


@app.route('/')
def index():
    return 'Flow Runner :)'

@app.route('/<int:id>', methods = ['PUT'])
def update_todo(id):
    updated = libput2.update_todo_by_id(id, "FFF", 2)
    print(updated)
    data = request.json
    print(data)
    return jsonify(
        data=data,
    )
