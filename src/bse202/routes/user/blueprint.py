from flask import Blueprint, render_template

user_blueprint = Blueprint("user", __name__, url_prefix="/user")
