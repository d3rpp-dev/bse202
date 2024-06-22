from flask import jsonify, request, g, session, render_template, flash, redirect, url_for
from .blueprint import user_blueprint
from ...db import get_db
import re
import logging

# Regular expressions for card number, expiry date, and CVV
card_number_regex = re.compile(r'^\d{16}$')
expiry_date_regex = re.compile(r'^(0[1-9]|1[0-2])\/(20[2-9][0-9])$')
cvv_regex = re.compile(r'^\d{3,4}$')

@user_blueprint.route("/top_up_credit", methods=["GET", "POST"])
def top_up_credit():
    if request.method == "POST":
        # Handle form submission and validate payment details
        card_number = request.form.get("card_number", "").strip()
        expiry_date = request.form.get("expiry_date", "").strip()
        cvv = request.form.get("cvv", "").strip()
        amount = request.form.get("amount")  # Retrieve amount from form data

        if not amount or not isinstance(amount, str):
            flash("Invalid amount. Please select a valid amount.", "error")
            return render_template("views/top_up_credit.html", amount=0)

        # Convert amount to float
        try:
            amount = float(amount)
        except ValueError:
            flash("Invalid amount. Please select a valid amount.", "error")
            return render_template("views/top_up_credit.html", amount=0)

        # Ensure the inputs are strings (they should be if coming from form)
        if not isinstance(card_number, str):
            flash("Invalid card number format.", "error")
            return render_template("views/top_up_credit.html", amount=amount)
        if not isinstance(expiry_date, str):
            flash("Invalid expiry date format.", "error")
            return render_template("views/top_up_credit.html", amount=amount)
        if not isinstance(cvv, str):
            flash("Invalid CVV format.", "error")
            return render_template("views/top_up_credit.html", amount=amount)

        # Validate card number, expiry date, and CVV (assuming your existing validation logic)

        # If all validations pass, top up the user's account
        try:
            db = get_db()
            user_id = g.token.get("user_id")  # Retrieve user_id from g.token

            if not user_id:
                flash("User ID not found in session.", "error")
                return render_template("views/top_up_credit.html", amount=amount)

            db.execute(
                "UPDATE users SET account_balance = account_balance + ? WHERE user_id = ?",
                (amount, user_id),
            )
            db.commit()

            flash(f"Successfully topped up ${amount:.2f} via Credit Card.", "success")
            # Redirect to the account page
            return redirect(url_for("views.account"))

        except Exception as ex:
            logging.error(f"Failed to top up credit: {str(ex)}")
            flash(f"Failed to top up credit: {str(ex)}", "error")
            return render_template("views/top_up_credit.html", amount=amount)

    # If it's a GET request, just render the top up credit page with a default amount
    amount = session.get('top_up_amount', 0)
    return render_template("views/top_up_credit.html", amount=float(amount))
