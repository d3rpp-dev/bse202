from typing import Any
from werkzeug.routing import BaseConverter
from re import fullmatch


class ULIDConverter(BaseConverter):
    regex = "^[0-7][0-9A-HJKMNP-TV-Z]{25}$"
