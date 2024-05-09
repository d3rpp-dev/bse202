import sqlite3
from flask import g

DB_LOCATION = "./database.db"


def get_db():
    db = getattr(g, "_db", None)
    if db is None:
        db = g._db = sqlite3.connect(DB_LOCATION)
    return db
