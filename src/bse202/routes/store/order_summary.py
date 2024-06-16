from flask import render_template

from .blueprint import store_blueprint


@store_blueprint.get("/order_summary")
def order_summary():
    return render_template("views/order_summary.html")
