"""
adds a home page for this blueprint that redirects home,

might get it to redirect to self in the future
"""

from flask import redirect, url_for, g

from .blueprint import user_blueprint


@user_blueprint.get("/")
@user_blueprint.get("/self")
def self():
    if "token" in g:
        user_id = g.token["user_id"]
        if user_id is not None:
            return redirect(url_for("user.account", user_id=user_id)), 302
        else:
            return redirect(url_for("auth.login")), 307
    else:
        return redirect(url_for("auth.login")), 307
