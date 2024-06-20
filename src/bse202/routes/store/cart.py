from flask import render_template, redirect, url_for, g, request
from sqlite3 import DatabaseError

from .blueprint import store_blueprint
from ...db import get_db


@store_blueprint.get("/cart")
def cart():
    # authenticated
    if "token" not in g:
        return redirect(url_for("auth.login"))
    
    error = None

    user_id: str = g.token['user_id']

    db = get_db()

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
                    "image_id": tup[4]
                },
                db.execute(query, (user_id,)).fetchall()
            )
        )

        cart_total = 0

        for item in cart:
            cart_total += item["price"]

    except DatabaseError as ex:
        print(ex)
        error = {
            "kind": "server",
            "code": "fetch_cart",
            "message": "Failed to get Cart - {ex}"
        }

    return render_template(
        "views/cart.html", 
        cart_items = cart,
        cart_total = cart_total,

        error = error
    )


@store_blueprint.post("/add_to_cart")
def add_to_cart():
    # authenticated
    if "token" not in g:
        return redirect(url_for("auth.login"))

    if request.form.get("product_id") is None:
        return "no product", 400

    db = get_db()
    cur = db.cursor()

    try:
        query = """--sql
        SELECT
            *
        FROM
            cart_items as item
        WHERE
            item.user_id = ?1 AND item.game_id = ?2
        """

        if db.execute(
            query, (g.token["user_id"], int(request.form.get("product_id")))  # type: ignore
        ).fetchall().__len__() > 0:
            # do not add, already there
            return redirect(url_for("store.store_root"))

        query = """--sql
        INSERT INTO
            cart_items (`user_id`, `game_id`)
        VALUES
            (?1, ?2)
        """

        cur.execute(
            query,
            (g.token["user_id"], int(request.form.get("product_id"))),  # type: ignore - ive already checked if its not there
        )

        db.commit()
    except DatabaseError as ex:
        print(ex)
        return "Failed to add to cart"

    return redirect(url_for("store.cart"))


@store_blueprint.post("/remove_from_cart")
def remove_from_cart():
    return redirect(url_for("store.cart"))
