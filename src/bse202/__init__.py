from .db import check_db_exists, get_db

from .hooks import register_hooks

from .routes import root_blueprint
from .routes.auth import auth_blueprint
from .routes.games import games_blueprint

from flask import Flask, g
from os import environ

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


# we can check ahead of time if the database exists and alert the server admin
# in the case it does not.
if environ.get("INIT_DB") is None and not check_db_exists():
    # this is essentially making the program more resistant to
    # someone forgetting to run `rye run init_db`
    raise RuntimeError("\n\nPlease run\n\n    rye run init_db\n\nAnd try again\n")

register_hooks(app)

app.register_blueprint(root_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(games_blueprint)
