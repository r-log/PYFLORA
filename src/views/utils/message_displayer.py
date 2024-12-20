from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from typing import Optional


class MessageDisplayer:
    """Utility class for displaying messages in the UI."""

    def __init__(self, ui_handler):
        """
        Initialize the MessageDisplayer.

        Args:
            ui_handler: The UI instance containing the message labels
        """
        self.ui_handler = ui_handler
        self._setup_default_style()

    def _setup_default_style(self):
        """Set up default styling for message labels."""
        self.default_font = QFont("Poppins", 8)
        self.default_alignment = Qt.AlignmentFlag.AlignCenter

    def show_error(self, message: str, is_signup: bool = True):
        """
        Display an error message.

        Args:
            message (str): The error message to display
            is_signup (bool): Whether to show in signup or signin label
        """
        label = self._get_label(is_signup)
        self._style_label(label, message, "red")

    def show_success(self, message: str, is_signup: bool = True):
        """
        Display a success message.

        Args:
            message (str): The success message to display
            is_signup (bool): Whether to show in signup or signin label
        """
        label = self._get_label(is_signup)
        self._style_label(label, message, "green")

    def show_info(self, message: str, is_signup: bool = True):
        """
        Display an info message.

        Args:
            message (str): The info message to display
            is_signup (bool): Whether to show in signup or signin label
        """
        label = self._get_label(is_signup)
        self._style_label(label, message, "white")

    def clear_message(self, is_signup: bool = True):
        """
        Clear the message label.

        Args:
            is_signup (bool): Whether to clear signup or signin label
        """
        label = self._get_label(is_signup)
        label.setText("")

    def _get_label(self, is_signup: bool) -> QLabel:
        """
        Get the appropriate label based on context.

        Args:
            is_signup (bool): Whether to get signup or signin label

        Returns:
            QLabel: The selected message label
        """
        return (self.ui_handler.sign_up_info_label if is_signup
                else self.ui_handler.sign_in_info_label)

    def _style_label(self, label: QLabel, message: str, color: str):
        """
        Apply styling to a label.

        Args:
            label (QLabel): The label to style
            message (str): The message to display
            color (str): The color to use
        """
        label.setText(message)
        label.setStyleSheet(f"color: {color};")
        label.setAlignment(self.default_alignment)
        label.setFont(self.default_font)
