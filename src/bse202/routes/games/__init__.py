"""
Games related functions
----------------------

Prefix: `/games`
"""

from .blueprint import games_blueprint
from .index import games_root
from .storepage import game_store_page
from .storepage_reviews import game_storepage_reviews

__all__ = ["games_blueprint"]
