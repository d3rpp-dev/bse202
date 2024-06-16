"""
User Home Page
"""

from sqlite3 import DatabaseError
from flask import render_template, redirect, url_for, g

from .blueprint import user_blueprint
from ...db import get_db


@user_blueprint.get("/<user_id>")
def account(user_id: str):
    return render_template("views/account.html")

    # If the username is in all caps (like it can be in some cases)
    # redirect the user to this endpoint but lowercase
    if user_id.lower() != user_id:
        return redirect(url_for("user.account", user_id=user_id.lower())), 302

    db = get_db()

    try:
        query = """--sql
        SELECT
            user_id,
            created_at,
            username,
            account_type,
            profile_bg,
            text_colour,
            description
        FROM
            users
        WHERE
            user_id = $1
        LIMIT
            1
        """

        query_result = db.execute(query, (user_id,)).fetchone()

        if query_result is None:
            return render_template(
                f"{g.template_prefix}user/index.html",
                error={
                    "kind": "user",
                    "code": "user_id_not_exist",
                    "message": "Unknown User ID",
                },
            ), 404

        (
            user_id,
            created_at,
            username,
            account_type,
            profile_bg,
            text_colour,
            description,
        ) = query_result
        user = {
            "user_id": user_id,
            "created_at": created_at,
            "username": username,
            "account_type": account_type,
            "description": description,
        }

        bg_string = f"--user-bg: {profile_bg};" if profile_bg is not None else ""
        colour_string = f"--user-text: {text_colour}" if text_colour is not None else ""

        user_style_string = " ".join([bg_string, colour_string])

        return render_template(
            f"{g.template_prefix}user/index.html",
            user=user,
            user_style_string=user_style_string,
        ), 200
    except DatabaseError as ex:
        print(ex)
        return render_template(
            f"{g.template_prefix}user/index.html",
            error={
                "kind": "server",
                "code": "user_get_by_id",
                "message": "Unknown Error returned by Query",
            },
        ), 500
