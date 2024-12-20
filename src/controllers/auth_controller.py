from PyQt6 import QtWidgets, QtCore
from src.views.ui.log_reg_ui import Ui_LogRegWindow
from src.services.auth.auth_service import AuthService
from src.views.ui.base_ui import BaseUI
from src.controllers.main_window_controller import MainWindowController
from src.views.utils.message_displayer import MessageDisplayer
from src.utils.validators.auth_validator import AuthValidator
from PyQt6.QtCore import pyqtSignal
from src.views.ui.log_reg_window import LoginRegistrationWindow
import json
import os
from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
from .password_reset_dialog import PasswordResetDialog


class LoginRegistrationController(LoginRegistrationWindow):
    """Controller for the login/registration window."""

    logout_signal = pyqtSignal()  # Signal to handle logout

    def __init__(self, debug_queue=None):
        super().__init__(debug_queue)
        self.ui = Ui_LogRegWindow()
        self.base_ui = BaseUI()
        self.auth_service = AuthService()
        self.message_displayer = MessageDisplayer(self.ui)
        self.validator = AuthValidator()
        self.main_window = None

        # Setup encryption with enhanced security
        self.key_file = Path.home() / '.pyflora' / '.key'
        self.salt_file = Path.home() / '.pyflora' / '.salt'
        self.creds_file = Path.home() / '.pyflora' / '.creds'
        self._setup_encryption()

        # Setup UI
        self.ui.setupUi(self)
        self.base_ui.setup_window_behavior(self)
        self.initialize_ui()

        # Load saved credentials
        self.load_saved_credentials()

        # Connect forgot password label
        self.ui.forgot_password_label.mousePressEvent = self._show_password_reset
        self.ui.forgot_password_label.setCursor(
            QtCore.Qt.CursorShape.PointingHandCursor)

    def _generate_key(self, salt):
        """Generate a secure key using PBKDF2."""
        try:
            # Use machine-specific info as base password
            base_password = f"{os.getlogin()}{os.name}".encode()

            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=480000,  # High iteration count for security
            )

            key = base64.urlsafe_b64encode(kdf.derive(base_password))
            return key
        except Exception as e:
            if hasattr(self, 'debug'):
                self.debug(f"Error generating key: {str(e)}")
            return None

    def _setup_encryption(self):
        """Setup encryption with enhanced security measures."""
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.key_file), exist_ok=True)

            # Generate or load salt
            if not self.salt_file.exists():
                salt = os.urandom(16)  # Generate random salt
                with open(self.salt_file, 'wb') as f:
                    f.write(salt)
            else:
                with open(self.salt_file, 'rb') as f:
                    salt = f.read()

            # Generate key using PBKDF2
            key = self._generate_key(salt)
            if key:
                self.cipher_suite = Fernet(key)
                if hasattr(self, 'debug'):
                    self.debug("Encryption setup complete")
            else:
                raise Exception("Failed to generate encryption key")

        except Exception as e:
            if hasattr(self, 'debug'):
                self.debug(f"Error in encryption setup: {str(e)}")
            self.cipher_suite = None

    def _save_credentials(self):
        """Save credentials with enhanced encryption if remember me is checked."""
        try:
            if not self.cipher_suite:
                if hasattr(self, 'debug'):
                    self.debug(
                        "Encryption not available, cannot save credentials")
                return

            if self.ui.remember_me_checkbox.isChecked():
                creds = {
                    'username': self.ui.sign_in_username_input.text(),
                    'password': self.ui.sign_in_password_input.text(),
                    'timestamp': str(QtCore.QDateTime.currentDateTime().toString())
                }

                # Add additional entropy
                creds['entropy'] = base64.b64encode(os.urandom(16)).decode()

                encrypted_data = self.cipher_suite.encrypt(
                    json.dumps(creds).encode())

                with open(self.creds_file, 'wb') as f:
                    f.write(encrypted_data)

                if hasattr(self, 'debug'):
                    self.debug("Credentials saved securely")
            else:
                # Securely remove saved credentials
                if self.creds_file.exists():
                    # Overwrite with random data before deleting
                    with open(self.creds_file, 'wb') as f:
                        f.write(os.urandom(1024))
                    os.remove(self.creds_file)
                    if hasattr(self, 'debug'):
                        self.debug("Credentials removed securely")

        except Exception as e:
            if hasattr(self, 'debug'):
                self.debug(f"Error saving credentials: {str(e)}")

    def load_saved_credentials(self):
        """Load and decrypt saved credentials if they exist."""
        try:
            if not self.cipher_suite:
                if hasattr(self, 'debug'):
                    self.debug(
                        "Encryption not available, cannot load credentials")
                return

            if self.creds_file.exists():
                with open(self.creds_file, 'rb') as f:
                    encrypted_data = f.read()
                    decrypted_data = self.cipher_suite.decrypt(encrypted_data)
                    creds = json.loads(decrypted_data)

                    # Set credentials in UI
                    self.ui.sign_in_username_input.setText(creds['username'])
                    self.ui.sign_in_password_input.setText(creds['password'])
                    self.ui.remember_me_checkbox.setChecked(True)

                    if hasattr(self, 'debug'):
                        self.debug("Credentials loaded securely")

        except Exception as e:
            if hasattr(self, 'debug'):
                self.debug(f"Error loading credentials: {str(e)}")
            # If there's any error, securely remove potentially corrupted credentials
            self._secure_cleanup()

    def _secure_cleanup(self):
        """Securely clean up stored credentials."""
        try:
            if self.creds_file.exists():
                # Overwrite with random data before deleting
                with open(self.creds_file, 'wb') as f:
                    f.write(os.urandom(1024))
                os.remove(self.creds_file)
        except Exception as e:
            if hasattr(self, 'debug'):
                self.debug(f"Error in secure cleanup: {str(e)}")

    def initialize_ui(self):
        """Initialize the UI components."""
        self.set_window_frameless()
        self.set_initial_focus()
        self.setup_tab_order()
        self._connect_signals()

    def set_window_frameless(self):
        """Set window flags for frameless window."""
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

    def set_initial_focus(self):
        """Set initial focus to username input."""
        self.ui.sign_in_username_input.setFocus()

    def setup_tab_order(self):
        """Set up tab order for input fields."""
        self.setTabOrder(self.ui.sign_in_username_input,
                         self.ui.sign_in_password_input)
        self.setTabOrder(self.ui.sign_in_password_input,
                         self.ui.sign_in_button)
        self.setTabOrder(self.ui.sign_up_username_input,
                         self.ui.sign_up_password_input)
        self.setTabOrder(self.ui.sign_up_password_input,
                         self.ui.sign_up_confirm_password_input)
        self.setTabOrder(self.ui.sign_up_confirm_password_input,
                         self.ui.sign_up_email_input)
        self.setTabOrder(self.ui.sign_up_email_input,
                         self.ui.sign_up_button)

    def _connect_signals(self):
        """Connect UI signals to their handlers."""
        # Sign in
        self.ui.sign_in_button.clicked.connect(self._handle_login)
        self.ui.sign_in_password_visible.toggled.connect(
            self._toggle_password_visibility)

        # Sign up
        self.ui.sign_up_button.clicked.connect(self._handle_register)
        self.ui.sign_up_password_visibile.toggled.connect(
            self._toggle_signup_password_visibility)

        # Navigation
        self.ui.sign_in_link.clicked.connect(self._show_sign_in)
        self.ui.sign_up_link.clicked.connect(self._show_sign_up)

        # Exit
        self.ui.exit_button.clicked.connect(self.close)

        # Connect forgot password label
        self.ui.forgot_password_label.mousePressEvent = self._show_password_reset
        self.ui.forgot_password_label.setCursor(
            QtCore.Qt.CursorShape.PointingHandCursor)

    def _handle_login(self):
        """Handle login button click."""
        username = self.ui.sign_in_username_input.text()
        password = self.ui.sign_in_password_input.text()

        success, message = self.auth_service.login(username, password)

        if success:
            # Save credentials if remember me is checked
            self._save_credentials()
            self.message_displayer.show_success(message, is_signup=False)
            self._handle_login_success()
        else:
            self.message_displayer.show_error(message, is_signup=False)

    def _handle_register(self):
        """Handle registration button click."""
        try:
            print("\nDEBUG: Starting registration for user:",
                  self.ui.sign_up_username_input.text())

            # Get input values
            username = self.ui.sign_up_username_input.text().strip()
            email = self.ui.sign_up_email_input.text().strip()
            password = self.ui.sign_up_password_input.text()
            confirm_password = self.ui.sign_up_confirm_password_input.text()

            # Validate inputs
            if not all([username, email, password, confirm_password]):
                self.message_displayer.show_error(
                    "All fields are required", is_signup=True)
                return

            # Validate email format
            email_valid, email_msg = self.validator.validate_email(email)
            if not email_valid:
                self.message_displayer.show_error(email_msg, is_signup=True)
                return

            # Check password match
            if password != confirm_password:
                self.message_displayer.show_error(
                    "Passwords do not match", is_signup=True)
                return

            # Validate password
            password_valid, password_msg = self.validator.validate_password(
                password)
            if not password_valid:
                self.message_displayer.show_error(password_msg, is_signup=True)
                return

            # Attempt registration
            success, message = self.auth_service.register_user(
                username, email, password)

            if success:
                self.message_displayer.show_success(
                    "Registration successful!", is_signup=True)
                # Clear inputs
                self.ui.sign_up_username_input.clear()
                self.ui.sign_up_email_input.clear()
                self.ui.sign_up_password_input.clear()
                self.ui.sign_up_confirm_password_input.clear()
                # Switch to sign in
                self._show_sign_in()
            else:
                self.message_displayer.show_error(message, is_signup=True)

        except Exception as e:
            print("DEBUG: Unexpected error in registration handler:", str(e))
            self.message_displayer.show_error(
                "Registration failed", is_signup=True)

    def _toggle_password_visibility(self, visible):
        """Toggle password field visibility."""
        mode = QtWidgets.QLineEdit.EchoMode.Normal if visible else QtWidgets.QLineEdit.EchoMode.Password
        self.ui.sign_in_password_input.setEchoMode(mode)

    def _toggle_signup_password_visibility(self, visible):
        """Toggle sign up password fields visibility."""
        mode = QtWidgets.QLineEdit.EchoMode.Normal if visible else QtWidgets.QLineEdit.EchoMode.Password
        self.ui.sign_up_password_input.setEchoMode(mode)
        self.ui.sign_up_confirm_password_input.setEchoMode(mode)

    def _show_sign_in(self):
        """Switch to sign in view."""
        self.ui.sign_up_widget.hide()
        self.ui.sign_in_widget.show()
        # Clear inputs
        self.ui.sign_in_username_input.clear()
        self.ui.sign_in_password_input.clear()
        self.message_displayer.clear_message(is_signup=False)

    def _show_sign_up(self):
        """Switch to sign up view."""
        self.ui.sign_in_widget.hide()
        self.ui.sign_up_widget.show()
        # Clear inputs
        self.ui.sign_up_username_input.clear()
        self.ui.sign_up_password_input.clear()
        self.ui.sign_up_confirm_password_input.clear()
        self.ui.sign_up_email_input.clear()
        self.message_displayer.clear_message(is_signup=True)

    def keyPressEvent(self, event):
        """Handle key press events."""
        if event.key() == QtCore.Qt.Key.Key_Return:
            if self.ui.sign_in_widget.isVisible():
                if (self.ui.sign_in_username_input.hasFocus() or
                        self.ui.sign_in_password_input.hasFocus()):
                    self.ui.sign_in_button.click()
            else:
                if (self.ui.sign_up_username_input.hasFocus() or
                    self.ui.sign_up_password_input.hasFocus() or
                    self.ui.sign_up_confirm_password_input.hasFocus() or
                        self.ui.sign_up_email_input.hasFocus()):
                    self.ui.sign_up_button.click()
        else:
            super().keyPressEvent(event)

    def _show_password_reset(self, event=None):
        """Show the password reset dialog."""
        try:
            print("\nDEBUG: Opening password reset dialog")
            dialog = PasswordResetDialog(self)
            dialog.exec()
        except Exception as e:
            print(f"DEBUG: Error showing password reset dialog: {e}")
            import traceback
            traceback.print_exc()

    def _handle_password_reset(self, dialog):
        """Handle password reset request."""
        try:
            email = dialog.email_input.text().strip()
            print(f"\nProcessing password reset for email: {email}")

            # Validate email
            email_valid, email_msg = self.validator.validate_email(email)
            if not email_valid:
                dialog.status_label.setText(email_msg)
                dialog.status_label.setStyleSheet(
                    "color: #FF5252;")  # Red for error
                return

            # Request password reset
            if self.auth_service.request_password_reset(email):
                dialog.status_label.setText(
                    "Password reset link sent to your email!")
                dialog.status_label.setStyleSheet(
                    "color: #4CAF50;")  # Green for success
                # Close after 2 seconds
                QtCore.QTimer.singleShot(2000, dialog.accept)
            else:
                dialog.status_label.setText(
                    "Failed to send reset email. Please try again.")
                dialog.status_label.setStyleSheet("color: #FF5252;")

        except Exception as e:
            print(f"Error in password reset: {str(e)}")
            import traceback
            traceback.print_exc()
            dialog.status_label.setText("An error occurred. Please try again.")
            dialog.status_label.setStyleSheet("color: #FF5252;")

    def handle_forgot_password(self):
        """Handle forgot password button click"""
        try:
            print("\nShowing password reset dialog...")
            dialog = PasswordResetDialog(self)
            dialog.exec()
        except Exception as e:
            print(f"Error showing password reset dialog: {e}")
            import traceback
            traceback.print_exc()

    def _handle_login_success(self):
        """Handle successful login."""
        self.main_window = MainWindowController(
            self.auth_service)  # Pass auth_service
        self.main_window.show()
        self.close()
