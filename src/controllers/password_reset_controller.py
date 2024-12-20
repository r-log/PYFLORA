from PyQt6 import QtWidgets
from src.services.auth.auth_service import AuthService
from src.controllers.new_password_dialog import NewPasswordDialog
import sys


class PasswordResetController:
    def __init__(self, parent=None):
        self.parent = parent
        self.auth_service = AuthService()

    def show_reset_dialog(self, token):
        """Show the password reset dialog."""
        try:
            print("\nPasswordResetController: Starting reset URL handling")
            print(f"Parent window: {self.parent}")
            print(f"Token: {token}")

            dialog = NewPasswordDialog(self.parent)
            dialog.reset_button.clicked.connect(
                lambda: self._handle_reset(dialog, token))

            print("Created dialog")
            print("Dialog setup complete, showing dialog...")
            dialog.exec()

        except Exception as e:
            print(f"Error showing reset dialog: {e}")
            import traceback
            traceback.print_exc()

    def _handle_reset(self, dialog, token):
        """Handle password reset."""
        try:
            print("\nPasswordResetController: Starting reset")
            print(f"Token: {token}")
            sys.stdout.flush()

            password = dialog.password_input.text()
            confirm_password = dialog.confirm_password_input.text()
            sys.stdout.flush()

            if password == confirm_password:
                print("Passwords match, attempting reset...")
                if self.auth_service.reset_password(token, password):
                    print("Password reset successful!")
                    dialog.status_label.setText("Password reset successful!")
                    dialog.status_label.setStyleSheet("color: green")
                    dialog.accept()
                else:
                    print("Failed to reset password")
                    dialog.status_label.setText("Failed to reset password")
                    dialog.status_label.setStyleSheet("color: red")
            else:
                print("Passwords do not match")
                dialog.status_label.setText("Passwords do not match")
                dialog.status_label.setStyleSheet("color: red")
            sys.stdout.flush()

        except Exception as e:
            print(f"Error in _handle_reset: {str(e)}")
            import traceback
            traceback.print_exc()
            sys.stdout.flush()
