# user/__init__.py

from .blueprint import user_blueprint
from .index import self
from .by_id import account
from .top_up_credit import top_up_credit
from .update_top_up_option import update_top_up_option
from .voucher import voucher
from .top_up import top_up
from .search import search_games
from .recommendation import get_specific_games

__all__ = ["user_blueprint"]

# Register the search route under user_blueprint
user_blueprint.route("/search", methods=["GET"])(search_games)

# Register the recommendation route under user_blueprint
user_blueprint.route("/recommendation", methods=["GET"])(get_specific_games)
