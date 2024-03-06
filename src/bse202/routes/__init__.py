from flask import render_template

from bse202.app import app

@app.route("/")
@app.route("/<name>")
def hello(name = None):
    template = render_template("index.html", name=name)
    return template