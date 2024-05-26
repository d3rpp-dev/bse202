"""
User Home Page
"""

from flask import render_template, redirect, url_for, g

from .blueprint import user_blueprint

@user_blueprint.get("/<user_id>")
def user_home(user_id: str):
    if user_id.lower() != user_id:
        return redirect(url_for("user.user_home", user_id = user_id.lower()))


    return render_template(f"{g.template_prefix}user/index.html", user_id=user_id)
