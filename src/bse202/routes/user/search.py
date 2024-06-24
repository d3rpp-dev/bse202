# user/search.py

from flask import Blueprint, request, jsonify
from ...db import get_db
import logging

search_bp = Blueprint("search", __name__, url_prefix="/search")

@search_bp.route("/", methods=["GET"])
def search_games():
    query = request.args.get("q", "")
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    search_pattern = f"%{query}%"
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "SELECT game_id, title, description, price FROM games WHERE title LIKE ?",
            (search_pattern,),
        )
        results = cursor.fetchall()

        games = []
        for row in results:
            game_id, title, description, price = row
            games.append(
                {
                    "game_id": game_id,
                    "title": title,
                    "description": description,
                    "price": price,
                }
            )

        return jsonify(games)

    except Exception as ex:
        logging.error(f"Error searching games: {str(ex)}")
        return jsonify({"error": "Internal server error"}), 500
