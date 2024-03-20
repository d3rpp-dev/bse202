from flask import render_template, g, Blueprint

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/login")
def index(name=None):
    template = render_template("auth/login.html")
    return template
