from flask import render_template, request, g, redirect, url_for
from sqlite3 import DatabaseError
from datetime import datetime
from ulid import ulid

from .blueprint import store_blueprint
from ...db import get_db


@store_blueprint.route("/vault_payment", methods=["GET", "POST"])
def vault_payment():
    # Protected
    if "token" not in g:
        redirect(url_for("auth.login"))

    user_id = g.token["user_id"]

    user_message = None
    error = None
    status = 200

    db = get_db()

    account_balance = None
    cart_total: float = 0
    cart_items = []

    ts = datetime.timestamp(datetime.now())

    try:
        query = """--sql
        SELECT
            account_balance
        FROM
            users
        WHERE
            user_id = ?1
        """

        account_balance = db.execute(query, (user_id,)).fetchone()[0]

        if account_balance is None:
            return "User not Found", 404

        query = """--sql
        SELECT
            games.price,
            games.game_id
        FROM
            cart_items
        RIGHT JOIN
            games
        ON
            cart_items.game_id = games.game_id
        WHERE
            cart_items.user_id = ?1
        """

        query = db.execute(query, (user_id,)).fetchall()

        for price, game_id in query:
            cart_items.append(game_id)
            cart_total += price

        if cart_total is None:
            cart_total = 0
        else:
            cart_total = round(cart_total, 2)

    except DatabaseError as ex:
        status = 500
        error = {
            "kind": "server",
            "code": "vault_payment_balance",
            "message": f"Failed to get User's Balance - {ex}",
        }

    # at this point, the vault payment method has been chosen
    #
    # We'll show
    #
    # - current balance
    # - cart price
    #
    # A top-up link will need to appear as will the complete payment link

    if request.method == "POST":
        # we've checked and know that account balance & cart total are not None
        # POST
        if len(cart_items) <= 0:
            user_message = "Cart is empty"

            return render_template(
                "views/vault_payment.html",
                user_message=user_message,
                error=error,
                account_balance=account_balance,
                cart_total=cart_total,
            ), status

        if account_balance < cart_total:  # type: ignore
            user_message = 'You don\'t have enough funds, press the "Top Up" button below to top it up'

            return render_template(
                "views/vault_payment.html",
                user_message=user_message,
                error=error,
                account_balance=account_balance,
                cart_total=cart_total,
            ), status
        else:
            cur = db.cursor()

            try:
                query = """--sql
                UPDATE
                    users
                SET
                    account_balance = ?1
                WHERE
                    user_id = ?2
                """

                cur.execute(query, (account_balance - cart_total, user_id))  # type: ignore

                purchase_id = ulid()

                query = """--sql
                INSERT INTO
                    purchases (purchase_id, user_id, game_id, purchased_at)
                VALUES
                    (?, ?, ?, ?)
                """

                cur.executemany(
                    query,
                    [(purchase_id, user_id, game_id, ts) for game_id in cart_items],
                )

                query = """--sql
                DELETE FROM 
                    cart_items
                WHERE
                    user_id = ?1
                """

                cur.execute(query, (user_id,))
                db.commit()
                return redirect(
                    url_for("store.vault_order_summary", purchase_id=purchase_id)
                )
            except DatabaseError as ex:
                db.rollback()
                print(ex)
                error = {
                    "kind": "server",
                    "code": "vault_order_pain",
                    "message": f"Unable to complete purchase, please try again - {ex}",
                }

                return render_template(
                    "views/vault_payment.html",
                    user_message=user_message,
                    error=error,
                    account_balance=account_balance,
                    cart_total=cart_total,
                ), status
    else:
        # GET
        return render_template(
            "views/vault_payment.html",
            account_balance=account_balance,
            cart_total=cart_total,
        )
