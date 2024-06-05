from flask import render_template, redirect, url_for, g
from sqlite3 import DatabaseError

from .blueprint import user_blueprint
from ...db import get_db


@user_blueprint.get("/<user_id>/library")
@user_blueprint.get("/library")
def user_library(user_id: str | None = None):
    user = None
    user_is_self = False

    if user_id is None:
        # url is /library so we attempt to get the user from the token
        if "token" in g:
            user_id = g.token["user_id"]
            user_is_self = True
        else:
            return redirect(url_for("auth.login"))
    else:
        if "token" in g:
            user_is_self = g.token["user_id"] == user_id

    if user_id is None:
        # last ditch effort to refresh the token, better than just a 500
        return redirect(url_for("auth.login"))

    # at this point, user is definitely some
    #
    # user = user_id of looking up user
    # user_is_self = if the library we're looking up is the currently signed in user's

    db = get_db()

    try:
        query = """--sql
		SELECT
			username,
			account_type,
			profile_bg,
			text_colour
		FROM
			users
		WHERE
			user_id = $1
		"""

        # sqlite3 is weird and this function can return None
        #
        # it's just not a part of the type
        #
        # reason #3132 that python is dumb, and there are
        # thousands of solutions that do the job better.
        user_db_result: tuple[str, str, str, str] = db.execute(
            query, (user_id,)
        ).fetchone()

        if user_db_result is None:
            return render_template(
                f"{g.template_prefix}user/library.html",
                error={
                    "kind": "user",
                    "code": "library_user_not_found",
                    "message": "user does not exist",
                },
            )

        user = {
            "user_id": user_id,
            "username": user_db_result[0],
            "account_type": user_db_result[1],
            "profile_bg": user_db_result[2],
            "text_colour": user_db_result[3],
        }

        # user_db_result is actually the tuple, case of none is handled

        query = """--sql
		SELECT
			purchases.game_id,
			purchases.purchased_at,
            game_assets.asset_id
		FROM
			purchases
        INNER JOIN
            game_assets
        ON
            game_assets.game_id = purchases.game_id AND game_assets.asset_type = 'grid_banner'
        WHERE
			user_id = $1
		"""
        user_purchases_result: list[tuple[str, int, int]] = db.execute(
            query, (user_id,)
        ).fetchall()
        # python                 = weird
        # functional programming = elite
        # i love haskell and parts of rust mwahahahahaha
        user_purchases_map = map(
            lambda a: {"game_id": a[0], "purchased_at": a[1], "banner_asset": a[2]},
            user_purchases_result,
        )

        # we know things worked as long as this try block catches everything
    except DatabaseError as ex:
        print(ex)
        return render_template(
            f"{g.template_prefix}user/library.html",
            error={
                "kind": "server",
                "code": "library_user_fetch",
                "message": "a database error occured",
            },
        )

    return render_template(
        f"{g.template_prefix}user/library.html",
        user=user,
        library=user_purchases_map,
        user_is_self=user_is_self,
    )
