from PyQt6.QtCore import QObject, QEvent
from typing import Any


class UiEventFilter(QObject):
    """
    Event filter for handling UI focus events on password fields.
    Controls the visibility of password toggle buttons based on focus state.
    """

    def __init__(self, ui_handler):
        """
        Initialize the event filter.

        Args:
            ui_handler: The UI handler containing the password input fields
        """
        super().__init__()
        self.ui_handler = ui_handler

    def eventFilter(self, source: Any, event: QEvent) -> bool:
        """
        Filter UI events to handle password field focus.

        Args:
            source: The widget that generated the event
            event: The event that occurred

        Returns:
            bool: True if the event was handled, False otherwise
        """
        if event.type() == QEvent.Type.FocusOut:
            self._handle_focus_out(source)
        elif event.type() == QEvent.Type.FocusIn:
            self._handle_focus_in(source)

        return super().eventFilter(source, event)

    def _handle_focus_out(self, source: Any):
        """
        Handle focus out events for password fields.

        Args:
            source: The widget that lost focus
        """
        password_fields = {
            self.ui_handler.sign_in_password_input: self.ui_handler.sign_in_password_visible,
            self.ui_handler.sign_up_password_input: self.ui_handler.sign_up_password_visibile,
            self.ui_handler.sign_up_confirm_password_input: self.ui_handler.sign_up_confirm_password_visibile
        }

        if source in password_fields and not password_fields[source].underMouse():
            password_fields[source].hide()

    def _handle_focus_in(self, source: Any):
        """
        Handle focus in events for password fields.

        Args:
            source: The widget that gained focus
        """
        password_fields = {
            self.ui_handler.sign_in_password_input: self.ui_handler.sign_in_password_visible,
            self.ui_handler.sign_up_password_input: self.ui_handler.sign_up_password_visibile,
            self.ui_handler.sign_up_confirm_password_input: self.ui_handler.sign_up_confirm_password_visibile
        }

        if source in password_fields:
            password_fields[source].show()
