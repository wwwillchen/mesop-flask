import os
from typing import Any, Callable
import mesop as me
import mesop.labs as mel
from flask import Flask, send_from_directory
from pydantic import BaseModel
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

app = Flask(__name__)


@app.route("/static/<path:path>")
def static_route(path: str):
    return send_from_directory("static", path)


@me.stateclass
class State:
    count: int = 0
    value: str


def increment(event: me.ClickEvent):
    state = me.state(State)
    state.count += 1


@me.page()
def page():
    state = me.state(State)
    me.text(f"count={state.count}")
    me.button("Increment", on_click=increment, type="flat")
    me.text("Image loaded from Flask server")
    me.image(src="sub/static/image.jpg")


combined_app = DispatcherMiddleware(
    me.create_wsgi_app(debug_mode=os.environ.get("DEBUG_MODE", "") == "true"),
    {"/sub": app},
)

if __name__ == "__main__":
    run_simple("localhost", 32123, combined_app, use_reloader=True, use_debugger=True)
