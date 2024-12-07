import sqlite3

DATABASE_PATH = 'my_app.db'

def get_connection():
    return sqlite3.connect(DATABASE_PATH)
