"""
Handler for `/`, this is the landing page
"""

from flask import render_template, g
from .blueprint import root_blueprint


@root_blueprint.get("/")
def index():
    template = render_template(f"{g.template_prefix}views/home.html")
    return template
