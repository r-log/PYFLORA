from PyQt6 import QtWidgets, QtCore
from src.views.ui.password_reset_dialog import Ui_PasswordResetDialog
from src.services.auth.auth_service import AuthService


class PasswordResetDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.auth_service = AuthService()

        # Set up the UI
        self.ui = Ui_PasswordResetDialog()
        self.ui.setupUi(self)

        # Set window flags for frameless window
        self.setWindowFlags(
            QtCore.Qt.WindowType.Dialog |
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint
        )

        # Connect signals
        self.ui.send_button.clicked.connect(self._request_reset)

        # Store references to commonly used widgets
        self.email_input = self.ui.email_input
        self.status_label = self.ui.status_label
        self.send_button = self.ui.send_button

    def _request_reset(self):
        """Request password reset."""
        email = self.email_input.text()
        print(f"\nRequesting password reset for email: {email}")

        try:
            if self.auth_service.request_password_reset(email):
                print("Password reset request successful")
                self.status_label.setText("Password reset email sent!")
                self.status_label.setStyleSheet("color: #4CAF50")  # Green
                # Close after 2 seconds
                QtCore.QTimer.singleShot(2000, self.accept)
            else:
                print("Password reset request failed")
                self.status_label.setText("Failed to send reset email")
                self.status_label.setStyleSheet("color: #FF5252")  # Red
        except Exception as e:
            print(f"Error in password reset request: {e}")
            import traceback
            traceback.print_exc()
            self.status_label.setText("An error occurred")
            self.status_label.setStyleSheet("color: #FF5252")

    def mousePressEvent(self, event):
        """Handle mouse press events for window dragging."""
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        """Handle mouse move events for window dragging."""
        if hasattr(self, 'oldPos'):
            delta = event.globalPosition().toPoint() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        """Handle mouse release events for window dragging."""
        if hasattr(self, 'oldPos'):
            delattr(self, 'oldPos')
