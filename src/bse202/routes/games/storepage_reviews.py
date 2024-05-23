from flask import render_template, g
from sqlite3 import DatabaseError
from time import sleep

from .blueprint import games_blueprint
from ...db import get_db


@games_blueprint.get("/<int:game_id>/reviews")
def game_storepage_reviews(game_id: int):
    # artificially delay to let lazy loading look nice
	# Todo: remove later
	sleep(1.5)
	return render_template(f"{g.template_prefix}games/snippets/reviews.html")
