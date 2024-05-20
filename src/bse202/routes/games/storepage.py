from flask import render_template, g, url_for
from sqlite3 import DatabaseError

from .blueprint import games_blueprint
from ...db import get_db


@games_blueprint.get("/<int:game_id>")
def game_store_page(game_id: int):
    return render_template(f"{g.template_prefix}games/storepage.html")
