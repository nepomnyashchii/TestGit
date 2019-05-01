from flask import Flask, jsonify, request, make_response

app=Flask(__name__)

@app.route("/json", methods=["POST"])

# def json():
#     return "Thanks", 200

def json():
    req=request.get_json()
    print(type(req)
    print(re)


# def json():
#     if request.is_json:
#         req= request.get_json()
#         print()
#         return "JSON received", 200
#     else:
#         return "No JSON received", 400





























