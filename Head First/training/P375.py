from flask import Flask, session

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp'


@app.route('/page1')
def page1() -> str:
    return 'This is page 1'


@app.route('/page2')
def page2() -> str:
    return 'This is page 2'


@app.route('/page3')
def page3() -> str:
    return 'This is page 3'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


app.secret_key = 'YouWillNeverGuessMySecretKey'
