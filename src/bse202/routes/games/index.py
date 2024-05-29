"""
The root page for the games store

will contain the games list
"""

from flask import render_template, g, url_for
from sqlite3 import DatabaseError

from .blueprint import games_blueprint
from ...db import get_db


@games_blueprint.get("/")
def games_root():
    """
    is this slow? yes

    is it slow enough to actually have an
    effect at a small scale? no

    do i care? no
    """
    db = get_db()

    try:
        query = """--sql
        SELECT
            game_id,
            title,
            description
        FROM
            games
        LIMIT
            20
        """
        games_list_result: list[tuple[int, str, str]] = db.execute(query).fetchall()
    except DatabaseError as ex:
        return render_template(
            f"{g.template_prefix}games/index.html",
            error={
                "kind": "server",
                "code": "initial_game_query_failed",
                "message": f"SQL Error - {ex}",
            },
        )

    # this, ladies and gentleman is why i don't like python
    game_ids: list[str] = [str(i[0]) for i in games_list_result]

    try:
        query = f"""--sql
        SELECT
            asset_id,
            game_id
        FROM
            game_assets
        WHERE
            game_id IN ({', '.join(game_ids)})
        """
        asset_list: list[tuple[int, int]] = db.execute(query).fetchall()
    except DatabaseError as ex:
        return render_template(
            f"{g.template_prefix}games/index.html",
            error={
                "kind": "server",
                "code": "initial_game_query_failed",
                "message": f"SQL Error - {ex}",
            },
        )

    games_list_with_associated_assets = []

    for game in games_list_result:
        for i in asset_list:
            if game[0] == i[1]:
                games_list_with_associated_assets.append(
                    {
                        "game_id": game[0],
                        "title": game[1],
                        "description": game[2],
                        "banner": url_for("static", filename=f"assets/{i[1]}.jpg"),
                        "page": url_for("games.game_store_page", game_id=game[0]),
                    }
                )

    return render_template(
        f"{g.template_prefix}games/index.html", games=games_list_with_associated_assets
    )
