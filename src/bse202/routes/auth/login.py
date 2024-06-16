"""
Handler for logging in

Takes GET and POST requests for the same URL to handle auth functions

Redirects to the homepage afterwards with the new token
"""

from sqlite3 import Cursor, DatabaseError
from flask import redirect, url_for, g, render_template, request, abort
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError, Argon2Error
from werkzeug.datastructures import ImmutableMultiDict
from .blueprint import auth_blueprint
from ...db import get_db

hasher = PasswordHasher()


def validate_password(fetched_hash: str, password: str) -> bool:
    """
    using the given hash
    """
    try:
        return hasher.verify(fetched_hash, password)
    except VerificationError:
        return False


def get_user_and_validate_hash(
    cursor: Cursor, username: str, password: str
) -> tuple[str, str | None] | None:
    """
    Get user's ID from the database based on username

    If this returns none, the user does not exists and a 404 should be returned
    """
    try:
        query = """--sql
            SELECT 
                users.user_id,
                users.account_type,
                password_hashes.password_hash 
            FROM 
                users 
            LEFT JOIN 
                password_hashes 
            ON 
                password_hashes.user_id = users.user_id 
            WHERE 
                username = ?1 
            LIMIT 1
        """

        db_result: tuple[str, str | None, str] | None = cursor.execute(
            query,
            [username],
        ).fetchone()

        if db_result is None:
            return None
        else:
            (user_id, account_type, password_hash) = db_result
            if validate_password(password_hash, password):
                return user_id, account_type
            else:
                return None

    except DatabaseError as ex:
        print(ex)
        return None


def get_valid_form_data(dict: ImmutableMultiDict[str, str]) -> tuple[str, str] | str:
    """
    Returns `str` if there is an error

    Returns `(str, str)` if all is good (username, password)
    """
    username = dict.get("user")
    password = dict.get("pass")

    if username is None:
        return "Missing Username"
    elif password is None:
        return "Missing Password"
    else:
        return (username, password)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if g.token is not None:
        return redirect(url_for("root.index"))

    if request.method == "POST":
        maybe_form_data = get_valid_form_data(request.form)

        if isinstance(maybe_form_data, str):
            return render_template(
                f"{g.template_prefix}views/login.html",
                error={
                    "kind": "user",
                    "code": "login_invalid_form_data",
                    "message": maybe_form_data,
                },
            ), 400
        else:
            (username, password) = maybe_form_data
            db_cursor = get_db().cursor()

            try:
                loaded_user = get_user_and_validate_hash(db_cursor, username, password)
                if loaded_user is None:
                    return render_template(
                        f"{g.template_prefix}views/login.html",
                        error={
                            "kind": "user",
                            "code": "login_invalid_input",
                            "message": "Invalid Username or Password",
                        },
                    ), 400
                else:
                    (user_id, account_type) = loaded_user

                    if "token" not in g:
                        g.token = {}

                    g.token["user_id"] = user_id
                    g.token["account_type"] = (
                        account_type if account_type is not None else "user"
                    )
                    g.token["username"] = username
                    g.refresh = True
                    return redirect(url_for("root.index"))

            except Argon2Error as ex:
                # all other cases have been handled
                db_cursor.close()
                return render_template(
                    f"{g.template_prefix}views/login.html",
                    error={
                        "kind": "server",
                        "code": "login_internal_error",
                        "message": f"Internal Server Error - {ex}",
                    },
                ), 500

    return render_template(f"{g.template_prefix}views/login.html"), 200
