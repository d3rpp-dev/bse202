from flask import render_template
from .blueprint import store_blueprint


@store_blueprint.get("/vault_order_summary")
def vault_order_summary():
    return render_template("views/vault_order_summary.html")
