from flask import render_template, g, url_for
from sqlite3 import DatabaseError

from .blueprint import games_blueprint
from ...db import get_db


@games_blueprint.get("/<int:game_id>")
def game_store_page(game_id: int):
    db = get_db()

    try:
        query = """--sql
		SELECT
			game_id,
			title,
			description
		FROM
			games
		WHERE
			game_id = ?1
		"""

        game_query_result: tuple[int, str, str] = db.execute(
            query, [game_id]
        ).fetchone()
    except DatabaseError as ex:
        return render_template(
            f"{g.template_prefix}games/storepage.html",
            error={
                "kind": "server",
                "code": "storepage_database_error_game",
                "message": f"SQL Error - {ex}",
            },
        )

    try:
        query = """--sql
		SELECT
			asset_id,
			description,
			asset_type
		FROM
			game_assets
		WHERE
			game_id = ?1
		"""

        game_assets_result: list[tuple[int, str, str]] = db.execute(
            query, [game_id]
        ).fetchall()
    except DatabaseError as ex:
        return render_template(
            f"{g.template_prefix}games/storepage.html",
            error={
                "kind": "server",
                "code": "storepage_database_error_assets",
                "message": f"SQL Error - {ex}",
            },
        )

    game_store_data = {
        "game_id": game_query_result[0],
        "title": game_query_result[1],
        "description": game_query_result[2],
        "assets": game_assets_result
	}

    return render_template(
        f"{g.template_prefix}games/storepage.html", 
        game=game_store_data,
        user=g.token if "token" in g else None
    )
