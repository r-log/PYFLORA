import os
import json
import bcrypt

# Path to the token file
TOKEN_FILE = 'user_token.json'


def create_token(username, password):
    # Create a secure token. This is a simplistic example. In a real app, you'd want a more secure token.
    token = bcrypt.hashpw(f'{username}{password}'.encode(), bcrypt.gensalt())
    return token


def save_token(username, token):
    with open(TOKEN_FILE, 'w') as file:
        json.dump({'username': username, 'token': token.decode()}, file)


def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as file:
            return json.load(file)
    return None


def validate_token(username, token):
    saved_token = load_token()
    return saved_token and saved_token['username'] == username and saved_token['token'] == token


def clear_token():
    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)
