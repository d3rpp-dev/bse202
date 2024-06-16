from flask import Blueprint, render_template

store_blueprint = Blueprint("store", __name__, url_prefix="/store")
