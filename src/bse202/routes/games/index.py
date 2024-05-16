from flask import render_template, g
from .blueprint import games_blueprint


@games_blueprint.get("/")
def games_root():
    return render_template(f"{g.template_prefix}games/index.html")
