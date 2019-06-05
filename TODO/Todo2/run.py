
from flask import Flask, request, jsonify
import lib

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

print("\n\n\n\n\n\n\n\n\n\n")


@app.route('/')
def index():
    return 'Flow Runner :)'
# get data through todo (not forget to transfer obtained tupple to the string)

@app.route('/todo')
def get_todo():
    all_data = lib.get_all()
    print(all_data)
    return str(all_data)

@app.route('/todo/<int:id>')
def get_all(id):
    id_data = lib.get_todo_by_id(id)
    print(id_data)
    return str(id_data)

@app.route('/todo', methods = ['POST'])
def insert_todo():
    new_id = lib.insert_todo("jopa")
    print(new_id)
    data = request.json
    print(data)
    return jsonify(
        data=data,
    )
@app.route('/todo/<int:id>', methods = ['PUT'])
def update_delete_todo(id):
    updated = lib.update_todo_by_id(id, "FFF", 100)
    print(updated)
    data = request.json
    # delete_previous_id = lib.delete_todo_by_id(id-1)
    # print (delete_previous_id)
    print(data)
    return jsonify(
        data=data,
    )


# {
#     text:"asdasd",
#     done:true
# }



