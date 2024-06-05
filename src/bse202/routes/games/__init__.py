"""
Games related functions
----------------------

Specifically relating to game stores, if it is here, it does not mean the
games are in the user library, but they are available for purchase.

the `user` module is where libraries are handled, and an extra module may
be added in future for handling a users library

Prefix: `/games`
"""

from .blueprint import games_blueprint
from .index import games_root
from .storepage import game_store_page
from .snippets import game_storepage_reviews
from .library_section import library_section

__all__ = ["games_blueprint"]
