from flask import render_template

from .blueprint import user_blueprint


@user_blueprint.route("/top_up", method=["GET", "POST"])
def top_up():
    return render_template("views/top_up_credit.html")
