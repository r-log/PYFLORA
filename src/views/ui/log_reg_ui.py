from PyQt6 import QtCore, QtGui, QtWidgets
from res import res_rc_rc
from .custom_widgets import ClickableLabel


class Ui_LogRegWindow(object):
    def setupUi(self, LogRegWindow):
        LogRegWindow.setObjectName("LogRegWindow")
        LogRegWindow.resize(682, 591)
        self.window_box_widget = QtWidgets.QWidget(parent=LogRegWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.window_box_widget.sizePolicy().hasHeightForWidth())
        self.window_box_widget.setSizePolicy(sizePolicy)
        self.window_box_widget.setObjectName("window_box_widget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.window_box_widget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 681, 591))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.log_reg_frame_left = QtWidgets.QFrame(parent=self.layoutWidget)
        self.log_reg_frame_left.setStyleSheet("border-top-left-radius:50px;\n"
                                              "border-bottom-left-radius:50px;")
        self.log_reg_frame_left.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel)
        self.log_reg_frame_left.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.log_reg_frame_left.setObjectName("log_reg_frame_left")
        self.log_reg_background = QtWidgets.QLabel(
            parent=self.log_reg_frame_left)
        self.log_reg_background.setGeometry(QtCore.QRect(0, 0, 901, 591))
        self.log_reg_background.setStyleSheet("border-image: url(\":Images/Images/Background_plant.png\") 0 0 0 0 stretch stretch;\n"
                                              "background-position: center;\n"
                                              "background-size: cover;\n"
                                              "border-top-left-radius:50px;\n"
                                              "border-bottom-left-radius:50px;")
        self.log_reg_background.setText("")
        self.log_reg_background.setScaledContents(False)
        self.log_reg_background.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.log_reg_background.setObjectName("log_reg_background")
        self.horizontalLayout.addWidget(self.log_reg_frame_left)
        self.log_reg_frame_right = QtWidgets.QFrame(parent=self.layoutWidget)
        self.log_reg_frame_right.setEnabled(True)
        self.log_reg_frame_right.setStyleSheet("background-color: #0D2522;\n"
                                               "border-top-right-radius:50px;\n"
                                               "border-bottom-right-radius:50px;")
        self.log_reg_frame_right.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel)
        self.log_reg_frame_right.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.log_reg_frame_right.setObjectName("log_reg_frame_right")
        self.logo_widget = QtWidgets.QWidget(parent=self.log_reg_frame_right)
        self.logo_widget.setGeometry(QtCore.QRect(30, 40, 251, 91))
        self.logo_widget.setStyleSheet("background-color:transparent;")
        self.logo_widget.setObjectName("logo_widget")
        self.log_reg_py_text_label = QtWidgets.QLabel(parent=self.logo_widget)
        self.log_reg_py_text_label.setGeometry(QtCore.QRect(34, 15, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setKerning(True)
        self.log_reg_py_text_label.setFont(font)
        self.log_reg_py_text_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                 "font: 250 40pt \"Poppins\";\n"
                                                 "")
        self.log_reg_py_text_label.setFrameShadow(
            QtWidgets.QFrame.Shadow.Plain)
        self.log_reg_py_text_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.log_reg_py_text_label.setObjectName("log_reg_py_text_label")
        self.logo_line_label = QtWidgets.QFrame(parent=self.logo_widget)
        self.logo_line_label.setGeometry(QtCore.QRect(29, 10, 61, 51))
        self.logo_line_label.setStyleSheet("border: 0.5px solid white;\n"
                                           "border-style: inset;")
        self.logo_line_label.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.logo_line_label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.logo_line_label.setObjectName("logo_line_label")
        self.log_reg_flora_text_label = QtWidgets.QLabel(
            parent=self.logo_widget)
        self.log_reg_flora_text_label.setGeometry(
            QtCore.QRect(90, 40, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setKerning(True)
        self.log_reg_flora_text_label.setFont(font)
        self.log_reg_flora_text_label.setStyleSheet("font: 250 40pt \"Poppins\";\n"
                                                    "color: rgb(255, 255, 255);")
        self.log_reg_flora_text_label.setFrameShadow(
            QtWidgets.QFrame.Shadow.Plain)
        self.log_reg_flora_text_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.log_reg_flora_text_label.setObjectName("log_reg_flora_text_label")
        self.logo_line_label.raise_()
        self.log_reg_flora_text_label.raise_()
        self.log_reg_py_text_label.raise_()
        self.sign_up_widget = QtWidgets.QWidget(
            parent=self.log_reg_frame_right)
        self.sign_up_widget.setGeometry(QtCore.QRect(5, 39, 321, 531))
        self.sign_up_widget.setStyleSheet("background-color:transparent;")
        self.sign_up_widget.setObjectName("sign_up_widget")
        self.sign_up_password_input = QtWidgets.QLineEdit(
            parent=self.sign_up_widget)
        self.sign_up_password_input.setGeometry(QtCore.QRect(60, 231, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.sign_up_password_input.setFont(font)
        self.sign_up_password_input.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                  "background-color: transparent;\n"
                                                  "border:none;\n"
                                                  "border-style: outset;\n"
                                                  "border-width: 1px;\n"
                                                  "border-radius: 15px;\n"
                                                  "border-color: rgb(255, 255, 255);\n"
                                                  "min-width: 10em;\n"
                                                  "padding: 2px;")
        self.sign_up_password_input.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password)
        self.sign_up_password_input.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sign_up_password_input.setClearButtonEnabled(False)
        self.sign_up_password_input.setObjectName("sign_up_password_input")
        self.sign_up_username_input = QtWidgets.QLineEdit(
            parent=self.sign_up_widget)
        self.sign_up_username_input.setGeometry(QtCore.QRect(60, 191, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.sign_up_username_input.setFont(font)
        self.sign_up_username_input.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                  "background-color: transparent;\n"
                                                  "border:none;\n"
                                                  "border-style: outset;\n"
                                                  "border-width: 1px;\n"
                                                  "border-radius: 15px;\n"
                                                  "border-color: rgb(255, 255, 255);\n"
                                                  "min-width: 10em;\n"
                                                  "padding: 2px;")
        self.sign_up_username_input.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sign_up_username_input.setClearButtonEnabled(False)
        self.sign_up_username_input.setObjectName("sign_up_username_input")
        self.sing_up_text_label = QtWidgets.QLabel(parent=self.sign_up_widget)
        self.sing_up_text_label.setGeometry(QtCore.QRect(97, 116, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraLight")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        self.sing_up_text_label.setFont(font)
        self.sing_up_text_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.sing_up_text_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sing_up_text_label.setObjectName("sing_up_text_label")
        self.line_label = QtWidgets.QLabel(parent=self.sign_up_widget)
        self.line_label.setGeometry(QtCore.QRect(95, 136, 131, 16))
        self.line_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_label.setObjectName("line_label")
        self.have_account_text_label = QtWidgets.QLabel(
            parent=self.sign_up_widget)
        self.have_account_text_label.setGeometry(
            QtCore.QRect(60, 430, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.have_account_text_label.setFont(font)
        self.have_account_text_label.setStyleSheet(
            "color: rgb(255, 255, 255);")
        self.have_account_text_label.setObjectName("have_account_text_label")
        self.sign_up_confirm_password_input = QtWidgets.QLineEdit(
            parent=self.sign_up_widget)
        self.sign_up_confirm_password_input.setGeometry(
            QtCore.QRect(60, 269, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.sign_up_confirm_password_input.setFont(font)
        self.sign_up_confirm_password_input.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                          "background-color: transparent;\n"
                                                          "border:none;\n"
                                                          "border-style: outset;\n"
                                                          "border-width: 1px;\n"
                                                          "border-radius: 15px;\n"
                                                          "border-color: rgb(255, 255, 255);\n"
                                                          "min-width: 10em;\n"
                                                          "padding: 2px;")
        self.sign_up_confirm_password_input.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password)
        self.sign_up_confirm_password_input.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sign_up_confirm_password_input.setClearButtonEnabled(False)
        self.sign_up_confirm_password_input.setObjectName(
            "sign_up_confirm_password_input")
        self.sign_up_email_input = QtWidgets.QLineEdit(
            parent=self.sign_up_widget)
        self.sign_up_email_input.setGeometry(QtCore.QRect(60, 308, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.sign_up_email_input.setFont(font)
        self.sign_up_email_input.setStyleSheet("color: rgb(255, 255, 255);\n"
                                               "background-color: transparent;\n"
                                               "border:none;\n"
                                               "border-style: outset;\n"
                                               "border-width: 1px;\n"
                                               "border-radius: 15px;\n"
                                               "border-color: rgb(255, 255, 255);\n"
                                               "min-width: 10em;\n"
                                               "padding: 2px;")
        self.sign_up_email_input.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sign_up_email_input.setClearButtonEnabled(False)
        self.sign_up_email_input.setObjectName("sign_up_email_input")
        self.sign_up_button = QtWidgets.QPushButton(parent=self.sign_up_widget)
        self.sign_up_button.setGeometry(QtCore.QRect(111, 360, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.sign_up_button.setFont(font)
        self.sign_up_button.setStyleSheet("QPushButton#sign_up_button{\n"
                                          "    background-color: transparent;\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    border:1px solid white;\n"
                                          "    border-radius:10px;    \n"
                                          "}\n"
                                          "QPushButton#sign_up_button:hover{\n"
                                          "    background-color: rgb(18, 88, 83);\n"
                                          "}\n"
                                          "QPushButton#sign_up_button:pressed{\n"
                                          "    padding-left:5px;\n"
                                          "    padding-top:5px;\n"
                                          "}\n"
                                          "")
        self.sign_up_button.setObjectName("sign_up_button")
        self.sign_in_link = QtWidgets.QPushButton(parent=self.sign_up_widget)
        self.sign_in_link.setGeometry(QtCore.QRect(220, 431, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        self.sign_in_link.setFont(font)
        self.sign_in_link.setStyleSheet("QPushButton#sign_in_link{\n"
                                        "    color:rgba(255,255,255,210);\n"
                                        "    background-color: transparent;\n"
                                        "    font: 900 8pt \"Poppins\";\n"
                                        "}\n"
                                        "QPushButton#sign_in_link:hover{\n"
                                        "    color: rgb(18, 88, 83);\n"
                                        "}\n"
                                        "QPushButton#sign_in_link:pressed{\n"
                                        "    padding-left:5px;\n"
                                        "    padding-top:5px;\n"
                                        "}\n"
                                        "")
        self.sign_in_link.setObjectName("sign_in_link")
        self.sign_up_info_label = QtWidgets.QLabel(parent=self.sign_up_widget)
        self.sign_up_info_label.setGeometry(QtCore.QRect(72, 166, 181, 20))
        self.sign_up_info_label.setText("")
        self.sign_up_info_label.setObjectName("sign_up_info_label")
        self.sign_up_password_visibile = QtWidgets.QPushButton(
            parent=self.sign_up_widget)
        self.sign_up_password_visibile.setGeometry(
            QtCore.QRect(235, 238, 16, 16))
        self.sign_up_password_visibile.setMinimumSize(QtCore.QSize(16, 16))
        self.sign_up_password_visibile.setMaximumSize(QtCore.QSize(16, 16))
        self.sign_up_password_visibile.setStyleSheet(
            "background-color:transparent;")
        self.sign_up_password_visibile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/eye.svg"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/eye-off.svg"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.sign_up_password_visibile.setIcon(icon)
        self.sign_up_password_visibile.setCheckable(True)
        self.sign_up_show_password = QtWidgets.QPushButton(
            parent=self.sign_up_widget)
        self.sign_up_show_password.setGeometry(QtCore.QRect(237, 273, 16, 16))
        self.sign_up_show_password.setMinimumSize(QtCore.QSize(16, 16))
        self.sign_up_show_password.setMaximumSize(QtCore.QSize(16, 16))
        self.sign_up_show_password.setStyleSheet(
            "background-color:transparent;")
        self.sign_up_show_password.setText("")
        self.sign_up_show_password.setObjectName("sign_up_show_password")
        self.sign_in_widget = QtWidgets.QWidget(
            parent=self.log_reg_frame_right)
        self.sign_in_widget.setGeometry(QtCore.QRect(5, 40, 321, 511))
        self.sign_in_widget.setStyleSheet("background-color:transparent;")
        self.sign_in_widget.setObjectName("sign_in_widget")
        self.sign_in_password_input = QtWidgets.QLineEdit(
            parent=self.sign_in_widget)
        self.sign_in_password_input.setGeometry(QtCore.QRect(60, 230, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.sign_in_password_input.setFont(font)
        self.sign_in_password_input.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                  "background-color: transparent;\n"
                                                  "border:none;\n"
                                                  "border-style: outset;\n"
                                                  "border-width: 1px;\n"
                                                  "border-radius: 15px;\n"
                                                  "border-color: rgb(255, 255, 255);\n"
                                                  "min-width: 10em;\n"
                                                  "padding: 2px;")
        self.sign_in_password_input.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password)
        self.sign_in_password_input.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sign_in_password_input.setClearButtonEnabled(False)
        self.sign_in_password_input.setObjectName("sign_in_password_input")
        self.sign_in_username_input = QtWidgets.QLineEdit(
            parent=self.sign_in_widget)
        self.sign_in_username_input.setGeometry(QtCore.QRect(60, 190, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.sign_in_username_input.setFont(font)
        self.sign_in_username_input.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                  "background-color: transparent;\n"
                                                  "border:none;\n"
                                                  "border-style: outset;\n"
                                                  "border-width: 1px;\n"
                                                  "border-radius: 15px;\n"
                                                  "border-color: rgb(255, 255, 255);\n"
                                                  "min-width: 10em;\n"
                                                  "padding: 2px;")
        self.sign_in_username_input.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sign_in_username_input.setClearButtonEnabled(False)
        self.sign_in_username_input.setObjectName("sign_in_username_input")
        self.sing_in_text_label = QtWidgets.QLabel(parent=self.sign_in_widget)
        self.sing_in_text_label.setGeometry(QtCore.QRect(93, 115, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraLight")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        self.sing_in_text_label.setFont(font)
        self.sing_in_text_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "")
        self.sing_in_text_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sing_in_text_label.setObjectName("sing_in_text_label")
        self.line_label_2 = QtWidgets.QLabel(parent=self.sign_in_widget)
        self.line_label_2.setGeometry(QtCore.QRect(95, 135, 131, 16))
        self.line_label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color:transparent;")
        self.line_label_2.setObjectName("line_label_2")
        self.sign_in_button = QtWidgets.QPushButton(parent=self.sign_in_widget)
        self.sign_in_button.setGeometry(QtCore.QRect(110, 314, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.sign_in_button.setFont(font)
        self.sign_in_button.setStyleSheet("QPushButton#sign_in_button{\n"
                                          "    background-color:transparent;\n"
                                          "    color:rgba(255,255,255,210);\n"
                                          "    border-radius:10px;\n"
                                          "    border:1px solid white;\n"
                                          "    font: 300 11pt \"Poppins\";\n"
                                          "}\n"
                                          "QPushButton#sign_in_button:hover{\n"
                                          "    background-color: rgb(18, 88, 83);\n"
                                          "}\n"
                                          "QPushButton#sign_in_button:pressed{\n"
                                          "    padding-left:5px;\n"
                                          "    padding-top:5px;\n"
                                          "}\n"
                                          "")
        self.sign_in_button.setObjectName("sign_in_button")
        self.no_account_text_label = QtWidgets.QLabel(
            parent=self.sign_in_widget)
        self.no_account_text_label.setGeometry(QtCore.QRect(60, 430, 151, 16))
        self.no_account_text_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                 "font: 9pt \"Poppins\";")
        self.no_account_text_label.setObjectName("no_account_text_label")
        self.remember_me_checkbox = QtWidgets.QCheckBox(
            parent=self.sign_in_widget)
        self.remember_me_checkbox.setGeometry(QtCore.QRect(60, 264, 111, 20))
        self.remember_me_checkbox.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                "font: 300 8pt \"Poppins\";")
        self.remember_me_checkbox.setObjectName("remember_me_checkbox")
        self.forgot_password_label = QtWidgets.QLabel(self.sign_in_widget)
        self.forgot_password_label.setGeometry(QtCore.QRect(167, 266, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        self.forgot_password_label.setFont(font)
        self.forgot_password_label.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.forgot_password_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.forgot_password_label.setObjectName("forgot_password_label")
        self.forgot_password_label.setStyleSheet("""
            QLabel {
                color: #125853;
                font: 300 8pt "Poppins";
            }
            QLabel:hover {
                color: #1a7a72;
            }
        """)
        self.forgot_password_label.setCursor(
            QtCore.Qt.CursorShape.PointingHandCursor)
        self.sign_up_link = QtWidgets.QPushButton(parent=self.sign_in_widget)
        self.sign_up_link.setGeometry(QtCore.QRect(207, 431, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        self.sign_up_link.setFont(font)
        self.sign_up_link.setStyleSheet("QPushButton#sign_up_link{\n"
                                        "    color:rgba(255,255,255,210);\n"
                                        "    background-color: transparent;\n"
                                        "    font: 900 8pt \"Poppins\";\n"
                                        "}\n"
                                        "QPushButton#sign_up_link:hover{\n"
                                        "    color: rgb(18, 88, 83);\n"
                                        "}\n"
                                        "QPushButton#sign_up_link:pressed{\n"
                                        "    padding-left:5px;\n"
                                        "    padding-top:5px;\n"
                                        "}\n"
                                        "")
        self.sign_up_link.setObjectName("sign_up_link")
        self.sign_in_info_label = QtWidgets.QLabel(parent=self.sign_in_widget)
        self.sign_in_info_label.setGeometry(QtCore.QRect(65, 169, 191, 16))
        self.sign_in_info_label.setText("")
        self.sign_in_info_label.setObjectName("sign_in_info_label")
        self.sign_in_password_visible = QtWidgets.QPushButton(
            parent=self.sign_in_widget)
        self.sign_in_password_visible.setGeometry(
            QtCore.QRect(235, 237, 16, 16))
        self.sign_in_password_visible.setMinimumSize(QtCore.QSize(16, 16))
        self.sign_in_password_visible.setMaximumSize(QtCore.QSize(16, 16))
        self.sign_in_password_visible.setStyleSheet("background-color:transparent;\n"
                                                    "color: rgb(255, 255, 255);")
        self.sign_in_password_visible.setText("")
        self.sign_in_password_visible.setIcon(icon)
        self.sign_in_password_visible.setCheckable(True)
        self.sign_in_password_visible.setObjectName("sign_in_password_visible")
        self.exit_button = QtWidgets.QPushButton(
            parent=self.log_reg_frame_right)
        self.exit_button.setGeometry(QtCore.QRect(294, 23, 20, 20))
        self.exit_button.setStyleSheet("QPushButton#exit_button{\n"
                                       "    background-color: transparent;\n"
                                       "}\n"
                                       "QPushButton#exit_button:hover{\n"
                                       "    border:none;\n"
                                       "    border-style: outset;\n"
                                       "    border-color: rgb(255, 255, 255);\n"
                                       "    border-width: 1px;\n"
                                       "}\n"
                                       "QPushButton#exit_button:pressed{\n"
                                       "    padding-left:2px;\n"
                                       "    padding-top:2px;\n"
                                       "}")
        self.exit_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/Icons/Plus.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exit_button.setIcon(icon2)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout.addWidget(self.log_reg_frame_right)
        LogRegWindow.setCentralWidget(self.window_box_widget)

        self.retranslateUi(LogRegWindow)
        self.exit_button.clicked.connect(LogRegWindow.close)  # type: ignore

        # Set initial state
        self.sign_in_widget.show()
        self.sign_up_widget.hide()

        QtCore.QMetaObject.connectSlotsByName(LogRegWindow)

    def retranslateUi(self, LogRegWindow):
        _translate = QtCore.QCoreApplication.translate
        LogRegWindow.setWindowTitle(_translate("LogRegWindow", "LogRegWindow"))
        self.log_reg_py_text_label.setText(_translate("LogRegWindow", "PY"))
        self.log_reg_flora_text_label.setText(
            _translate("LogRegWindow", "FLORA"))
        self.sign_up_password_input.setPlaceholderText(
            _translate("LogRegWindow", "Password"))
        self.sign_up_username_input.setPlaceholderText(
            _translate("LogRegWindow", "Username"))
        self.sing_up_text_label.setText(_translate("LogRegWindow", "SIGN UP"))
        self.line_label.setText(_translate(
            "LogRegWindow", "___________________________"))
        self.have_account_text_label.setText(_translate(
            "LogRegWindow", "Already have an account?"))
        self.sign_up_confirm_password_input.setPlaceholderText(
            _translate("LogRegWindow", "Confirm password"))
        self.sign_up_email_input.setPlaceholderText(
            _translate("LogRegWindow", "E-mail"))
        self.sign_up_button.setText(_translate("LogRegWindow", "SIGN UP"))
        self.sign_in_link.setText(_translate("LogRegWindow", "SIGN IN"))
        self.sign_in_password_input.setPlaceholderText(
            _translate("LogRegWindow", "Password"))
        self.sign_in_username_input.setPlaceholderText(
            _translate("LogRegWindow", "Username"))
        self.sing_in_text_label.setText(_translate("LogRegWindow", "SIGN IN"))
        self.line_label_2.setText(_translate(
            "LogRegWindow", "___________________________"))
        self.sign_in_button.setText(_translate("LogRegWindow", "LOGIN"))
        self.no_account_text_label.setText(_translate(
            "LogRegWindow", "Don\'t have an account?"))
        self.remember_me_checkbox.setText(
            _translate("LogRegWindow", "Remember me"))
        self.forgot_password_label.setText(
            _translate("LogRegWindow", "Forgot password?"))
        self.sign_up_link.setText(_translate("LogRegWindow", "SIGN UP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogRegWindow = QtWidgets.QLogRegWindow()
    ui = Ui_LogRegWindow()
    ui.setupUi(LogRegWindow)
    LogRegWindow.show()
    sys.exit(app.exec())
