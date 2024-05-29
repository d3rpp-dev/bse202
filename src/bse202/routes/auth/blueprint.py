from flask import Blueprint, redirect, url_for, g

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.get("/")
def auth_root_redirect():
    """
    Automatically redirect `/auth` to `/auth/login` if not signed in
    Automitically redirect `/auth` to `/` if signed in

    This is a convenience endpoint for users and for us.
    """

    if "token" in g:
        return redirect(url_for("root.index")), 307
    else:
        return redirect(url_for("auth.login")), 307
