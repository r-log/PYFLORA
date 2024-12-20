from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ChangePasswordDialog(object):
    def setupUi(self, ChangePasswordDialog):
        ChangePasswordDialog.setObjectName("ChangePasswordDialog")
        ChangePasswordDialog.resize(400, 300)

        # Just keep frameless window
        ChangePasswordDialog.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint)

        ChangePasswordDialog.setStyleSheet("""
            QDialog {
                background-color: #0D2522;
                border-radius: 10px;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #125853;
                border-radius: 4px;
                background: white;
                color: black;
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

        self.verticalLayout = QtWidgets.QVBoxLayout(ChangePasswordDialog)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(15)

        # Title
        self.title_label = QtWidgets.QLabel(ChangePasswordDialog)
        self.title_label.setStyleSheet("""
            QLabel {
                color: #ddd;
                font-size: 18px;
                font-weight: bold;
            }
        """)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.title_label)

        # Current Password
        self.current_password_label = QtWidgets.QLabel(ChangePasswordDialog)
        self.verticalLayout.addWidget(self.current_password_label)

        self.current_password_input = QtWidgets.QLineEdit(ChangePasswordDialog)
        self.current_password_input.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password)
        self.verticalLayout.addWidget(self.current_password_input)

        # New Password
        self.new_password_label = QtWidgets.QLabel(ChangePasswordDialog)
        self.verticalLayout.addWidget(self.new_password_label)

        self.new_password_input = QtWidgets.QLineEdit(ChangePasswordDialog)
        self.new_password_input.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password)
        self.verticalLayout.addWidget(self.new_password_input)

        # Confirm New Password
        self.confirm_password_label = QtWidgets.QLabel(ChangePasswordDialog)
        self.verticalLayout.addWidget(self.confirm_password_label)

        self.confirm_password_input = QtWidgets.QLineEdit(ChangePasswordDialog)
        self.confirm_password_input.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password)
        self.verticalLayout.addWidget(self.confirm_password_input)

        # Show password checkbox
        self.show_password = QtWidgets.QCheckBox(ChangePasswordDialog)
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
        self.status_label = QtWidgets.QLabel(ChangePasswordDialog)
        self.status_label.setStyleSheet("""
            QLabel {
                color: #8B8B8B;
                min-height: 20px;
            }
        """)
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.status_label)

        # Change button
        self.change_button = QtWidgets.QPushButton(ChangePasswordDialog)
        self.verticalLayout.addWidget(self.change_button)

        # Add stretch to push everything up
        self.verticalLayout.addStretch()

        self.retranslateUi(ChangePasswordDialog)
        QtCore.QMetaObject.connectSlotsByName(ChangePasswordDialog)

    def retranslateUi(self, ChangePasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        ChangePasswordDialog.setWindowTitle(
            _translate("ChangePasswordDialog", "Change Password"))
        self.title_label.setText(_translate(
            "ChangePasswordDialog", "Change Password"))
        self.current_password_label.setText(
            _translate("ChangePasswordDialog", "Current Password"))
        self.new_password_label.setText(
            _translate("ChangePasswordDialog", "New Password"))
        self.confirm_password_label.setText(
            _translate("ChangePasswordDialog", "Confirm New Password"))
        self.change_button.setText(
            _translate("ChangePasswordDialog", "Change Password"))
        self.show_password.setText(
            _translate("ChangePasswordDialog", "Show Password"))
