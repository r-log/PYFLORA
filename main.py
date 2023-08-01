from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from LoginUi import UiLoginWindow
from app_logic import AppLogic
import sys


class LoginApp(QtWidgets.QWidget, UiLoginWindow):
    def __init__(self):
        super(LoginApp, self).__init__()
        self.setup_ui(self)

        # Initialize the AppLogic instance
        self.app_logic = AppLogic({
            'host': 'localhost',
            'user': 'root',
            'password': 'root',
            'database': 'pyflora_db',
            'auth_plugin': 'root'
        })

        # Checking for a database connection (debugging)
        self.app_logic.test_connection()

        # Connect signals to slots
        self.signUp_arrow.clicked.connect(self.change_window)
        self.exit_bttn.clicked.connect(self.exit_app)
        self.signup_bttn.clicked.connect(self.register_user)
        self.login_bttn.clicked.connect(self.login_user)


        # Set graphics effects for buttons
        self.login_bttn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.signup_bttn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.email_box_signup.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.confirm_password_box_signup.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.password_box_signup.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.username_box_signup.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.password_box.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.username_box.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        # Hide the signup widget initially
        self.signUp_widget.hide()

    def change_window(self):
        # Toggle between sign up and sign in widgets
        if self.signUp_arrow.isChecked():
            self.signUp_widget.show()
            self.signIn_widget.hide()
        else:
            self.signUp_widget.hide()
            self.signIn_widget.show()

    def exit_app(self):
        # Exit the application
        if self.exit_bttn.isChecked():
            sys.exit(app.exec_())
        else:
            LoginWindow.show()

    def register_user(self):
        # Retrieve data from input fields
        username = self.username_box_signup.text()
        password = self.password_box_signup.text()
        confirm_password = self.confirm_password_box_signup.text()
        email = self.email_box_signup.text()

        # Check if the username already exists in the database
        if self.app_logic.check_username_exists(username):
            QMessageBox.warning(self, "INFO", "Username already exists!")
            return

        # Check if the email is valid
        if not self.app_logic.is_valid_email(email):
            QMessageBox.warning(self, "INFO", "Invalid email.")
            return

        # Check if the password and confirm password match
        if password != confirm_password:
            QMessageBox.warning(self, "INFO", "Password and Confirm Password do not match.")
            return

        # If everything is valid, save user data to the database
        self.app_logic.save_user_data(username, password, email)

    def login_user(self):
        # Retrieve data from login input fields
        username = self.username_box.text()
        password = self.password_box.text()

        # Check if the username and password are correct
        if self.app_logic.verify_user_credentials(username, password):
            QMessageBox.information(self, "INFO", "Login successful!")
            LoginWindow.hide()
        else:
            QMessageBox.warning(self, "INFO", "Invalid username or password.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = LoginApp()
    LoginWindow.show()
    sys.exit(app.exec_())
