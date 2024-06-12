from .db import check_db_exists, get_db

from .hooks import register_hooks


from .user_id_matcher import ULIDConverter

from flask import Flask, g
from flask_wtf.csrf import CSRFProtect

from os import environ


app = Flask(__name__)
app.config.update(
    SECRET_KEY=environ.get("SECRET_KEY"),
)
csrf = CSRFProtect(app)

app.url_map.converters["ulid"] = ULIDConverter


def init_db():
    with app.app_context():
        database = get_db()
        with app.open_resource("schema.sql", mode="r") as f:
            database.cursor().executescript(f.read())
        database.commit()
        with app.open_resource("sample_data.sql", mode="r") as f:
            database.cursor().executescript(f.read())
        database.commit()


@app.teardown_appcontext
def close_db(_exception):
    database = getattr(g, "_db", None)
    if database is not None:
        database.close()


# we can check ahead of time if the database exists and alert the server admin
# in the case it does not.
#
# this code also runs when we init the DB so the `init_db` command adds and
# environment variable so it doesn't trigger is we're trying to initialise
# the DB.
if environ.get("INIT_DB") is None and not check_db_exists():
    # this is essentially making the program more resistant to
    # someone forgetting to run `rye run init_db`
    raise RuntimeError("\n\nPlease run\n\n    rye run init_db\n\nAnd try again\n")
else:
    register_hooks(app)

    from .routes import root_blueprint
    app.register_blueprint(root_blueprint)

    from .routes.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .routes.games import games_blueprint
    app.register_blueprint(games_blueprint)

    from .routes.user import user_blueprint
    app.register_blueprint(user_blueprint)
