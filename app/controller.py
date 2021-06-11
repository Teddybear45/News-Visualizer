from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    print(name)
    return render_template('hello.html', name=name)


# only send coords and name, not urls until requested


