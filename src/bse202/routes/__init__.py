from flask import render_template, Blueprint

root_blueprint = Blueprint("root", __name__, url_prefix="")


@root_blueprint.route("/")
@root_blueprint.route("/<name>")
def index(name="Unknown Name"):
    template = render_template("index.html", name=name)
    return template
