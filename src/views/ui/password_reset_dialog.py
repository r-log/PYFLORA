from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PasswordResetDialog(object):
    def setupUi(self, PasswordResetDialog):
        PasswordResetDialog.setObjectName("PasswordResetDialog")
        PasswordResetDialog.resize(400, 300)

        # Just keep frameless window
        PasswordResetDialog.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint)

        PasswordResetDialog.setStyleSheet("""
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

        self.verticalLayout = QtWidgets.QVBoxLayout(PasswordResetDialog)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(15)

        # Title
        self.title_label = QtWidgets.QLabel(PasswordResetDialog)
        self.title_label.setStyleSheet("""
            QLabel {
                color: #ddd;
                font-size: 18px;
                font-weight: bold;
            }
        """)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.title_label)

        # Email label and input
        self.email_label = QtWidgets.QLabel(PasswordResetDialog)
        self.verticalLayout.addWidget(self.email_label)

        self.email_input = QtWidgets.QLineEdit(PasswordResetDialog)
        self.email_input.setPlaceholderText("Enter your email address")
        self.verticalLayout.addWidget(self.email_input)

        # Status label
        self.status_label = QtWidgets.QLabel(PasswordResetDialog)
        self.status_label.setStyleSheet("""
            QLabel {
                color: #8B8B8B;
                min-height: 20px;
            }
        """)
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.status_label)

        # Send button
        self.send_button = QtWidgets.QPushButton(PasswordResetDialog)
        self.verticalLayout.addWidget(self.send_button)

        # Add stretch to push everything up
        self.verticalLayout.addStretch()

        self.retranslateUi(PasswordResetDialog)
        QtCore.QMetaObject.connectSlotsByName(PasswordResetDialog)

    def retranslateUi(self, PasswordResetDialog):
        _translate = QtCore.QCoreApplication.translate
        PasswordResetDialog.setWindowTitle(
            _translate("PasswordResetDialog", "Reset Password"))
        self.title_label.setText(_translate(
            "PasswordResetDialog", "Reset Password"))
        self.email_label.setText(_translate(
            "PasswordResetDialog", "Email Address"))
        self.send_button.setText(_translate(
            "PasswordResetDialog", "Send Reset Link"))
