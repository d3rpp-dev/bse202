from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

games = ["Valorant", "Fall Guys", "DOTA2"]


@app.route("/")
def index():
    return render_template("searchbar.html")


@app.route("/search")
def search():
    query = request.args.get("query", "")
    if query:
        results = [game for game in games if query.lower() in game.lower()]
    else:
        results = []
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
