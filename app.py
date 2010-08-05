import sys
sys.path.append('lib')

from flask import Flask
from flask import render_template

# if necessary
# from flask import redirect, url_for, session, request,\
#   abort, flash, get_flashed_messages, g, Response\

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    from wsgiref.handlers import CGIHandler
    CGIHandler().run(app)
