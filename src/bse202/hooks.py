from flask import Flask, Response, g, request
from itsdangerous import URLSafeSerializer, BadSignature
from os import environ, _exit
from time import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('.env')

secret_key = environ.get("SECRET_KEY")
template_prefix = environ.get("TEMPLATE_PREFIX")

one_month_in_seconds = 60 * 60 * 24 * 30
one_year_in_seconds = one_month_in_seconds * 12

# check
# - var is set
# - var is not empty
if secret_key is None or secret_key.strip() == "":
    print("SECRET_KEY not set")
    _exit(1)

# We've already checked that SECRET_KEY is set
auth_serializer = URLSafeSerializer(secret_key)

def register_hooks(app: Flask):
    # Pre-Request Middleware
    @app.before_request
    def _():
        g.ip = request.remote_addr
        g.ua = request.headers.get("User-Agent")

        # Allows me to use backend pages without affecting the front-end development
        if template_prefix is not None:
            g.template_prefix = template_prefix
        else:
            g.template_prefix = ""

        auth_cookie = request.cookies.get("auth")
        if auth_cookie is not None:
            g.original_token = auth_cookie
            # attempt to parse the token, allow the request to proceed if invalid, but assume not logged in
            try:
                g.token = auth_serializer.loads(auth_cookie, secret_key)

                # refresh the cookie anyway if about to expire
                if g.token["exp"] - time() < one_month_in_seconds:
                    g.token["exp"] = int(time() + one_year_in_seconds)
                    g.refresh = True
            except BadSignature:
                # Signature Verification Failed
                print("Rejecting Token")
            except _:
                pass

    # Post-Request Middleware
    @app.after_request
    def _(response: Response) -> Response:
        # catch non-standard response code and delete token, then change the status to a standard status
        if response.status == "403":
            print("bad auth, reset cookie")
            response.set_cookie(key="auth", value="", httponly=True, expires=0)
            return response

        if "token" in g:
            if "exp" not in g.token:
                g.token["exp"] = int(time() + one_year_in_seconds)

            # Only update cookie if change occurred
            serialised_cookie = auth_serializer.dumps(g.token, secret_key)

            if (
                "original_token" not in g
                or serialised_cookie != g.original_token
                or ("refresh" in g and g.refresh)
            ):
                response.set_cookie(
                    key="auth",
                    value=serialised_cookie,
                    expires=g.token["exp"],
                    httponly=True,
                )
        elif "original_token" in g:
            # clear cookie if original token set but token is not
            #
            # if this pops up it means the cookie is invalid, or was deleted
            response.set_cookie(key="auth", value="", expires=0)

        return response
