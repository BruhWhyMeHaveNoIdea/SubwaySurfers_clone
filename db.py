import sqlite3


def get_connection():
    conn = sqlite3.connect('actual.db')
    return conn


def start_session():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS information (
            nickname TEXT,
            music BOOLEAN,
            sounds BOOLEAN,
            skin TEXT,
            wallpaper TEXT,
            record INTEGER,
        )""")


def update_information(data):
    ...