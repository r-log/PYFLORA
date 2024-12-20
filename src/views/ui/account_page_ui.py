from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AccountPage(object):
    def setupUi(self, AccountPage):
        AccountPage.setObjectName("AccountPage")
        AccountPage.setStyleSheet("""
            QWidget {
                background-color: transparent;
                color: white;
            }
            QLabel {
                font-family: 'Poppins';
                color: white;
            }
            QPushButton {
                background-color: #125853;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-family: 'Poppins';
                font-size: 10pt;
            }
            QPushButton:hover {
                background-color: #1a7a72;
            }
            QLineEdit {
                background-color: #125853;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px;
                font-family: 'Poppins';
                font-size: 10pt;
            }
            QLineEdit:focus {
                background-color: #1a7a72;
            }
        """)

        # Main Layout
        self.main_layout = QtWidgets.QVBoxLayout(AccountPage)
        self.main_layout.setContentsMargins(30, 30, 30, 30)
        self.main_layout.setSpacing(20)

        # Profile Section
        self.profile_group = QtWidgets.QGroupBox("Profile")
        self.profile_group.setStyleSheet("""
            QGroupBox {
                border: 1px solid #125853;
                border-radius: 5px;
                margin-top: 1em;
                padding-top: 10px;
            }
            QGroupBox::title {
                color: white;
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        self.profile_layout = QtWidgets.QVBoxLayout(self.profile_group)

        # Profile Picture
        self.profile_pic_layout = QtWidgets.QHBoxLayout()
        self.profile_pic = QtWidgets.QLabel()
        self.profile_pic.setFixedSize(100, 100)
        self.profile_pic.setStyleSheet("""
            background-color: #125853;
            border-radius: 50px;
        """)
        self.change_pic_btn = QtWidgets.QPushButton("Change Picture")
        self.profile_pic_layout.addWidget(self.profile_pic)
        self.profile_pic_layout.addWidget(self.change_pic_btn)
        self.profile_pic_layout.addStretch()
        self.profile_layout.addLayout(self.profile_pic_layout)

        # User Info
        self.info_layout = QtWidgets.QGridLayout()
        labels = ["Username:", "Email:", "Member Since:", "Last Login:"]
        self.info_fields = {}

        for i, label in enumerate(labels):
            label_widget = QtWidgets.QLabel(label)
            value_widget = QtWidgets.QLabel("Loading...")
            self.info_fields[label] = value_widget
            self.info_layout.addWidget(label_widget, i, 0)
            self.info_layout.addWidget(value_widget, i, 1)

        self.profile_layout.addLayout(self.info_layout)
        self.main_layout.addWidget(self.profile_group)

        # Account Settings Section
        self.settings_group = QtWidgets.QGroupBox("Account Settings")
        self.settings_group.setStyleSheet(self.profile_group.styleSheet())
        self.settings_layout = QtWidgets.QVBoxLayout(self.settings_group)

        # Settings Buttons
        settings_buttons = [
            "Change Password",
            "Update Email",
            "Notification Preferences"
        ]

        self.settings_button_refs = {}  # Store button references
        for button_text in settings_buttons:
            button = QtWidgets.QPushButton(button_text)
            self.settings_button_refs[button_text] = button  # Store reference
            self.settings_layout.addWidget(button)

        self.main_layout.addWidget(self.settings_group)

        # Account Actions Section
        self.actions_group = QtWidgets.QGroupBox("Account Actions")
        self.actions_group.setStyleSheet(self.profile_group.styleSheet())
        self.actions_layout = QtWidgets.QHBoxLayout(self.actions_group)

        self.export_data_btn = QtWidgets.QPushButton("Export Data")
        self.delete_account_btn = QtWidgets.QPushButton("Delete Account")
        self.delete_account_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF5252;
            }
            QPushButton:hover {
                background-color: #FF0000;
            }
        """)

        self.actions_layout.addWidget(self.export_data_btn)
        self.actions_layout.addWidget(self.delete_account_btn)
        self.main_layout.addWidget(self.actions_group)

        # Add stretch to push everything up
        self.main_layout.addStretch()
