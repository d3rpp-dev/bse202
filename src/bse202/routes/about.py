from flask import render_template
from .blueprint import root_blueprint


@root_blueprint.get("/about")
def about_page():
    return render_template("views/about.html")
