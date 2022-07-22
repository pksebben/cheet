import queue
import webbrowser

import flask
from flask import render_template, request

# cheet internals
from config import config

# blueprints
from views.api import api
from views.web_interface import interface
from views.display import display
from views.editpage import editpage

app = flask.Flask(__name__)
DEBUG = True

app.register_blueprint(api)
app.register_blueprint(interface)
app.register_blueprint(display)
app.register_blueprint(editpage)


if __name__ == "__main__":
    if not DEBUG:
        webbrowser.get().open('http://localhost:8765')
    app.run(debug=DEBUG, port="8765")
