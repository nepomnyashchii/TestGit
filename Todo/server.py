from flask import Flask, jsonify
import lib

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

print("\n\n\n\n\n\n\n\n\n\n")


@app.route('/')
def index():
    return 'Flow Runner :)'


# @app.route('/todo')
# def get_todo():
#     data = lib.get_todo()
#     print(data)
#     return str(data)

# @app.route('/todo/<int:id>')
# def get_todo(id):
#     data = lib.get_todo(id)
#     print(data)
#     return str(data)


# data = lib.get_todo()
# print(data)

# @app.route('/todo/<user>', methods = ['POST'])
# def insert_todo(user):
#     user = {"text":"asdasdasd"}
#     data = lib.insert_todo(user)
#     print(data)
#     return(str(data))

@app.route('/todo', methods = ['POST'])
def insert_todo():
    data = request.json
    print(data)
    return jsonify(
        data=data,
    )

INSERT INTO `todo` (`id`, `text`, `done`, `created`) VALUES (NULL, %s, '0', CURRENT_DATE());
