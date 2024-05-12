from flask import Blueprint, redirect, url_for

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.get("/")
def auth_root_redirect():
    """
    Automatically redirect `/auth` to `/auth/login`

    This is a convenience endpoint for users and for us.
    """
    return redirect(url_for("auth.login"))
