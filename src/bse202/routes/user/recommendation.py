from flask import Blueprint, jsonify
from ...db import get_db

from .blueprint import user_blueprint


@user_blueprint.route("/recommendation", methods=["GET"])
def get_specific_games():
    try:
        db = get_db()
        cursor = db.cursor()

        # Specify the game_ids for the 4 fixed games
        game_ids = (1, 14, 16, 12)

        # Select the specific games based on the provided game_ids
        cursor.execute(
            "SELECT game_id, title, description, price FROM games WHERE game_id IN (?, ?, ?, ?)",
            game_ids,
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
        # Handle exceptions appropriately
        print(f"Error fetching specific games: {str(ex)}")
        return jsonify({"error": "Internal server error"}), 500
