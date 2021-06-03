from flask import Flask
from flask import request
from flask import url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return do_show_the_login()


def do_the_login():
    return f'Do the Login!'


def do_show_the_login():
    return f'Show the Login!'


with app.test_request_context():
    print(url_for('static', filename='test.txt'))
