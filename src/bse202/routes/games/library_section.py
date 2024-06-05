from flask import redirect, url_for

from .blueprint import games_blueprint


@games_blueprint.get("/library_section/<int:game_id>")
def library_section(game_id: int):
    return redirect(url_for("root.index"))
