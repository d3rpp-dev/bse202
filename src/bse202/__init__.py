from bse202.middlware import register_middleware

from bse202.routes import root_blueprint
from bse202.routes.auth import auth_blueprint

from flask import Flask


def app():
    app = Flask(__name__)

    register_middleware(app)

    app.register_blueprint(root_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
