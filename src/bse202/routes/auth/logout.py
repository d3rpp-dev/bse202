from flask import g, redirect, url_for
from .blueprint import auth_blueprint

@auth_blueprint.get("/logout")
def logout():
	del g.token
	return redirect(url_for("root.index"))