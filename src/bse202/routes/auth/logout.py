"""
Handler for logging out

direct the user to the URL of this function and it will
sign them out and return them to the homepage.
"""

from flask import g, redirect, url_for
from .blueprint import auth_blueprint


@auth_blueprint.get("/logout")
def logout():
    # the post-request handler will delete the cookie if g.token becomes None
    del g.token
    return redirect(url_for("root.index"))
