from flask import render_template, g
from .blueprint import auth_blueprint


@auth_blueprint.get("/login")
def login():
    if "token" not in g:
        g.token = {}
    g.token["auth"] = True
    g.refresh = True

    template = render_template("auth/login.html")
    return template
