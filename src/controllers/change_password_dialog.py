from PyQt6 import QtWidgets, QtCore
from src.views.ui.change_password_dialog import Ui_ChangePasswordDialog
from src.services.auth.auth_service import AuthService
from src.utils.validators.auth_validator import AuthValidator


class ChangePasswordDialog(QtWidgets.QDialog):
    def __init__(self, auth_service, parent=None):
        super().__init__(parent)
        self.auth_service = auth_service
        self.ui = Ui_ChangePasswordDialog()
        self.ui.setupUi(self)

        # Set window flags for frameless window
        self.setWindowFlags(
            QtCore.Qt.WindowType.Dialog |
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint
        )

        # Connect signals
        self.ui.change_button.clicked.connect(self._change_password)
        self.ui.show_password.stateChanged.connect(
            self._toggle_password_visibility)

        # Store references to commonly used widgets
        self.current_password_input = self.ui.current_password_input
        self.new_password_input = self.ui.new_password_input
        self.confirm_password_input = self.ui.confirm_password_input
        self.status_label = self.ui.status_label

    def _change_password(self):
        """Handle password change."""
        current_password = self.current_password_input.text()
        new_password = self.new_password_input.text()
        confirm_password = self.confirm_password_input.text()

        if new_password != confirm_password:
            self.status_label.setText("New passwords do not match")
            self.status_label.setStyleSheet("color: #FF5252")
            return

        success, message = self.auth_service.change_password(
            current_password, new_password)

        if success:
            self.status_label.setText(message)
            self.status_label.setStyleSheet("color: #4CAF50")
            QtCore.QTimer.singleShot(1500, self.accept)  # Close after 1.5s
        else:
            self.status_label.setText(message)
            self.status_label.setStyleSheet("color: #FF5252")

    def _toggle_password_visibility(self, state):
        """Toggle password visibility for all password fields."""
        echo_mode = (QtWidgets.QLineEdit.EchoMode.Normal
                     if state == QtCore.Qt.CheckState.Checked.value
                     else QtWidgets.QLineEdit.EchoMode.Password)

        self.current_password_input.setEchoMode(echo_mode)
        self.new_password_input.setEchoMode(echo_mode)
        self.confirm_password_input.setEchoMode(echo_mode)

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
