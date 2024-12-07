import bcrypt
from .connection import get_connection

def username_exists(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM users WHERE username=?)", (username,))
    exists = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return exists

def create_user(username, hashed_password, email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO users (username, password, email) VALUES (?, ?, ?)
    ''', (username, hashed_password, email))

    conn.commit()
    conn.close()

def check_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    stored_password = cursor.fetchone()

    if stored_password and bcrypt.checkpw(password.encode('utf-8'), stored_password[0]):
        return True
    return False
