from PyQt6 import QtWidgets, QtCore
from src.views.ui.new_password_dialog import Ui_NewPasswordDialog


class NewPasswordDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the UI
        self.ui = Ui_NewPasswordDialog()
        self.ui.setupUi(self)

        # Set window flags for frameless window
        self.setWindowFlags(
            QtCore.Qt.WindowType.Dialog |
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint
        )

        # Connect show password checkbox
        self.ui.show_password.toggled.connect(self._toggle_password_visibility)

        # Store references to commonly used widgets
        self.password_input = self.ui.password_input
        self.confirm_password_input = self.ui.confirm_password_input
        self.status_label = self.ui.status_label
        self.reset_button = self.ui.reset_button

    def _toggle_password_visibility(self, checked):
        """Toggle password visibility for both password fields."""
        mode = (QtWidgets.QLineEdit.EchoMode.Normal
                if checked
                else QtWidgets.QLineEdit.EchoMode.Password)
        self.ui.password_input.setEchoMode(mode)
        self.ui.confirm_password_input.setEchoMode(mode)

    def mousePressEvent(self, event):
        """Handle mouse press events for window dragging."""
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        """Handle mouse move events for window dragging."""
        if self.oldPos is not None:
            delta = event.globalPosition().toPoint() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        """Handle mouse release events for window dragging."""
        self.oldPos = None
