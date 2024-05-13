"""
Handler for `/`, this is the landing page
"""

from flask import render_template
from .blueprint import root_blueprint


@root_blueprint.get("/")
def index():
    template = render_template("index.html")
    return template
