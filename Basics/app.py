from flask import url_for
from typing import ForwardRef
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<p>Hello World! From Giridhar at Flask Tutorials</p>"

# injection attacks are avoided using this


@app.route('/<name>')
def hello(name):
    return f"Hello, {escape(name)}!"

# routing


@app.route('/index')
def index():
    return 'Index Page'


@app.route('/hello')
def helloWorld():
    return 'Hello, World'

# Variable types


@app.route('/user/<username>')
def show_user_profile(username):
    return f'Hi there: {escape(username)}'


@app.route('/post/<int:id>')
def show_post_id(id):
    id = id + 100
    return f'This post id is: {escape(id)}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

# Unique URLs / Redirection Behaviour


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


# url for function


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
