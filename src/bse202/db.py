import sqlite3
from flask import g
from os.path import exists
from os import environ, remove

_db = environ.get("DATABASE_FILE")

DB_LOCATION: str = _db if _db is not None else "./database.db"


def check_db_exists() -> bool:
    return exists(DB_LOCATION)

def delete_db():
    if check_db_exists():
        remove(DB_LOCATION)

def get_db():
    db = getattr(g, "_db", None)
    if db is None:
        db = g._db = sqlite3.connect(DB_LOCATION)
    return db
