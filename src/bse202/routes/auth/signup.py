from flask import redirect, url_for, request, render_template
from werkzeug.datastructures import ImmutableMultiDict
from sqlite3 import Connection
from ulid import ulid
from time import time

from .blueprint import auth_blueprint
from ...db import get_db


def get_valid_form_data(dict: ImmutableMultiDict[str, str]) -> tuple[str, str] | str:
    """
    Returns `str` if there is an error

    Returns `(str, str)` if all is good (username, password)
    """
    username = dict.get("username")
    password = dict.get("password")

    if username is None:
        return "Missing Username"
    elif password is None:
        return "Missing Password"
    else:
        return (username, password)


def is_username_available(db: Connection, username: str) -> dict | None:
    """
    Check the amount of database entries where the username is the same

    Since it is a unique key, this query will always return `1`, or `0`, so
    we check if it is zero.
    """
    is_username_taken_cursor = db.execute(
        "SELECT count(user_id) FROM `users` where `username` = ?", [username]
    )
    if is_username_taken_cursor.fetchone()[0] == 0:
        return None
    else:
        return {"kind": "username", "message": f"Username \"{username}\" is already taken"}


@auth_blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        db = get_db()

        maybe_valid_data = get_valid_form_data(request.form)

        if isinstance(maybe_valid_data, str):
            return render_template(
                "auth/signup.html",
                error={
                    "kind": "missing",
                    "message": maybe_valid_data
                }
            ), 400

        (username, password) = maybe_valid_data

        maybe_error = is_username_available(db, username)
        if maybe_error is not None:
            return render_template("auth/signup.html", error=maybe_error), 400

        user_insert = db.cursor()
        user_insert.execute(
            "INSERT INTO `users` (`user_id`, `created_at`, `username`) VALUES (?1, ?2, ?3)",
            [ulid(), int(time()), username],
        )
        db.commit()

    return render_template("auth/signup.html")
