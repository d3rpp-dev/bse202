from flask import render_template

from .blueprint import store_blueprint


@store_blueprint.route("/checkout", methods=["GET", "POST"])
def checkout():
    return render_template("views/checkout.html")
