from .hooks import register_hooks

from .routes import root_blueprint
from .routes.auth import auth_blueprint

from flask import Flask


def app():
    app = Flask(__name__)

    register_hooks(app)

    app.register_blueprint(root_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
