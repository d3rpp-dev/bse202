from flask import render_template, jsonify

from .blueprint import user_blueprint


@user_blueprint.post("/update_top_up_option")
def update_top_up_option():
    return jsonify({"success": True}), 200
