from flask import render_template, request, redirect, url_for

from .blueprint import user_blueprint


@user_blueprint.route("/top_up", methods=["GET", "POST"])
def top_up():
    amount_str = request.form.get("amount")

    if amount_str is not None:
        return render_template("views/top_up_credit.html", amount=float(amount_str))
    else:
        return redirect(url_for("user.self"))
