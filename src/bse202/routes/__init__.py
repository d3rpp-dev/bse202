from flask import render_template, g, Blueprint

root_blueprint = Blueprint("root", __name__, url_prefix="")


@root_blueprint.route("/")
@root_blueprint.route("/<name>")
def index(name=None):
    template = render_template("index.html", name=name)
    return template
