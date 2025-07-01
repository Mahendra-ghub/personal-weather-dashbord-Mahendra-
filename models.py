
import sqlite3

DB_NAME = 'users.db'

def init_db():
    with sqlite3.connect(DB_NAME) as con:
        con.execute('''CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            location TEXT NOT NULL)''')
        con.execute('''CREATE TABLE IF NOT EXISTS agri_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT,
            crop TEXT,
            observation TEXT,
            date TEXT,
            FOREIGN KEY(user_email) REFERENCES users(email)
        )''')

def get_user_by_email(email):
    with sqlite3.connect(DB_NAME) as con:
        con.row_factory = sqlite3.Row
        cur = con.execute('SELECT * FROM users WHERE email=?', (email,))
        row = cur.fetchone()
        return dict(row) if row else None

def insert_user(email, password, location):
    with sqlite3.connect(DB_NAME) as con:
        con.execute('INSERT INTO users (email, password, location) VALUES (?, ?, ?)', (email, password, location))

def update_location(email, location):
    with sqlite3.connect(DB_NAME) as con:
        con.execute('UPDATE users SET location=? WHERE email=?', (location, email))

def insert_agri_log(email, crop, observation, date):
    with sqlite3.connect(DB_NAME) as con:
        con.execute('INSERT INTO agri_logs (user_email, crop, observation, date) VALUES (?, ?, ?, ?)', (email, crop, observation, date))

def get_agri_logs(email):
    with sqlite3.connect(DB_NAME) as con:
        con.row_factory = sqlite3.Row
        cur = con.execute('SELECT * FROM agri_logs WHERE user_email=? ORDER BY date DESC', (email,))
        return [dict(row) for row in cur.fetchall()]
