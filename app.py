import sys
sys.path.append('lib')

from flask import Flask
from flask import render_template, request

# if necessary
# from flask import redirect, url_for, session,\
#   abort, flash, get_flashed_messages, g, Response\

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return render_template('hello.html', name=request.args.get('name'))

if __name__ == '__main__':
    from wsgiref.handlers import CGIHandler
    CGIHandler().run(app)
