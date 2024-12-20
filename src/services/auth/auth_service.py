import sqlite3
import secrets
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from src.config import email_config


class AuthService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AuthService, cls).__new__(cls)
            cls._instance.db_path = 'my_app.db'
            cls._instance.current_user_id = None
        return cls._instance

    def _get_db_connection(self):
        """Create a database connection."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def register_user(self, username, email, password):
        """Register a new user."""
        try:
            print(f"\nAttempting to register user: {username}")
            connection = self._get_db_connection()
            cursor = connection.cursor()

            # Check if username exists
            cursor.execute(
                "SELECT COUNT(*) FROM users WHERE username = ?", (username,))
            username_count = cursor.fetchone()[0]
            print(f"Username count: {username_count}")

            # Check if email exists
            cursor.execute(
                "SELECT COUNT(*) FROM users WHERE email = ?", (email,))
            email_count = cursor.fetchone()[0]
            print(f"Email count: {email_count}")

            if username_count > 0:
                print("Username already exists")
                return False, "Username already exists"

            if email_count > 0:
                print("Email already exists")
                return False, "Email already exists"

            # Hash the password using PBKDF2
            hashed_password = self.hash_password(password)
            if not hashed_password:
                return False, "Failed to hash password"

            print("Password hashed successfully")

            # Insert the new user
            cursor.execute(
                """
                INSERT INTO users (username, email, password) 
                VALUES (?, ?, ?)
                """,
                (username, email, hashed_password)
            )
            connection.commit()
            print("User inserted successfully")

            cursor.close()
            connection.close()
            return True, "Registration successful"

        except Exception as e:
            print(f"Error in register_user: {e}")
            import traceback
            traceback.print_exc()
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()
            return False, f"Registration failed: {str(e)}"

    def login(self, username, password):
        """Authenticate a user."""
        try:
            print("\n=== LOGIN ATTEMPT ===")
            print(f"Username: {username}")
            conn = self._get_db_connection()
            cursor = conn.cursor()

            # Get user data
            cursor.execute(
                "SELECT user_id, password FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()

            if not result:
                print("User not found")
                return False, "Invalid username or password"

            user_id, stored_password = result
            print(f"Found user with ID: {user_id}")

            # Use PBKDF2 for verification
            if self.verify_password(password, stored_password):
                self.current_user_id = user_id
                print(
                    f"Password verified. Set current_user_id to: {self.current_user_id}")

                # Update last login
                cursor.execute("""
                    UPDATE users 
                    SET last_login = CURRENT_TIMESTAMP 
                    WHERE username = ?
                """, (username,))
                conn.commit()
                print("Login successful")
                return True, "Login successful"

            print("Invalid password")
            return False, "Invalid username or password"

        except Exception as e:
            print(f"Login error: {e}")
            traceback.print_exc()
            return False, f"Login failed: {str(e)}"
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    def email_exists(self, email):
        """Check if email exists in database."""
        try:
            conn = self._get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT 1 FROM users WHERE email = ?", (email,))
            result = cursor.fetchone()
            return bool(result)
        finally:
            cursor.close()
            conn.close()

    def send_reset_email(self, email):
        """Send password reset email."""
        try:
            if not self.email_exists(email):
                return False

            conn = self._get_db_connection()
            cursor = conn.cursor()

            # Generate reset token
            reset_token = secrets.token_urlsafe(32)
            expiry = datetime.now() + timedelta(hours=24)

            # Store token in database
            cursor.execute("""
                UPDATE users 
                SET reset_token = ?,
                    reset_token_expiry = ?
                WHERE email = ?
            """, (reset_token, expiry, email))

            conn.commit()

            # Create reset URL
            reset_url = f"pyflora://reset-password?token={reset_token}"

            # Email setup
            sender_email = email_config.SENDER_EMAIL
            password = email_config.APP_PASSWORD

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = email
            message["Subject"] = "PyFlora Password Reset"

            body = f"""
            Hello,

            You have requested to reset your password for PyFlora.
            Please click the link below to reset your password:

            {reset_url}

            If you did not request this reset, please ignore this email.
            This link will expire in 24 hours.

            Best regards,
            PyFlora Team
            """
            message.attach(MIMEText(body, "plain"))

            # Send email
            with smtplib.SMTP_SSL(email_config.SMTP_SERVER, email_config.SMTP_PORT) as server:
                server.login(sender_email, password)
                server.send_message(message)

            return True

        except Exception as e:
            print(f"Reset email error: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def verify_reset_token(self, token):
        """Verify if reset token is valid and not expired."""
        try:
            conn = self._get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT user_id, reset_token_expiry 
                FROM users 
                WHERE reset_token = ?
            """, (token,))

            result = cursor.fetchone()
            if result:
                user_id, expiry = result
                if expiry and datetime.strptime(expiry, '%Y-%m-%d %H:%M:%S') > datetime.now():
                    return user_id
            return None
        except Exception as e:
            print(f"Token verification error: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    def reset_password(self, token, new_password):
        """Reset password using token."""
        try:
            print(f"\nAttempting to reset password with token: {token}")
            connection = self._get_db_connection()
            cursor = connection.cursor()

            # First verify the token is valid and not expired
            cursor.execute(
                """
                SELECT email 
                FROM password_reset_tokens 
                WHERE token = ? 
                AND is_valid = 1
                AND datetime('now') < datetime(expiry)
                """,
                (token,)
            )
            result = cursor.fetchone()
            print(f"Token lookup result: {result}")

            if not result:
                print("Token not found, invalid, or expired")
                cursor.close()
                connection.close()
                return False

            email = result[0]
            print(f"Found valid token for email: {email}")

            # Hash the new password using PBKDF2 (same as registration/login)
            hashed_password = self.hash_password(new_password)
            if not hashed_password:
                print("Failed to hash new password")
                cursor.close()
                connection.close()
                return False

            # Update the password
            cursor.execute(
                """
                UPDATE users 
                SET password = ? 
                WHERE email = ?
                """,
                (hashed_password, email)
            )
            rows_affected = cursor.rowcount
            print(f"Password update rows affected: {rows_affected}")

            # Invalidate the token
            cursor.execute(
                """
                UPDATE password_reset_tokens 
                SET is_valid = 0 
                WHERE token = ?
                """,
                (token,)
            )
            token_rows = cursor.rowcount
            print(f"Token update rows affected: {token_rows}")

            connection.commit()
            cursor.close()
            connection.close()

            return rows_affected > 0

        except Exception as e:
            print(f"Error in reset_password: {e}")
            traceback.print_exc()
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()
            return False

    def request_password_reset(self, email):
        """Request password reset for user."""
        try:
            print(f"\nRequesting password reset for email: {email}")
            connection = self._get_db_connection()
            cursor = connection.cursor()

            # Verify email exists
            cursor.execute(
                "SELECT user_id FROM users WHERE email = ?", (email,))
            result = cursor.fetchone()
            print(f"User lookup result: {result}")

            if not result:
                print("Email not found")
                return False

            # Generate token
            token = secrets.token_urlsafe(32)
            expiry = datetime.now() + timedelta(hours=24)
            print(f"Generated token: {token}")

            try:
                # Save token to database
                cursor.execute(
                    """
                    INSERT INTO password_reset_tokens 
                    (email, token, expiry, is_valid) 
                    VALUES (?, ?, ?, 1)
                    """,
                    (email, token, expiry.isoformat())
                )
                connection.commit()

                # Create reset URL
                reset_url = f"pyflora://reset-password/?token={token}"

                # Send email using Gmail SMTP
                sender_email = "rkkundid9@gmail.com"  # Your Gmail address
                app_password = "zefj otgl ocfm rpzg"  # Your app password

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = email
                msg['Subject'] = "PyFlora - Password Reset Request"

                body = f"""
                <html>
                <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
                    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                        <div style="background-color: white; padding: 40px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                            <div style="text-align: center; margin-bottom: 30px;">
                                <h1 style="color: #4CAF50; margin: 0; font-size: 28px;">PyFlora</h1>
                                <p style="color: #666; margin: 5px 0 0;">Password Reset Request</p>
                            </div>
                            
                            <p style="color: #333; font-size: 16px; line-height: 1.5;">Hello,</p>
                            
                            <p style="color: #333; font-size: 16px; line-height: 1.5;">We received a request to reset your password for your PyFlora account. To proceed with the password reset, click the link below:</p>
                            
                            <div style="text-align: center; margin: 30px 0;">
                                <a href="{reset_url}" 
                                   style="background-color: #4CAF50; 
                                          color: white; 
                                          padding: 12px 30px; 
                                          text-decoration: none; 
                                          border-radius: 25px;
                                          font-size: 16px;
                                          font-weight: bold;
                                          display: inline-block;
                                          box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                                    Reset Password
                                </a>
                            </div>
                            
                            <p style="color: #666; font-size: 14px; line-height: 1.5;">
                                If the button doesn't work, copy and paste this link into your browser:
                                <br>
                                <span style="color: #4CAF50; word-break: break-all;">{reset_url}</span>
                            </p>
                            
                            <p style="color: #666; font-size: 14px; line-height: 1.5;">
                                If you didn't request this password reset, you can safely ignore this email. 
                                The link will expire in 24 hours for security purposes.
                            </p>
                            
                            <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee;">
                                <p style="color: #888; font-size: 14px; margin: 0;">Best regards,</p>
                                <p style="color: #4CAF50; font-weight: bold; font-size: 16px; margin: 5px 0;">PyFlora Team</p>
                            </div>
                        </div>
                        
                        <div style="text-align: center; margin-top: 20px;">
                            <p style="color: #999; font-size: 12px;">
                                This is an automated message, please do not reply to this email.
                            </p>
                        </div>
                    </div>
                </body>
                </html>
                """
                msg.attach(MIMEText(body, 'html'))

                # Send email
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(sender_email, app_password)
                    server.send_message(msg)
                    print(f"Reset email sent to: {email}")

                cursor.close()
                connection.close()
                return True

            except Exception as e:
                print(f"Error in token generation/email: {e}")
                traceback.print_exc()
                if 'cursor' in locals():
                    cursor.close()
                if 'connection' in locals():
                    connection.close()
                return False

        except Exception as e:
            print(f"Error requesting password reset: {e}")
            traceback.print_exc()
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()
            return False

    def _send_reset_email(self, email, reset_url):
        """Send password reset email."""
        try:
            print(f"\nSending reset email to: {email}")
            print(f"Reset URL: {reset_url}")

            # Debug: Check if token exists in database
            connection = self._get_db_connection()
            cursor = connection.cursor()
            token = reset_url.split('token=')[1]
            cursor.execute(
                "SELECT * FROM password_reset_tokens WHERE token = ?", (token,))
            token_data = cursor.fetchone()
            print(f"Token in database before sending email: {token_data}")
            cursor.close()
            connection.close()

            # Create email message
            msg = MIMEMultipart()
            msg['From'] = "your-email@example.com"  # Replace with your email
            msg['To'] = email
            msg['Subject'] = "Password Reset Request"

            body = f"""
            Click the following link to reset your password:
            {reset_url}
            
            This link will expire in 24 hours.
            """
            msg.attach(MIMEText(body, 'plain'))

            # For testing, just print the email
            print("\nEmail content:")
            print(f"To: {email}")
            print(f"Subject: {msg['Subject']}")
            print(f"Body: {body}")

            return True

        except Exception as e:
            print(f"Error sending reset email: {e}")
            import traceback
            traceback.print_exc()
            return False

    def get_current_user_data(self):
        """Get current user's data from the database."""
        try:
            connection = self._get_db_connection()
            cursor = connection.cursor()
            cursor.execute("""
                SELECT username, email, created_at, last_login
                FROM users
                WHERE user_id = ?
            """, (self.current_user_id,))

            result = cursor.fetchone()
            if result:
                return {
                    "username": result[0],
                    "email": result[1],
                    "created_at": result[2],
                    "last_login": result[3]
                }
            return None
        except Exception as e:
            print(f"Error getting user data: {e}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()

    def change_password(self, current_password, new_password):
        """Change user's password."""
        try:
            print("\n=== CHANGE PASSWORD ATTEMPT ===")
            print(f"Current user_id: {self.current_user_id}")

            if self.current_user_id is None:
                print("Error: No user is currently logged in")
                return False, "No user is currently logged in"

            connection = self._get_db_connection()
            cursor = connection.cursor()

            # First verify current password
            cursor.execute(
                """
                SELECT password 
                FROM users 
                WHERE user_id = ?
                """,
                (self.current_user_id,)
            )
            result = cursor.fetchone()

            if not result:
                print(f"No user found with ID: {self.current_user_id}")
                cursor.close()
                connection.close()
                return False, "User not found"

            stored_hash = result[0]
            print("Found stored password hash")

            # Use PBKDF2 for verification (same as forgot password)
            if not self.verify_password(current_password, stored_hash):
                print("Current password verification failed")
                cursor.close()
                connection.close()
                return False, "Current password is incorrect"

            print("Current password verified, hashing new password...")
            # Hash new password with PBKDF2 (same as forgot password)
            new_hash = self.hash_password(new_password)
            if not new_hash:
                print("Failed to hash new password")
                cursor.close()
                connection.close()
                return False, "Failed to hash new password"

            print("Updating password in database...")
            cursor.execute("""
                UPDATE users 
                SET password = ?
                WHERE user_id = ?
            """, (new_hash, self.current_user_id))

            connection.commit()
            cursor.close()
            connection.close()
            print("Password updated successfully")
            return True, "Password changed successfully"

        except Exception as e:
            print(f"Error changing password: {e}")
            import traceback
            traceback.print_exc()
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()
            return False, "An error occurred while changing password"

    def is_logged_in(self):
        """Check if a user is currently logged in."""
        return self.current_user_id is not None

    def logout(self):
        """Log out the current user."""
        self.current_user_id = None

    def hash_password(self, password):
        """Hash a password for storing."""
        try:
            # Generate a random salt
            salt = os.urandom(32)

            # Derive the key using the password and salt
            key = self._derive_key(password, salt)

            # Combine salt and key, then convert to hex string
            return (salt + key).hex()
        except Exception as e:
            print(f"Error hashing password: {e}")
            return None

    def verify_password(self, password, stored_hash):
        """Verify a password against its stored hash."""
        try:
            # Convert stored hash from hex string back to bytes
            stored_hash_bytes = bytes.fromhex(stored_hash)

            # Hash the provided password with the same salt
            salt = stored_hash_bytes[:32]  # First 32 bytes are salt
            key = self._derive_key(password, salt)

            # Compare the new hash with stored hash (excluding salt)
            return key == stored_hash_bytes[32:]
        except Exception as e:
            print(f"Error verifying password: {e}")
            return False

    def _derive_key(self, password, salt):
        """Derive a key from password and salt using PBKDF2."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        return kdf.derive(password.encode())
