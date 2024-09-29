from flask import Flask
from pathlib import Path
import datetime
from scanner import FileSync, scan


# To run:
# set PYTHONPATH=E:\local\GitHub\mmendozam\mmendoza13\python\file-sync
# flask --app controller run

class State:
    def __init__(self) -> None:
        self.running = False
        self.content: list[FileSync] = []
        self.date: str = None


app = Flask(__name__)

STATE = State()


def get_data() -> dict[str, object]:
    return {
        'date': STATE.date,
        'data': [c.__dict__ for c in STATE.content]
    }


@app.route('/content')
def content() -> dict[str, object]:
    if not STATE.content and not STATE.running:
        STATE.running = True
        STATE.content = scan(Path('E:/NNLK_HOME'))
        STATE.date = datetime.datetime.now()
        STATE.running = False

    return get_data()
