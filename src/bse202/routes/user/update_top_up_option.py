from flask import jsonify, request, session
from .blueprint import user_blueprint


@user_blueprint.route("/update_top_up_option", methods=["POST"])
def update_top_up_option():
    request_data = request.get_json()
    amount = request_data.get("amount")
    session["top_up_amount"] = amount  # Store the amount in session
    return jsonify(success=True), 200
