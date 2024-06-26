from .db import check_db_exists, get_db, delete_db
from .hooks import register_hooks

from .routes import root_blueprint
from .routes.auth import auth_blueprint
from .routes.store import store_blueprint
from .routes.user import user_blueprint

from flask import Flask, g
from os import environ

app = Flask(__name__)


def init_db():
    with app.app_context():
        db = get_db()

        # Execute schema.sql
        with app.open_resource("schema.sql", mode="rb") as f:
            schema_content = f.read().decode("utf-8")
            db.cursor().executescript(schema_content)

        # Commit changes after executing schema.sql
        db.commit()

        # Execute sample_data.sql
        with app.open_resource("sample_data.sql", mode="rb") as f:
            sample_data_content = f.read().decode("utf-8")
            db.cursor().executescript(sample_data_content)

        # Commit changes after executing sample_data.sql
        db.commit()


@app.teardown_appcontext
def close_db(_exception):
    db = getattr(g, "_db", None)
    if db is not None:
        db.close()


# we can check ahead of time if the database exists and alert the server admin
# in the case it does not.
#
# this code also runs when we init the DB so the `init_db` command adds and
# environment variable so it doesn't trigger if we're trying to initialise
# the DB.
if environ.get("INIT_DB") is None and not check_db_exists():
    # this is essentially making the program more resistant to
    # someone forgetting to run `rye run init_db`
    raise RuntimeError("\n\nPlease run\n\n    rye run init_db\n\nAnd try again\n")
else:
    register_hooks(app)

    app.register_blueprint(root_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(store_blueprint)
    app.register_blueprint(user_blueprint)
