from flask import Flask
import vsearch  #

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask'


###最大行數: 3行
@app.route('/search4')
def do_search() -> str:
    return str(vsearch.search4letters("life,the universe,and everything!", "eiru,!"))

###
