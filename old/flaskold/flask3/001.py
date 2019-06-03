from flask import Flask
from flask import request
# print(__name__)
app = Flask(__name__)

@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'
        
# ?name=Alec
