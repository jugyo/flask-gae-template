#
# Flask Documentation:      http://flask.pocoo.org/docs/
# Jinja2 Documentation:     http://jinja.pocoo.org/2/documentation/
# Werkzeug Documentation:   http://werkzeug.pocoo.org/documentation/
# The Python Datastore API: http://code.google.com/appengine/docs/python/datastore/
#

from flask import Flask, url_for, render_template, request, redirect
from models import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', todos=Todo.all().order('-created_at'))

@app.route('/add', methods=["POST"])
def add():
    todo = Todo(text=request.form['text'])
    todo.save()
    return redirect(url_for('index'))
