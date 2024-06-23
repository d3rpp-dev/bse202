from flask import render_template, g, redirect, url_for, request
from sqlite3 import DatabaseError

from ...db import get_db
from .blueprint import store_blueprint


@store_blueprint.route("/checkout", methods=["GET", "POST"])
def checkout():
    # authenticated
    if "token" not in g:
        return redirect(url_for("auth.login"))

    user_id = g.token["user_id"]
    db = get_db()

    error = None

    if request.method == "GET":
        cart = []
        cart_total = 0

        try:
            query = """--sql
            SELECT
                items.game_id,

                games.title,
                games.description,
                games.price,

                game_assets.asset_id
            FROM 
                cart_items as items
            RIGHT JOIN
                games
            ON
                items.game_id = games.game_id
            RIGHT JOIN
                game_assets
            ON
                items.game_id = game_assets.game_id
            WHERE
                items.user_id = ?1
            """

            cart = list(
                map(
                    lambda tup: {
                        "game_id": tup[0],
                        "title": tup[1],
                        "description": tup[2],
                        "price": tup[3],
                        "image_id": tup[4],
                    },
                    db.execute(query, (user_id,)).fetchall(),
                )
            )

            for item in cart:
                cart_total += item["price"]
        except DatabaseError as ex:
            error = {
                "kind": "server",
                "code": "checkout_get_db",
                "message": f"failed to fetch users cart - {ex}",
            }

        return render_template(
            "views/checkout.html", error=error, cart_items=cart, cart_total=cart_total
        )

    else:
        method = request.form.get("payment_method")
        if method is None:
            return "No Payment Method", 400

        if method == "credit_card":
            # credit/debit card
            return redirect(url_for("store.payment"))
        else:
            # vault coin
            return redirect(url_for("store.vault_payment"))
