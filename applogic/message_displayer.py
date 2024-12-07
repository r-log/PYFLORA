from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class MessageDisplayer:
    def __init__(self, ui_handler):
        self.ui_handler = ui_handler

    def show_error(self, message, is_signup=True):
        if is_signup:
            self.ui_handler.sign_up_info_label.setText(message)
            self.ui_handler.sign_up_info_label.setStyleSheet("color: red;")
            self.ui_handler.sign_up_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.ui_handler.sign_up_info_label.setFont(QFont("Poppins", 8))
        else:
            self.ui_handler.sign_in_info_label.setText(message)
            self.ui_handler.sign_in_info_label.setStyleSheet("color: red;")
            self.ui_handler.sign_in_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.ui_handler.sign_in_info_label.setFont(QFont("Poppins", 8))

    def clear_message(self, is_signup=True):
        if is_signup:
            self.ui_handler.sign_up_info_label.setText("")
        else:
            self.ui_handler.sign_in_info_label.setText("")
