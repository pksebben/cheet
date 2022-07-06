# from https://maxhalford.github.io/blog/flask-sse-no-deps/
import flask
import queue

app = flask.Flask(__name__)

class CheetDisplay:

    def __init__(self, template = "basic.j2"):
        self.master_cheetlist = []
        self.current_cheets = []
        self.template = template

    def render_cheetsheet():
        rendered = flask.render_template(self.template, self.cheetlist)
        return rendered

    def by_tag(self, tag):
        self.current_cheets = []
        for cheet in self.master_cheetlist:
            if tag in cheet['tags']:
                self.current_cheets.append(cheet)
        return self.render_cheetsheet()

    def by_context(self, context):
        self.current_cheets = []
        for cheet in self.master_cheetlist:
            if cheet.context == context:
                self.current_cheets.append(cheet)
        return self.render_cheetsheet()



class MessageAnnouncer:

    def __init__(self):
        self.listeners = []

    def listen(self):
        q = queue.Queue(maxsize=5)
        self.listeners.append(q)
        return q

    def announce(self, msg):
        for i in reversed(range(len(self.listeners))):
            try:
                self.listeners[i].put_nowait(msg)
            except queue.Full:
                del self.listeners[i]


announcer = MessageAnnouncer()

@app.route('/')
def home():
    return 'make me a website, he said!'

@app.route('/ping')
def ping():
    msg = format_sse(data='pong')
    announcer.announce(msg=msg)
    return {}, 200

@app.route('/listen')
def listen():

    def stream():
        messages = announcer.listen()
        while True:
            msg = messages.get()
            yield msg

    return flask.Response(stream(), mimetype="text/event-stream")

class CheetUpdate:

    def __init__(self):
        self.listeners = []

    def listen(self):
        q = queue.Queue(maxsize=5)
        self.listeners.append(q)
        return q

    def announce(self, msg):
        for i in reversed(range(len(self.listeners))):
            try:
                self.listeners[i].put_nowait(msg)
            except queue.Full:
                del self.listeners[i]

def format_sse(data: str, event=None):
    msg = f'data: {data}\n\n'
    if event is not None:
        msg = f'event: {event}\n{msg}'
    return msg

if __name__ == "__main__":
    app.run()
