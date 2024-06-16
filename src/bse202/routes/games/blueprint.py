from flask import Blueprint, render_template

games_blueprint = Blueprint("games", __name__, url_prefix="/games")
