from applogic.input_validation import validate_username, validate_password, validate_email
from database.user_data_handler import create_user, check_user
from PyQt6.QtCore import QObject, pyqtSignal
import bcrypt
from .message_displayer import MessageDisplayer
from applogic.plant_management import decrypt_and_populate_plants


class LoginHandler(QObject):
    update_username = pyqtSignal(str)

    def __init__(self, ui_handler):
        super().__init__()
        self.ui_handler = ui_handler
        self.message_displayer = MessageDisplayer(ui_handler)

    def signup(self, username, password, confirm_password, email):
        self.message_displayer.clear_message(is_signup=True)

        is_valid, message = validate_username(username)
        if not is_valid:
            self.message_displayer.show_error(message, is_signup=True)
            return

        is_valid, message = validate_password(password, confirm_password)
        if not is_valid:
            self.message_displayer.show_error(message, is_signup=True)
            return

        is_valid, message = validate_email(email)
        if not is_valid:
            self.message_displayer.show_error(message, is_signup=True)
            return

        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())
        create_user(username, hashed_password, email)
        self.message_displayer.clear_message(is_signup=True)
        self.ui_handler.show_sign_in_widget()

    def signin(self, username, password):
        self.message_displayer.clear_message(is_signup=False)

        if check_user(username, password):
            # Assuming username is unique, alternatively use actual user_id
            self.ui_handler.set_user_id(username)
            self.ui_handler.open_main_window()
            self.update_username.emit(username)
            self.ui_handler.initialize_plants()
        else:
            self.message_displayer.show_error(
                "Invalid username or password!", is_signup=False)
