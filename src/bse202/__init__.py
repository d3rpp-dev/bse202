from .db import check_db_exists, get_db, delete_db
from .hooks import register_hooks
from .routes import root_blueprint
from .routes.auth import auth_blueprint
from .routes.store import store_blueprint
from .routes.user import user_blueprint

from flask import Flask, g
from os import environ
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('.env')

app = Flask(__name__)

# Set secret key from environment variable
app.config['SECRET_KEY'] = environ.get('SECRET_KEY', 'default_secret_key')

def init_db():
    with app.app_context():
        # start fresh
        delete_db()

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
