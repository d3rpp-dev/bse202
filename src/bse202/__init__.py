from .db import get_db

from .hooks import register_hooks

from .routes import root_blueprint
from .routes.auth import auth_blueprint
from .routes.games import games_blueprint

from flask import Flask, g

app = Flask(__name__)


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("schema.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()
        with app.open_resource("sample_data.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.teardown_appcontext
def close_db(_exception):
    db = getattr(g, "_db", None)
    if db is not None:
        db.close()


register_hooks(app)

app.register_blueprint(root_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(games_blueprint)
