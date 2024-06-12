from sqlite3 import DatabaseError
from flask import g

from ...db import get_db

from .blueprint import games_blueprint


# i hate CSRF sometimes
#
# we're going to live with it
@games_blueprint.get("/add_cart/<int:game_id>")
def add_item_to_cart(game_id: int):
	if "token" in g:
		db = get_db()
		cur = db.cursor()

		try:
			query = """--sql
				INSERT INTO
					`carts` (`user_id`, `game_id`)
				VALUES
					(?1, ?2)
			"""

			cur.execute(query, (g.token["user_id"], game_id))

			db.commit()

			return "Done!", 200
		except DatabaseError as ex:
			db.rollback()
			print(ex)
			return "Failed :(", 500
	else:
		return "No.", 400