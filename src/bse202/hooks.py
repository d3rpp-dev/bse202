from .lib import generate_default_cookie

from flask import Flask, Response, g, request
from itsdangerous import URLSafeSerializer
from os import environ, abort

secret_key = environ.get("SECRET_KEY")

if secret_key is None:
    print("SECRET_KEY not set")
    abort()

# We've already checked that SECRET_KEY is set
auth_serializer = URLSafeSerializer(secret_key)  # type: ignore


def register_hooks(app: Flask):
    # Pre-Request Middlware
    @app.before_request
    def _():
        g.ip = request.remote_addr
        g.ua = request.headers.get("User_Agent")

        auth_cookie = request.cookies.get("auth")
        if auth_cookie is not None:
            g.token = auth_serializer.loads(auth_cookie)
        else:
            g.token = generate_default_cookie(ip=g.ip, authenticated=False)

    # Post-Request Middleware
    @app.after_request
    def _(response: Response) -> Response:
        if "token" in g:
            response.set_cookie(
                key="auth", value=auth_serializer.dumps(g.token), expires=1746524701
            )

        response.headers.set("X-Test-Header", g.get("ua"))
        return response
