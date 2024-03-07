from bse202.middlware import register_middleware
from bse202.routes import root_blueprint

from flask import Flask


def app():
    app = Flask(__name__)

    register_middleware(app)
    
    app.register_blueprint(root_blueprint)

    return app
