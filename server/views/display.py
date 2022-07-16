import queue

from flask import render_template, request, Blueprint, Response

from db import db

# from https://maxhalford.github.io/blog/flask-sse-no-deps/
"""Serves an SSE-based updating display of cheets"""

display = Blueprint('display', __name__,
                template_folder='templates')


class CheetDispatcher:
    """handles dispatch of the cheet sheet to the browser.  I need to
    better understand how this works"""

    def __init__(self):
        self.listeners = []
        self.selector = None

    def listen(self):
        q = queue.Queue(maxsize=5)
        self.listeners.append(q)
        return q

    def update(self):
        if selector is None:
            cheets = db.cheets
        else:
            cheets = db.get_by(selector[0], selector[1])
        msg = render_template("basic.j2", cheets = cheets)
        for i in reversed(range(len(self.listeners))):
            try:
                self.listeners[i].put_nowait(msg)
            except queue.Full:
                del self.listeners[i]


dispatcher = CheetDispatcher()


@display.route('/listen')
def listen():
    """registers a browser as a listener"""

    def stream():
        messages = dispatcher.listen()
        while True:
            msg = messages.get()
            yield msg

    return Response(stream())

# @api.route('/update/<id>', methods=["POST"])
def display_update(id):
    """updates display with selected cheets"""

    print(f"attempting to update {id}")
    print(request.data)
    msg = format_sse(data='pong')
    dispatcher.update()
    return "updated cheets", 200



def format_sse(data: str, event=None):
    msg = f'data: {data}\n\n'
    if event is not None:
        msg = f'event: {event}\n{msg}'
    return msg
