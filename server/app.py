import queue

import flask
from flask import render_template, request

# cheet internals
from core.cheet import Cheet
from db import db

# blueprints
from views.api import api
from views.web_interface import interface
from views.display import display
from views.editpage import editpage

app = flask.Flask(__name__)

# Use me if requests are totes fucked
# @app.before_request
# def log_request_info():
    # app.logger.debug('Headers: %s', request.headers)
    # app.logger.debug('Body: %s', request.get_data())
    # app.logger.debug('Form: %s', [thing for thing in request.form.items()])

app.register_blueprint(api)
app.register_blueprint(interface)
app.register_blueprint(display)
app.register_blueprint(editpage)

if __name__ == "__main__":
    app.run(debug=True, port="8765")
