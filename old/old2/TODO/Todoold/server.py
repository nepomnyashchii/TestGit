
from flask import Flask, request, jsonify
import json
import lib
import logger_module
import json


logger = logger_module.setup_logger("todo")
logger.debug('Start my super App')
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
print("\n\n\n")



@app.route('/')
def index():
    return 'Flow Runner :)'
# get data through todo (not forget to transfer obtained tuple to the string)

@app.route('/todo')
def get_todo():
    logger.debug('run invoked')
    all_data = lib.get_all()
    # rs = json.dumps(all_data)
    respond = json.loads(all_data)
    logger.debug("get information from all ids: " + str(respond))
    # print(respond)
    return jsonify(data= respond)

@app.route('/todo/<int:id>')
def get_all(id):
    logger.debug("Get all information by id")
    id_data = lib.get_todo_by_id(id)
    respond =json.loads(id_data)
    logger.debug("Provide all information for asked id: " + str(respond))
    return jsonify(data= respond)

@app.route('/todo', methods=['POST'])
def insert_todo():
    logger.debug("Insert is invoked")
    result = request.json
    print(result)
    data = result["text"]
    logger.debug("Information from the body: " + str(data))
    print(data)
    new_id = lib.insert_todo(data)
    logger.debug("Inserted id: " + str(new_id))
    print(new_id)
    return jsonify(id=new_id)

@app.route('/todo/<int:id>', methods = ['PUT'])
def update_todo(id):
    result= request.json
    logger.debug("Information from the body: " +str(result))
    print(result)
    new_result=result["text"]
    print(new_result)
    logger.debug("Information for updated text from dictionary: " + str(new_result))
    new_data=result["done"]
    logger.debug("Information for true or false from dictonary: " + str(new_data))
    new_information_id = lib.update_todo_by_id(id, new_result, new_data)
    logger.debug("updated id: " + str(new_information_id))
    print(new_information_id)
    return jsonify(id= new_information_id)

@app.route('/todo/<int:id>', methods =['DELETE'])
def delete_todo(id):
    delete_id = lib.delete_todo_by_id(id)
    logger.debug("Requested operation to delete the data successfully accomplished")
    return jsonify(id="data successfully deleted")


@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'URL is wrong: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

# {
#     "text":"asdasd",
#     "done":true
# }

# {"text":"asdasdasd"}


