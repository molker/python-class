from flask import Flask, render_template
from flask.helpers import send_from_directory
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return 'This is a blog'
