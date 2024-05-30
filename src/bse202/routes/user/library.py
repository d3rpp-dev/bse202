from flask import render_template, redirect, url_for, g
from sqlite3 import DatabaseError

from .blueprint import user_blueprint
from ...db import get_db

@user_blueprint.get("/<user_id>/library")
@user_blueprint.get("/library")
def user_library(user_id: str | None):
	user = None
	user_is_self = False

	if user_id is None:
		# url is /library so we attempt to get the user from the token
		if "token" in g:
			user = g.token['user_id']
			user_is_self = True
		else:
			return redirect(url_for("auth.login"))
	else:
		# url is /<user_id>/library
		user = user_id
		if "token" in g:
			user_is_self = g.token['user_id'] == user_id
	
	if user is None:
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
		user_db_result: tuple[str, str, str, str] = db.execute(query, (user_id,)).fetchone()

		if user_db_result is None:
			return render_template(
				f"{g.template_prefix}user/library.html",
				error = {
					"kind": "user",
					"code": "library_user_not_found",
					"message": "user does not exist"
				}
			)
		
		user_db_result: tuple[str, str, str, str] = user_db_result


		query = """--sql
		"""
		user_purchases_result = db.execute(query, (user_id,))

		# we know things worked as long as this try block catches everything
	except DatabaseError as ex:
		print(ex)
		return render_template(
			f"{g.template_prefix}user/library.html",
			error = {
				"kind": "server",
				"code": "library_user_fetch",
				"message": "a database error occured"
			}
		)

	return render_template(f"{g.template_prefix}user/library.html")