import sys
sys.path.append('lib')

from flask import Flask

# if necessary
# from flask import redirect, url_for, session, request,\
#   render_template, abort, flash, get_flashed_messages, g, Response\

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    from wsgiref.handlers import CGIHandler
    CGIHandler().run(app)
