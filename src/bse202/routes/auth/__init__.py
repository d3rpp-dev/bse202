from flask import render_template, g, Blueprint

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/login")
@auth_blueprint.route("/<name>")
def index(name="Unknown Name"):
    template = render_template("auth/login.html", name=name)
    g.token["auth"] = True
    return template
