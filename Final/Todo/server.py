
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
    logger.debug("Request for testing connection invoked")
    return 'Todo Experience :)'

@app.route('/todo', methods=['GET'])
def get_todo():
    logger.debug('Run invoked to obtain data for all ids')
    all_data = lib.get_all()
    logger.debug("Data for all ids" + str(all_data))
    return jsonify(data=all_data)


@app.route('/todo/<int:id>', methods=['GET'])
def get_all(id):
    logger.debug("Run invoked to obtain data by id")
    id_data = lib.get_todo_by_id(id)
    logger.debug("Data for asked id: " + str(id_data))
    return jsonify(data=id_data)

@app.route('/todo', methods=['POST'])
def insert_todo():
    logger.debug("Run invoked to insert data with new id to the database")
    result = request.json
    logger.debug("Json new_data from the dictionary in the body" + str(result))
    data = result["text"]
    username = result["username"]
    logger.debug("Data from the body: " + str(data))
    new_id = lib.insert_todo(data, username)
    logger.debug("Inserted id: " + str(new_id))
    return jsonify(id=new_id)


@app.route('/todo/<int:id>', methods=['PUT'])
def update_todo(id):
    logger.debug("Run invoked to update data with new id to the database")
    result = request.json
    logger.debug("Data from the body: " + str(result))
    new_result = result["text"]
    logger.debug("Data for updated text from dictionary: " + str(new_result))
    new_data = result["done"]
    logger.debug("Data for true or false from dictonary: " + str(new_data))
    new_information_id = lib.update_todo_by_id(id, new_result, new_data)
    logger.debug("Updated id: " + str(new_information_id))
    return jsonify(id=new_information_id)


@app.route('/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    logger.debug("Run invoked to delete data for certain id from the database")
    delete_id = lib.delete_todo_by_id(id)
    logger.debug(
        "Requested operation to delete the data successfully accomplished")
    return jsonify(id="Data successfully deleted")


@app.errorhandler(404)
def not_found(error=None):
    logger.debug("Start app.errorhandler to confirm status 404")
    message = {
        'status': 404,
        'message': 'URL is wrong: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.errorhandler(405)
def invalid_method(error=None):
    logger.debug("405 errorhandler invoked for:" + request.url)
    message = {
        'status': 405,
        'message': '405 Method Not Allowed: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 405
    logger.debug("Status 405 found with errorhandler")
    return resp


# {
#     "text":"asdasd",
#     "username": "alex"
#     "done":true
# }

# {"text":"asdasdasd"}
