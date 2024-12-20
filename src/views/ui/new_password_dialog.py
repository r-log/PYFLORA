from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_NewPasswordDialog(object):
    def setupUi(self, NewPasswordDialog):
        NewPasswordDialog.setObjectName("NewPasswordDialog")
        NewPasswordDialog.resize(400, 300)

        # Just keep frameless window
        NewPasswordDialog.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint)

        NewPasswordDialog.setStyleSheet("""
            QDialog {
                background-color: #0D2522;
                border-radius: 10px;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #125853;
                border-radius: 4px;
                background: white;
                min-height: 25px;
            }
            QLineEdit:focus {
                border: 1px solid #1a7a72;
            }
            QPushButton {
                background-color: #125853;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                min-width: 100px;
                min-height: 30px;
            }
            QPushButton:hover {
                background-color: #1a7a72;
            }
            QPushButton:pressed {
                background-color: #125853;
            }
            QLabel {
                color: #8B8B8B;
            }
        """)

        self.verticalLayout = QtWidgets.QVBoxLayout(NewPasswordDialog)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(15)

        # Title
        self.title_label = QtWidgets.QLabel(NewPasswordDialog)
        self.title_label.setStyleSheet("""
            QLabel {
                color: #ddd;
                font-size: 18px;
                font-weight: bold;
            }
        """)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.title_label)

        # Password input
        self.password_label = QtWidgets.QLabel(NewPasswordDialog)
        self.verticalLayout.addWidget(self.password_label)

        self.password_input = QtWidgets.QLineEdit(NewPasswordDialog)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.verticalLayout.addWidget(self.password_input)

        # Confirm password input
        self.confirm_password_label = QtWidgets.QLabel(NewPasswordDialog)
        self.verticalLayout.addWidget(self.confirm_password_label)

        self.confirm_password_input = QtWidgets.QLineEdit(NewPasswordDialog)
        self.confirm_password_input.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password)
        self.verticalLayout.addWidget(self.confirm_password_input)

        # Show password checkbox
        self.show_password = QtWidgets.QCheckBox(NewPasswordDialog)
        self.show_password.setStyleSheet("""
            QCheckBox {
                color: #666;
            }
            QCheckBox::indicator {
                width: 15px;
                height: 15px;
            }
            QCheckBox::indicator:unchecked {
                border: 1px solid #ddd;
                background: white;
            }
            QCheckBox::indicator:checked {
                background: #125853;
                border: 1px solid #125853;
            }
        """)
        self.verticalLayout.addWidget(self.show_password)

        # Status label
        self.status_label = QtWidgets.QLabel(NewPasswordDialog)
        self.status_label.setStyleSheet("""
            QLabel {
                color: #8B8B8B;
                min-height: 20px;
            }
        """)
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.status_label)

        # Reset button
        self.reset_button = QtWidgets.QPushButton(NewPasswordDialog)
        self.verticalLayout.addWidget(self.reset_button)

        # Add stretch to push everything up
        self.verticalLayout.addStretch()

        self.retranslateUi(NewPasswordDialog)
        QtCore.QMetaObject.connectSlotsByName(NewPasswordDialog)

    def retranslateUi(self, NewPasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        NewPasswordDialog.setWindowTitle(
            _translate("NewPasswordDialog", "Reset Password"))
        self.title_label.setText(_translate(
            "NewPasswordDialog", "Reset Your Password"))
        self.password_label.setText(_translate(
            "NewPasswordDialog", "New Password"))
        self.confirm_password_label.setText(
            _translate("NewPasswordDialog", "Confirm Password"))
        self.show_password.setText(_translate(
            "NewPasswordDialog", "Show Password"))
        self.reset_button.setText(_translate(
            "NewPasswordDialog", "Reset Password"))
