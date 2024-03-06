from bse202.app import app
from flask import Request, Response, g, request


@app.before_request
def before_req() -> Request:
    g.ua = request.headers.get("User_Agent")


@app.after_request
def after_req(response: Response) -> Response:
    response.headers.set("X-Test-Header", "bruh moment")
    return response
