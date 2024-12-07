import re
from database.user_data_handler import username_exists

def validate_username(username):
    if not username:
        return False, "Username cannot be empty!"

    if username_exists(username):
        return False, "Username already exists!"
    return True, ""

def validate_password(password, confirm_password):
    if not password or not confirm_password:
        return False, "Password fields can't be empty!"

    if password != confirm_password:
        return False, "Passwords do not match!"
    return True, ""

def validate_email(email):
    if not email:
        return False, "Email cannot be empty."

    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not re.match(email_regex, email):
        return False, "Invalid email format!"
    return True, ""
