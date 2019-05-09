import flask
from flask import request, jsonify

app = flask.Flask(__name__)


app.config["DEBUG"] = True

alex= {"scriptName": "goodmorning",
    "description": "Dedicated server for web hosting",
    "status": "active",
    "created_time": "2019-04-05 17:38:06",
    "data": {
        "norris": [
            "string1",
            "string2",
            "string3"
        ],
        "news": [
        	"string1",
            "string2",
            "string3"
        	]
    }
}
@ app.route("/run/alex/goodmorning")
def good_morning():
    return jsonify (alex)
# app.run()


# {{ApiUrl}}/run/alex/goodmorning




#     "data": {
#         "norris": [
#             "string1",
#             "string2",
#             "string3"
#         ],
#         "news": [
#         	"string1",
#             "string2",
#             "string3"
#         	]
#     }
# }
#


    # print(a+data)

# response {
#     "scriptName": "goodmorning",
#     "description": "Dedicated server for web hosting",
#     "status": "active",
#     "created_time": "2019-04-05 17:38:06",
#     "data": {
#         "norris": [
#             "string1",
#             "string2",
#             "string3"
#         ],
#         "news": [
#         	"string1",
#             "string2",
#             "string3"
#         	]
#     }
# }



