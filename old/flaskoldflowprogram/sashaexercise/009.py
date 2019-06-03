from flask import Flask, request, jsonify, json
import datetime, time
created_time = datetime.datetime.utcnow()
created_time = "created time"
app = Flask(__name__)

@ app.route("/run/alex/goodmorning")
def good_morning():
    alex= {"scriptName": "goodmorning",
    "description": "Dedicated server for web hosting",
    "status": "active",
    "created_time"
    "data": {
        "norris": [
            "Who let the dogs out? Chuck Norris let the dogs out and then roundhouse kicked them through an Oldsmobile.",
            "When Chuck Norris is in a crowded area, he doesn't walk around people. He walks through them.",
            "Product Owners never argue with Chuck Norris after he demonstrates the DropKick feature."
        ],
        "news": [
        	"Last week we made a fairly quiet (too quiet, in fact) announcement of our plan to slowly and carefully deprecate the path-based access model that is used to specify the address of an object in an S3 bucket. I spent some time talking to the S3 team in order to get a better understanding of",
            "For Better Computing, Liberate CPUs From Garbage Collection",
            "Dr. Moncef Kartas is a member of a UN panel of experts investigating violations of the UN arms embargo on Libya."
        	]
    }
}
    return jsonify(alex)





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


current_time = datetime.datetime.now()