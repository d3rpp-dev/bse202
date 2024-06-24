from flask import render_template

from .blueprint import store_blueprint


@store_blueprint.route("/vault_payment", methods=["GET", "POST"])
def payment():
    return render_template("views/payment.html")
