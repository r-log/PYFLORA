from PyQt5 import QtWidgets, QtCore
from LoginUi import Ui_MainWindow
import sys
from app_logic import AppLogic
import re
from PyQt5.QtWidgets import QMessageBox


class LoginApp(QtWidgets.QWidget, Ui_MainWindow):
    def change_window(self):
        if self.signUp_arrow.isChecked():
            self.signUp_widget.show()
            self.signIn_widget.hide()
        else:
            self.signUp_widget.hide()
            self.signIn_widget.show()

    def exit_app(self):
        if self.exit_bttn.isChecked():
            sys.exit(app.exec_())
        else:
            MainWindow.show()

    def is_valid_email(self, email):
        # Define the regex pattern for a valid email address
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Use the re.match() function to check if the email matches the pattern
        if re.match(pattern, email):
            return True
        else:
            return False

    def register_user(self):
        # Retrieve data from input fields
        username = self.username_box_signup.text()
        password = self.password_box_signup.text()
        confirm_password = self.confirm_password_box_signup.text()
        email = self.email_box_signup.text()

        # Check if the password and confirm password match
        if self.app_logic.check_username_exists(username):
            QMessageBox.warning(self, "INFO", "Username already exists!")
            return

        if not self.is_valid_email(email):
            QMessageBox.warning(self, "INFO", "Invalid email.")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "INFO", "Password and Confirm Password do not match.")
            return

    def __init__(self):

        self.app_logic = AppLogic({
            'host': 'localhost',
            'user': 'root',
            'password': 'root',
            'database': 'pyflora_db',
            'auth_plugin': 'root'
        })

        self.app_logic.test_connection()  # Checking for a connection (debugging)

        super(LoginApp, self).__init__()
        self.setupUi(self)
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

        self.signUp_widget.hide()

        self.signUp_arrow.clicked.connect(self.change_window)
        self.exit_bttn.clicked.connect(self.exit_app)

        self.signup_bttn.clicked.connect(self.register_user)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = LoginApp()
    MainWindow.show()
    sys.exit(app.exec_())
