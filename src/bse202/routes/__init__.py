"""
Index Routes
----------------------

Prefix: `/`
"""

from .blueprint import root_blueprint
from .index import index
from .about import about_page
from .contact import contact_page

__all__ = ["root_blueprint"]
