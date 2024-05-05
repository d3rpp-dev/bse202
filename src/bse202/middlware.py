from flask import Flask, Response, g, request


def register_middleware(app: Flask):
    # Pre-Request Middlware
    @app.before_request
    def _():
        g.ua = request.headers.get("User_Agent")

    # Post-Request Middleware
    @app.after_request
    def _(response: Response) -> Response:
        response.headers.set("X-Test-Header", g.get("ua"))
        return response
