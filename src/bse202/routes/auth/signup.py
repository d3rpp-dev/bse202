from flask import redirect, url_for, request
from .blueprint import auth_blueprint


@auth_blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        print("GET request received for create account")
    else:
        print("POST request received for create account")

    return redirect(url_for("static", filename="styles/auth.css"), code=307)
