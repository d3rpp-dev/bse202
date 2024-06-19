from flask import render_template

from .blueprint import user_blueprint


@user_blueprint.route("/voucher", methods=["GET", "POST"])
def voucher():
    return render_template("views/voucher.html")
