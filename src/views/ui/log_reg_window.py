from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import QTimer, QPoint, Qt
import sys


class LoginRegistrationWindow(QtWidgets.QMainWindow):
    def __init__(self, debug_queue=None):
        super().__init__()

        self.debug_queue = debug_queue

        from .log_reg_ui import Ui_LogRegWindow
        from .base_ui import BaseUI

        self.ui = Ui_LogRegWindow()
        self.ui.setupUi(self)
        self.base_ui = BaseUI()

        self.debug("Window initialization started")

        # Store original positions
        self.signin_original_pos = self.ui.sign_in_widget.pos()
        self.signup_original_pos = self.ui.sign_up_widget.pos()

        # Set up debug timer to process events
        self.debug_timer = QTimer(self)
        self.debug_timer.timeout.connect(self.debug_check)
        self.debug_timer.start(100)  # Check every 100ms

        # Install event filter on buttons and parent widgets
        self.ui.sign_in_password_visible.installEventFilter(self)
        self.ui.sign_up_password_visibile.installEventFilter(self)
        self.ui.sign_up_show_password.installEventFilter(self)
        self.ui.sign_in_widget.installEventFilter(self)
        self.ui.sign_up_widget.installEventFilter(self)

        self.debug("Event filters installed")

        # Set initial state
        self.set_initial_state()

        # Set up icons for password visibility
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/eye.svg"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/eye-off.svg"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)

        # Set up buttons with more explicit configuration
        self.setup_password_buttons(icon)
        self.connect_buttons()

    def debug(self, message):
        """Send debug message to queue"""
        if self.debug_queue:
            self.debug_queue.put(message)

    def debug_check(self):
        """Periodic debug check of button states"""
        for button in [self.ui.sign_in_password_visible,
                       self.ui.sign_up_password_visibile,
                       self.ui.sign_up_show_password]:
            if button.isDown():
                self.debug(f"Button {button.objectName()} is being clicked")

    def eventFilter(self, obj, event):
        """Filter events for monitored objects."""
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            self.debug(f"Mouse press on {obj.objectName()}")
        elif event.type() == QtCore.QEvent.Type.MouseButtonRelease:
            self.debug(f"Mouse release on {obj.objectName()}")
        return super().eventFilter(obj, event)

    def set_initial_state(self):
        """Set initial state with sign-in visible and sign-up off-screen."""
        self.ui.sign_in_widget.show()
        self.ui.sign_in_widget.move(self.signin_original_pos)

        # Move sign-up widget off-screen
        self.ui.sign_up_widget.hide()
        self.ui.sign_up_widget.move(QPoint(-1000, -1000))
        self.debug("Initial state set - Sign-up moved off-screen")

    def toggle_password_visibility(self, input_field, button_name, checked):
        """Toggle password visibility."""
        self.debug(f"Toggle clicked for {button_name}, checked={checked}")

        # Get the button that was clicked
        button = None
        if button_name == "sign-up":
            button = self.ui.sign_up_password_visibile
        elif button_name == "confirm":
            button = self.ui.sign_up_show_password

        if button:
            # Force the checked state
            button.setChecked(checked)

        # Toggle the password field
        if checked:
            input_field.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.debug(f"{button_name} password now visible")
        else:
            input_field.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.debug(f"{button_name} password now hidden")

    def setup_password_buttons(self, icon):
        """Set up password visibility buttons."""
        self.debug("Setting up password buttons")

        # Define buttons with their corresponding input fields for easier reference
        button_configs = [
            (self.ui.sign_in_password_visible, "Sign in password"),
            (self.ui.sign_up_password_visibile, "Sign up password"),
            (self.ui.sign_up_show_password, "Confirm password")
        ]

        for button, name in button_configs:
            # Set up button properties
            button.setIcon(icon)
            button.setCheckable(True)
            button.setEnabled(True)
            button.setMinimumSize(24, 24)  # Increased size for visibility
            button.setIconSize(QtCore.QSize(20, 20))  # Set icon size
            button.raise_()
            button.show()

            # Make sure the button is visible
            button.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                    padding: 2px;
                }
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 30);
                }
                QPushButton:checked {
                    background-color: rgba(255, 255, 255, 20);
                }
            """)

            # Force button to be visible
            button.setVisible(True)
            button.raise_()

            self.debug(
                f"Button {button.objectName()} for {name} setup complete")

    def connect_buttons(self):
        """Connect all buttons to their functions."""
        self.debug("Connecting buttons")

        # Password visibility buttons - only for sign up password
        self.ui.sign_up_password_visibile.clicked.connect(
            lambda checked: self.toggle_password_visibility(
                self.ui.sign_up_password_input,
                "sign-up",
                checked
            )
        )

        self.debug("Password visibility buttons connected")

    def switch_to_signup(self):
        """Switch to signup form."""
        self.debug("Switching to signup")
        self.ui.sign_in_widget.hide()
        self.ui.sign_up_widget.show()
        self.ui.sign_up_widget.move(self.signup_original_pos)
        self.ui.sign_up_password_visibile.raise_()
        self.ui.sign_up_show_password.raise_()

    def switch_to_signin(self):
        """Switch to signin form."""
        self.debug("Switching to signin")
        self.ui.sign_up_widget.hide()
        self.ui.sign_in_widget.show()
        self.ui.sign_in_widget.move(self.signin_original_pos)
        self.ui.sign_in_password_visible.raise_()
