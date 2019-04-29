from flask import Flask
# print(__name__)
app = Flask(__name__)


# @app.route('/')
# def index():
#     return 'Index Page'


# @app.route('/hello')
# def hello():
#     return 'Hello, World'


# @app.route("/hello2")
# def hello2():
#     return "I lova all"


@app.route('/source/<sourceName>')
def source_by_name(sourceName):
    if sourceName == 'cnn' or sourceName == 'bbc':
        return 'hurray'
    else:
        return 'bad source'


# @app.route('/put/<msg>/<int:pin>/<int:exp>')
# def put(msg, pin, exp):
#     return 'msg = ' + msg + "  pin= " + str(pin) + " exp = " + str(exp)


# @app.route('/get/<sid>/<int:pin>')
# def get(sid, pin):
#     # lib.get_secret(sid, pin)
#     return 'sid = ' + sid + "  pin= " + str(pin)


# @app.route('/sources')
# def sources():
#     # show the user profile for that user
#     return 'cnn, bbc'


# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id


# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % subpath


# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/project')
# def projects1():
#     return 'The project page1'


# @app.route('/about')
# def about():
#     return 'The about page'
