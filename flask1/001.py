from flask import Flask
# print(__name__)
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route("/hello2")
def hello2():
    return "I lova all"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath




# @app.route('/projects/')
# def projects():
#     return 'The project page'

@app.route('/projects')
def projects1():
    return 'The project page1'

@app.route('/about')
def about():
    return 'The about page'