import sqlite3
from flask import g
from os.path import exists

DB_LOCATION = "./database.db"


def check_db_exists() -> bool:
    return exists(DB_LOCATION)


def get_db():
    db = getattr(g, "_db", None)
    if db is None:
        db = g._db = sqlite3.connect(DB_LOCATION)
    return db
