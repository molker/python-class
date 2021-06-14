from flask import Flask, render_template
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:file_name>')
def routes(file_name=None):
    return render_template(file_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(
            f'\nEmail: {email},\nSubject: {subject},\nMessage: {message}\n')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('./thankyou.html')
    else:
        return 'something went wrong. try again'
