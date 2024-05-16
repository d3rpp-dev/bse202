"""
Handler for signing up

Takes GET and POST requests for the same URL to handle auth functions

Redirects to the homepage afterwards with the new token
"""

from flask import redirect, url_for, request, render_template, g
from werkzeug.datastructures import ImmutableMultiDict
from sqlite3 import Connection, Cursor, DatabaseError
from ulid import ulid
from time import time
from argon2 import PasswordHasher

from .blueprint import auth_blueprint
from ...db import get_db

hasher = PasswordHasher()


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


def is_username_available(db: Connection, username: str) -> dict | None:
    """
    Check the amount of database entries where the username is the same

    Since it is a unique key, this query will always return `1`, or `0`, so
    we check if it is zero.
    """

    query = """--sql
        SELECT 
            count(user_id) 
        FROM 
            `users` 
        WHERE 
            `username` = ?
    """

    is_username_taken_cursor = db.execute(query, [username])
    if is_username_taken_cursor.fetchone()[0] == 0:
        return None
    else:
        return {
            "kind": "user",
            "code": "signup_username_taken",
            "message": f'Username "{username}" is already taken',
        }


def save_user(cursor: Cursor, user_id: str, username: str):
    """
    Save the user with an ID of `user_id`
    """
    query = """--sql
        INSERT INTO 
            `users` (
                `user_id`, 
                `created_at`, 
                `username`
            ) 
        VALUES 
            (
                ?1, 
                ?2, 
                ?3
            )
    """

    cursor.execute(
        query,
        [user_id, int(time()), username],
    )


def save_password(cursor: Cursor, user_id: str, password: str):
    """
    Hash the password using Argon2

    This will also automatically generate a ULID salt
    """
    salt = ulid()

    hashed_password = hasher.hash(password=password, salt=str.encode(salt))

    query = """--sql
        INSERT INTO 
            `password_hashes` (
                `user_id`, 
                `password_hash`
            ) 
        VALUES 
            (
                ?1, 
                ?2
            )
    """

    insertion_result_cursor = cursor.execute(
        query,
        [user_id, hashed_password],
    )

    print(insertion_result_cursor.fetchall())


@auth_blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Request is a POST request from the form.
        db = get_db()

        maybe_valid_data = get_valid_form_data(request.form)

        if isinstance(maybe_valid_data, str):
            return render_template(
                f"{g.template_prefix}auth/signup.html",
                error={
                    "kind": "missing",
                    "code": "signup_invalid_form_data",
                    "message": maybe_valid_data,
                },
            ), 400

        (username, password) = maybe_valid_data

        maybe_error = is_username_available(db, username)
        if maybe_error is not None:
            return render_template(
                f"{g.template_prefix}auth/signup.html", error=maybe_error
            ), 400

        user_id = ulid()

        # try/catch here incase the DB operation fails,
        # will cause a database rollback
        try:
            db_cursor = db.cursor()
            save_user(db_cursor, user_id, username)
            save_password(db_cursor, user_id, password)
            db.commit()
        except DatabaseError:
            db.rollback()
            db_cursor.close()
            return "Database Error", 500

        db_cursor.close()

        if "token" not in g:
            g.token = {}

        g.token["user_id"] = user_id
        g.token["username"] = username
        g.token["account_type"] = "user"
        g.refresh = True

        return redirect(url_for("root.index"))
    else:
        # Request is a GET request
        return render_template(f"{g.template_prefix}auth/signup.html")
