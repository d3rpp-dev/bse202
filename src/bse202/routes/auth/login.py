from flask import redirect, url_for, g, render_template, request, abort
from .blueprint import auth_blueprint


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        if "token" not in g:
            g.token = {}

        form_data = request.form.to_dict()
        if not ("user" in form_data and "pass" in form_data):
            abort(400)
        else:
            g.token["user"] = form_data["user"]
            g.token["pass"] = form_data["pass"]
            g.token["auth"] = True
            g.refresh = True
            return redirect(url_for("root.index"))

    return render_template("auth/login.html", error=error)
