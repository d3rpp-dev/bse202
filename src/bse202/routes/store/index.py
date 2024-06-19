"""
The root page for the games store

will contain the games list
"""

from flask import render_template, g, url_for
from sqlite3 import DatabaseError

from .blueprint import store_blueprint
from ...db import get_db

import json


@store_blueprint.get("/")
def store_root():
    """
    is this slow? yes

    is it slow enough to actually have an
    effect at a small scale? no

    do i care? no
    """

    db = get_db()

    error = None

    try:
        query = """--sql
        SELECT
            cats.category_id,
            cats.title,
            cats.description
        FROM
            categories as cats
        """

        cats = list(
            map(
                lambda tup: {
                    "category_id": tup[0],
                    "title": tup[1],
                    "description": tup[2],
                    "slug": "%s-category" % tup[1].lower().replace(" ", "-"),
                },
                db.execute(query).fetchall(),
            )
        )

    except DatabaseError as ex:
        error = {
            "kind": "server",
            "code": "get_categories",
            "message": f"Failed to get Game Categories List - {ex}",
        }

    for idx, category in enumerate(cats):
        try:
            query = """--sql
            SELECT
                games.game_id,
                games.title,
                games.description,
                games.price,

                assets.asset_id
            FROM
                game_categories_link as links
            RIGHT JOIN
                games
            ON
                games.game_id = links.game_id
            RIGHT JOIN
                game_assets as assets
            ON
                games.game_id = assets.game_id
            WHERE
                links.category_id = ?1
            """

            category["games"] = list(
                map(
                    lambda tup: {
                        "game_id": tup[0],
                        "title": tup[1],
                        "description": tup[2],
                        "price": tup[3],
                        "image_id": tup[4],
                    },
                    db.execute(query, (category["category_id"],)).fetchall(),
                )
            )

            cats[idx] = category

            print(cats[idx])
        except DatabaseError as ex:
            error = {
                "kind": "server",
                "code": "get_categories",
                "message": f"Failed to get Games List - {ex}",
            }
            break

    return render_template("views/store.html", error=error, product_categories=cats)
