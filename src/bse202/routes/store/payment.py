from flask import render_template, redirect, url_for, g, request, flash
from datetime import datetime
from sqlite3 import DatabaseError
import re
from ulid import ulid

from .blueprint import store_blueprint
from ...db import get_db

# Regular expressions for card number, expiry date, and CVV
card_number_regex = re.compile(r"^\d{16}$")
expiry_date_regex = re.compile(r"^(0[1-9]|1[0-2])\/(20[2-9][0-9])$")
cvv_regex = re.compile(r"^\d{3,4}$")

@store_blueprint.route("/payment", methods=["GET", "POST"])
def payment():
     # Protected
    if "token" not in g:
        redirect(url_for("auth.login"))

    user_id = g.token["user_id"]

    user_message = None
    error = None
    status = 200

    db = get_db()

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

    if request.method == "POST":
        if len(cart_items) <= 0:
            user_message = "Cart is empty"

            return render_template(
                "views/payment.html",
                user_message=user_message,
                error=error,
                cart_total=cart_total,
            ), status
        
        card_number = request.form.get("card_number", "").strip()
        expiry_date = request.form.get("expiry_date", "").strip()
        cvv = request.form.get("cvv", "").strip()

        # Ensure the inputs are strings (they should be if coming from form)
        if not isinstance(card_number, str):
            flash("Invalid card number format.", "error")
            return render_template("views/payment.html")
        if not isinstance(expiry_date, str):
            flash("Invalid expiry date format.", "error")
            return render_template("views/payment.html")
        if not isinstance(cvv, str):
            flash("Invalid CVV format.", "error")
            return render_template("views/payment.html")

        # Validate card number, expiry date, and CVV
        if not card_number_regex.match(card_number):
            return render_template("views/payment.html")
        if not expiry_date_regex.match(expiry_date):
            flash(
                "Invalid expiry date. Please enter a valid date in MM/YYYY format.",
                "error",
            )
            return render_template("views/payment.html")
        if not cvv_regex.match(cvv):
            flash("Invalid CVV. Please enter a valid 3 or 4 digit CVV.", "error")
            return render_template("views/payment.html")

        # At this point we can just add the items to the users library

        cur = db.cursor()
        purchase_id = ulid()

        try:
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

            return redirect(url_for("store.order_summary", purchase_id = purchase_id))
        except DatabaseError as ex:
            db.rollback()
            print(ex)
            error={
                "kind": "server",
                "code": "card_order_pain",
                "message": f"Unable to complete purchase, please try again - {ex}"
            }

            return render_template(
                "views/payment.html",
                error=error
            )

    return render_template("views/payment.html")
