from flask import render_template, redirect, url_for, g
from datetime import datetime
from sqlite3 import DatabaseError

from .blueprint import store_blueprint
from ...db import get_db

@store_blueprint.get("/order_summary/<purchase_id>")
def order_summary(purchase_id: str):
    # Protected
    if "token" not in g:
        redirect(url_for("auth.login"))

    items = []
    total_price = 0
    error = None

    db = get_db()

    try:
        query = """--sql
        SELECT
            purchases.game_id,
            purchases.purchased_at,
            games.title,
            games.price,
            game_assets.asset_id
        FROM
            purchases
        RIGHT JOIN
            games
        ON
            games.game_id = purchases.game_id
        RIGHT JOIN
            game_assets
        ON
            games.game_id = game_assets.game_id
        WHERE
            purchases.purchase_id = ?1
        """

        items = list(
            map(
                lambda tup: {
                    "game_id": tup[0],
                    "purchased_at": datetime.fromtimestamp(tup[1]).strftime(
                        "%d/%m/%Y - %H:%M"
                    ),
                    "title": tup[2],
                    "price": tup[3],
                    "image_id": tup[4],
                },
                db.execute(query, (purchase_id,)).fetchall(),
            )
        )

        for i in items:
            total_price += i["price"]  # type: ignore

    except DatabaseError as ex:
        print(ex)
        error = {
            "kind": "server",
            "code": "order_summary_get_purchased_items",
            "message": f"Failed to get purchase - {ex}",
        }
        return render_template("views/order_summary.html", error=error)

    return render_template(
        "views/order_summary.html", items=items, total_price=total_price
    )
