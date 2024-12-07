from PyQt6.QtCore import QObject, QEvent


class UiEventFilter(QObject):
    def __init__(self, ui_handler):
        super().__init__()
        self.ui_handler = ui_handler

    def event_filter(self, source, event):
        if event.type() == QEvent.Type.FocusOut:
            if source == self.ui_handler.sign_in_password_input and not self.ui_handler.sign_in_password_visible.underMouse():
                self.ui_handler.sign_in_password_visible.hide()
            elif source == self.ui_handler.sign_up_password_input and not self.ui_handler.sign_up_password_visibile.underMouse():
                self.ui_handler.sign_up_password_visibile.hide()
            elif source == self.ui_handler.sign_up_confirm_password_input and not self.ui_handler.sign_up_confirm_password_visibile.underMouse():
                self.ui_handler.sign_up_confirm_password_visibile.hide()
        elif event.type() == QEvent.Type.FocusIn:
            if source == self.ui_handler.sign_in_password_input:
                self.ui_handler.sign_in_password_visible.show()
            elif source == self.ui_handler.sign_up_password_input:
                self.ui_handler.sign_up_password_visibile.show()
            elif source == self.ui_handler.sign_up_confirm_password_input:
                self.ui_handler.sign_up_confirm_password_visibile.show()

        return super().event_filter(source, event)
