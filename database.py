import sqlite3

def init_db():
    conn = sqlite3.connect('husky_game.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            referrer_id INTEGER,
            balance INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()
