"""
Games related functions
----------------------

Specifically relating to game stores, if it is here, it does not mean the
games are in the user library, but they are available for purchase.

the `user` module is where libraries are handled, and an extra module may
be added in future for handling a users library

Prefix: `/games`
"""

from .blueprint import store_blueprint
from .index import store_root
from .checkout import checkout

from .vault_payment import vault_payment
from .vault_order_summary import render_template

from .payment import payment
from .order_summary import order_summary

from .cart import cart

__all__ = ["store_blueprint"]
