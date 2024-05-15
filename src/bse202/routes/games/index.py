from flask import render_template
from .blueprint import games_blueprint


@games_blueprint.get("/")
def games_root():
    return render_template("games/index.html")
