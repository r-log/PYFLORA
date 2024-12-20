import re
from typing import Tuple
from ...utils.database.user_data_handler import UserDataHandler


class AuthValidator:
    """Validator for authentication-related input."""

    def __init__(self):
        self.user_data_handler = UserDataHandler()

    def validate_username(self, username: str) -> Tuple[bool, str]:
        """
        Validate username input.

        Args:
            username (str): The username to validate

        Returns:
            Tuple[bool, str]: (is_valid, error_message)
        """
        if not username:
            return False, "Username cannot be empty!"

        # Add additional username validation rules
        if len(username) < 3:
            return False, "Username must be at least 3 characters long!"

        if len(username) > 30:
            return False, "Username must be less than 30 characters!"

        if not username.isalnum():
            return False, "Username can only contain letters and numbers!"

        if self.user_data_handler.username_exists(username):
            return False, "Username already exists!"

        return True, ""

    @staticmethod
    def validate_password(password: str, confirm_password: str = None) -> Tuple[bool, str]:
        """
        Validate password input.

        Args:
            password (str): The password to validate
            confirm_password (str, optional): The confirmation password

        Returns:
            Tuple[bool, str]: (is_valid, error_message)
        """
        if not password:
            return False, "Password cannot be empty!"

        # Check passwords match first
        if confirm_password is not None:
            if password != confirm_password:
                return False, "Passwords do not match!"

        # Add password strength validation
        if len(password) < 8:
            return False, "Password must be at least 8 characters long!"

        if not any(c.isupper() for c in password):
            return False, "Password must contain at least one uppercase letter!"

        if not any(c.islower() for c in password):
            return False, "Password must contain at least one lowercase letter!"

        if not any(c.isdigit() for c in password):
            return False, "Password must contain at least one number!"

        return True, ""

    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        """
        Validate email input.

        Args:
            email (str): The email to validate

        Returns:
            Tuple[bool, str]: (is_valid, error_message)
        """
        if not email:
            return False, "Email cannot be empty!"

        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(email_regex, email):
            return False, "Invalid email format!"

        return True, ""
