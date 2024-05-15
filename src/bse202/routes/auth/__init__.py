"""
Auth related functions
----------------------

Prefix: `/auth`
"""

from .blueprint import auth_blueprint

from .login import login
from .logout import logout
from .signup import signup

__all__ = ["auth_blueprint"]
