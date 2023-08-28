from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMessageBox

import app_logic
from MainWindowUI import Ui_MainWindow
from LoginUi import UiLoginWindow
from app_logic import AppLogic
from temperature_monitor import TemperatureMonitor
import sys


class LoginApp(QtWidgets.QWidget, UiLoginWindow, QObject, Ui_MainWindow):
    def __init__(self):
        super(LoginApp, self).__init__()
        self.setup_login_ui(self)

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

        self.app_logic.credentials_verified.connect(self.update_username_placeholder)

    def update_username_placeholder(self, username=):
        self.Ui_MainWindow.sidemenu_username_placeholder.setText(f'{username}')

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
        LoginWindow.hide()
        self.sidemenu_username_placeholder.setText(f'{username}')
        MainWindow.show()

    def login_user(self):
        # Retrieve data from login input fields
        username = self.username_box.text()
        password = self.password_box.text()

        # Check if the username and password are correct
        if self.app_logic.verify_user_credentials(username, password):
            LoginWindow.hide()
            MainWindow.show()
            QMessageBox.information(self, "INFO", "Login successful!")
        else:
            QMessageBox.warning(self, "INFO", "Invalid username or password.")


class MainApp(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setup_main_ui(self)

        self.exit_bttn_mw.clicked.connect(self.exit_app)
        self.log_out_bttn.clicked.connect(self.log_out)

    def exit_app(self):
        # Exit the application
        if self.exit_bttn_mw.isChecked():
            sys.exit(app.exec_())
        else:
            MainWindow.show()

    def log_out(self):
        # Loggin out of the application
        if self.log_out_bttn.isChecked():
            # QMessageBox.warning(self, "INFO", "Are you sure you want to log-out?") *add a function to leave or not
            LoginWindow.show()
            MainWindow.hide()
        else:
            MainWindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = LoginApp()
    LoginWindow.show()
    MainWindow = MainApp()
    sys.exit(app.exec_())
