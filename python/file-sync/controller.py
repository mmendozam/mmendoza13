from flask import Flask
from pathlib import Path
from scanner import FileSync, scan


# To run:
# set PYTHONPATH=E:\local\GitHub\mmendozam\mmendoza13\python\file-sync
# flask --app controller run


class State:
    def __init__(self) -> None:
        self.scanning = False
        self.content: list[FileSync] = []


class Response:
    def __init__(self) -> None:
        self.status = None
        self.data = None


app = Flask(__name__)


STATE = State()


@app.route('/status')
def status():
    return STATE.__dict__


@app.route('/content')
def content():
    response = Response()

    if STATE.content:
        response.status = 'cached content'
        response.data = [c.__dict__ for c in STATE.content]
    elif not STATE.scanning:
        STATE.scanning = True
        response.status = 'started scan'
        path = Path('E:/NNLK_HOME')
        STATE.content = scan(path)
        response.data = [c.__dict__ for c in STATE.content]
        STATE.scanning = False
    else:
        response.status = 'scan is running, wait until it is done'

    return response.__dict__
