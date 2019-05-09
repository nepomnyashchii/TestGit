from flask import Flask, request, json, jsonify
# print(__name__)
app = Flask(__name__)
username ="bolshaya"
flow="jopa"
ale= {"flow": flow, "username": username}

@ app.route("/run/alex/")
def alex():
    return ale

