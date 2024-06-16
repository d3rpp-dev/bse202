from flask import render_template

from .blueprint import root_blueprint


@root_blueprint.get("/contact")
def contact_page():
    return render_template("views/contact.html")
