"""
Index Routes
----------------------

Prefix: `/`
"""

from .blueprint import root_blueprint
from .index import index

__all__ = ["root_blueprint"]
