"""
*NOTE* This is a snippet endpoint

This means the template it renders is not a whole page
and the HTML this returns is not a page, but a snippet meant
to be inserted into a valid HTML doc (in this case, via HTMX)
"""

from sqlite3 import DatabaseError
from flask import render_template, g
from time import sleep

from .blueprint import games_blueprint
from ...db import get_db


@games_blueprint.get("/<int:game_id>/reviews")
def game_storepage_reviews_snippet(game_id: int):
    # artificially delay to let lazy loading look nice
    # Todo: remove later
    sleep(1.5)
    return render_template(f"{g.template_prefix}games/snippets/reviews.html")


@games_blueprint.get("/cart")
def cart_snippet():
    if "token" in g:
        user_id = g.token["user_id"]

        try:
            query = """--sql
                SELECT
                    games.game_id,
                    games.title,
                    games.price
                FROM
                    carts
                RIGHT JOIN
                    games on games.game_id = carts.game_id
                WHERE
                    carts.user_id = ?1
                LIMIT
                    50
            """

            query_result = get_db().execute(query, (user_id,)).fetchall()

            cart = list(map(
                lambda a: { "game_id": a[0], "title": a[1], "price": a[2] },
                query_result
            ))

            cart_total = sum([a["price"] for a in cart if "price" in a])

            print(cart)

            return render_template(
                f"{g.template_prefix}games/snippets/cart.html",
                cart=cart,
                cart_total=cart_total
            )
        except DatabaseError as ex:
            return render_template(
                f"{g.template_prefix}games/snippets/cart.html",
                 error={
                    "kind": "server",
                    "code": "cart_snippet_query_error",
                    "message": f"Internal Server Error - {ex}",
                },
            )
        
        # logged in
        
    else:
        return "", 404 