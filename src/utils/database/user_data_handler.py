import bcrypt
import logging
from typing import Optional, Tuple
from sqlite3 import Connection, Cursor, Error
from .connection import DatabaseConnection
from datetime import datetime


class UserDataHandler:
    """Handles all user-related database operations."""

    def __init__(self):
        """Initialize UserDataHandler with database connection and logger."""
        self.db = DatabaseConnection()
        self.logger = logging.getLogger(__name__)

    def username_exists(self, username: str) -> bool:
        """
        Check if a username already exists in the database.

        Args:
            username (str): Username to check

        Returns:
            bool: True if username exists, False otherwise
        """
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT EXISTS(SELECT 1 FROM users WHERE username=?)",
                    (username,)
                )
                return bool(cursor.fetchone()[0])
        except Error as e:
            self.logger.error(f"Database error checking username: {e}")
            raise

    def create_user(self, username: str, password: str, email: str) -> bool:
        """
        Create a new user in the database.

        Args:
            username (str): Username for new user
            password (str): Plain password to be hashed
            email (str): User's email address

        Returns:
            bool: True if user created successfully, False otherwise

        Raises:
            ValueError: If username already exists
        """
        if self.username_exists(username):
            raise ValueError("Username already exists")

        try:
            # Hash password
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (username, password, email) 
                    VALUES (?, ?, ?)
                ''', (username, hashed_password, email))
                conn.commit()
                self.logger.info(f"Created new user: {username}")
                return True
        except Error as e:
            self.logger.error(f"Database error creating user: {e}")
            return False

    def check_user(self, username: str, password: str) -> bool:
        """Check if username and password match."""
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT password 
                    FROM users 
                    WHERE username = ? AND is_active = 1
                    """,
                    (username,)
                )
                result = cursor.fetchone()

                if result:
                    stored_password = result[0]
                    return bcrypt.checkpw(
                        password.encode('utf-8'),
                        stored_password if isinstance(
                            stored_password, bytes) else stored_password.encode('utf-8')
                    )
                return False

        except Error as e:
            self.logger.error(f"Database error checking user: {e}")
            return False

    def get_user_details(self, username: str) -> Optional[dict]:
        """
        Get user details (except password).

        Args:
            username (str): Username to fetch details for

        Returns:
            Optional[dict]: User details or None if user not found
        """
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT username, email FROM users WHERE username = ?',
                    (username,)
                )
                user_data = cursor.fetchone()

                if user_data:
                    return {
                        'username': user_data[0],
                        'email': user_data[1]
                    }
                return None

        except Error as e:
            self.logger.error(f"Database error fetching user details: {e}")
            return None

    def email_exists(self, email: str) -> bool:
        """
        Check if an email already exists in the database.

        Args:
            email (str): Email to check

        Returns:
            bool: True if email exists, False otherwise
        """
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT EXISTS(SELECT 1 FROM users WHERE email=? AND is_active=1)",
                    (email,)
                )
                return bool(cursor.fetchone()[0])
        except Error as e:
            self.logger.error(f"Database error checking email: {e}")
            return False

    def update_password(self, email: str, new_password: bytes) -> bool:
        """
        Update user's password in the database.

        Args:
            email (str): User's email address
            new_password (bytes): New hashed password as bytes

        Returns:
            bool: True if password updated successfully, False otherwise
        """
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    UPDATE users 
                    SET password = ?,
                        last_login = ?
                    WHERE email = ? 
                    AND is_active = 1
                    """,
                    (new_password, datetime.now(), email)
                )
                conn.commit()

                if cursor.rowcount > 0:
                    self.logger.info(f"Password updated for email: {email}")
                    return True
                else:
                    self.logger.warning(
                        f"No active user found with email: {email}")
                    return False

        except Error as e:
            self.logger.error(f"Database error updating password: {e}")
            return False

    def get_user_by_email(self, email: str) -> Optional[dict]:
        """
        Get user details by email (except password).

        Args:
            email (str): Email to fetch details for

        Returns:
            Optional[dict]: User details or None if user not found
        """
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    '''
                    SELECT user_id, username, email, created_at, last_login, is_active 
                    FROM users 
                    WHERE email = ? AND is_active = 1
                    ''',
                    (email,)
                )
                user_data = cursor.fetchone()

                if user_data:
                    return {
                        'user_id': user_data[0],
                        'username': user_data[1],
                        'email': user_data[2],
                        'created_at': user_data[3],
                        'last_login': user_data[4],
                        'is_active': user_data[5]
                    }
                return None

        except Error as e:
            self.logger.error(f"Database error fetching user by email: {e}")
            return None

    def create_password_reset_token(self, email: str, token: str, expiry: datetime) -> bool:
        """
        Store password reset token in the database.

        Args:
            email (str): User's email
            token (str): Reset token
            expiry (datetime): Token expiry timestamp

        Returns:
            bool: True if token stored successfully
        """
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                # First, invalidate any existing tokens for this user
                cursor.execute(
                    """
                    UPDATE password_reset_tokens 
                    SET is_valid = 0 
                    WHERE email = ?
                    """,
                    (email,)
                )

                # Insert new token
                cursor.execute(
                    """
                    INSERT INTO password_reset_tokens 
                    (email, token, expiry, is_valid) 
                    VALUES (?, ?, ?, 1)
                    """,
                    (email, token, expiry)
                )
                conn.commit()
                return True

        except Error as e:
            self.logger.error(f"Database error creating reset token: {e}")
            return False

    def verify_reset_token(self, token: str) -> Optional[str]:
        """
        Verify if a reset token is valid and return associated email.

        Args:
            token (str): Reset token to verify

        Returns:
            Optional[str]: Associated email if token valid, None otherwise
        """
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT email 
                    FROM password_reset_tokens 
                    WHERE token = ? 
                    AND is_valid = 1 
                    AND expiry > ?
                    """,
                    (token, datetime.now())
                )
                result = cursor.fetchone()
                return result[0] if result else None

        except Error as e:
            self.logger.error(f"Database error verifying reset token: {e}")
            return None
