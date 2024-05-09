from flask import render_template
from .blueprint import root_blueprint


@root_blueprint.get("/")
def index():
    template = render_template("views/home.html")
    return template
