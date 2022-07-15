import queue

import flask
from flask import render_template, request

# cheet internals
from core.cheet import Cheet
from db import db

# blueprints
from api import api
from web_interface import interface
from display import display
from editpage import editpage

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

@app.route('/')
def home():
    page = render_template("basic.j2", cheets = db.cheets)
    return page

if __name__ == "__main__":
    app.run(debug=True, port="8765")
