from flask import render_template, redirect, url_for

from .blueprint import store_blueprint


@store_blueprint.get("/cart")
def cart():
    return render_template("views/cart.html")


@store_blueprint.post("/add_to_cart")
def add_to_cart():
    return redirect(url_for("store.cart"))


@store_blueprint.post("/remove_from_cart")
def remove_from_cart():
    return redirect(url_for("store.cart"))
