from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 565)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_widget_login = QtWidgets.QWidget(self.centralwidget)
        self.main_widget_login.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.main_widget_login.setObjectName("main_widget_login")

        self.login_bg_left = QtWidgets.QLabel(self.main_widget_login)
        self.login_bg_left.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.login_bg_left.setStyleSheet("border-image: url(:/images/images/flora_bg.png);\n"
                                         "border-bottom-left-radius:50px;\n"
                                         "border-top-left-radius:50px;\n"
                                         "")
        self.login_bg_left.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login_bg_left.setText("")
        self.login_bg_left.setObjectName("login_bg_left")
        self.login_bg_leftDarken = QtWidgets.QLabel(self.main_widget_login)
        self.login_bg_leftDarken.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.login_bg_leftDarken.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
                                               "border-bottom-left-radius:50px;\n"
                                               "border-top-left-radius:50px;\n"
                                               "")
        self.login_bg_leftDarken.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login_bg_leftDarken.setText("")
        self.login_bg_leftDarken.setObjectName("login_bg_leftDarken")

        self.login_bg_right = QtWidgets.QLabel(self.main_widget_login)
        self.login_bg_right.setEnabled(True)
        self.login_bg_right.setGeometry(QtCore.QRect(270, 30, 240, 430))
        self.login_bg_right.setStyleSheet("background-color:rgba(35, 93, 113, 255);\n"
                                          "border-top-right-radius:50px;\n"
                                          "border-bottom-right-radius:50px;")
        self.login_bg_right.setText("")
        self.login_bg_right.setObjectName("login_bg_right")

        self.signIn_widget = QtWidgets.QWidget(self.main_widget_login)
        self.signIn_widget.setGeometry(QtCore.QRect(280, 60, 211, 361))
        self.signIn_widget.setObjectName("signIn_widget")

        self.signUp_text_2 = QtWidgets.QLabel(self.signIn_widget)
        self.signUp_text_2.setGeometry(QtCore.QRect(160, 47, 61, 16))
        self.signUp_text_2.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.signUp_text_2.setFont(font)
        self.signUp_text_2.setObjectName("signUp_text_2")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.signIn_widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 300, 161, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.facebook_bttn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.facebook_bttn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Icons Social Media 8")
        font.setPointSize(20)
        self.facebook_bttn.setFont(font)
        self.facebook_bttn.setStyleSheet("QPushButton#facebook_bttn{\n"
                                         "    background-color: rgba(0,0,0,0);\n"
                                         "    color:rgba(100, 160, 160, 219);\n"
                                         "    border-radius:10px;\n"
                                         "}\n"
                                         "QPushButton#facebook_bttn:hover{\n"
                                         "    color: rgba(100, 160, 160, 255);\n"
                                         "}\n"
                                         "QPushButton#facebook_bttn:pressed{\n"
                                         "    padding-left:5px;\n"
                                         "    padding-top:5px;\n"
                                         "    color:rgba(120, 120, 255, 240)\n"
                                         "}")
        self.facebook_bttn.setObjectName("facebook_bttn")
        self.horizontalLayout.addWidget(self.facebook_bttn)

        self.github_bttn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.github_bttn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Icons Social Media 8")
        font.setPointSize(20)
        self.github_bttn.setFont(font)
        self.github_bttn.setStyleSheet("QPushButton#github_bttn{\n"
                                       "    background-color: rgba(0,0,0,0);\n"
                                       "    color:rgba(100, 160, 160, 219);\n"
                                       "    border-radius:10px;\n"
                                       "}\n"
                                       "QPushButton#github_bttn:hover{\n"
                                       "    color: rgba(100, 160, 160, 255);\n"
                                       "}\n"
                                       "QPushButton#github_bttn:pressed{\n"
                                       "    padding-left:5px;\n"
                                       "    padding-top:5px;\n"
                                       "    color:rgba(120, 120, 255, 240)\n"
                                       "}")
        self.github_bttn.setObjectName("github_bttn")
        self.horizontalLayout.addWidget(self.github_bttn)

        self.google_bttn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.google_bttn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Icons Social Media 8")
        font.setPointSize(20)
        self.google_bttn.setFont(font)
        self.google_bttn.setStyleSheet("QPushButton#google_bttn{\n"
                                       "    background-color: rgba(0,0,0,0);\n"
                                       "    color:rgba(100, 160, 160, 219);\n"
                                       "    border-radius:10px;\n"
                                       "}\n"
                                       "QPushButton#google_bttn:hover{\n"
                                       "    color: rgba(100, 160, 160, 255);\n"
                                       "}\n"
                                       "QPushButton#google_bttn:pressed{\n"
                                       "    padding-left:5px;\n"
                                       "    padding-top:5px;\n"
                                       "    color:rgba(120, 120, 255, 240)\n"
                                       "}")
        self.google_bttn.setObjectName("google_bttn")
        self.horizontalLayout.addWidget(self.google_bttn)

        self.username_box = QtWidgets.QLineEdit(self.signIn_widget)
        self.username_box.setGeometry(QtCore.QRect(20, 160, 171, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.username_box.setFont(font)
        self.username_box.setStyleSheet("border-radius:10px;")
        self.username_box.setMaxLength(30)
        self.username_box.setAlignment(QtCore.Qt.AlignCenter)
        self.username_box.setClearButtonEnabled(False)
        self.username_box.setObjectName("username_box")

        self.login_bttn = QtWidgets.QPushButton(self.signIn_widget)
        self.login_bttn.setGeometry(QtCore.QRect(70, 250, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.login_bttn.setFont(font)
        self.login_bttn.setStyleSheet("QPushButton#login_bttn{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(100, 160, 160, 219), stop:1 rgba(167, 167, 255, 226));\n"
                                      "    color:rgba(255,255,255,210);\n"
                                      "    border-radius:10px;\n"
                                      "}\n"
                                      "QPushButton#login_bttn:hover{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(100, 160, 160, 255), stop:1 rgba(167, 167, 255, 255));\n"
                                      "}\n"
                                      "QPushButton#login_bttn:pressed{\n"
                                      "    padding-left:5px;\n"
                                      "    padding-top:5px;\n"
                                      "    background-color:rgba(120, 120, 255, 240)\n"
                                      "}")
        self.login_bttn.setObjectName("login_bttn")

        self.signIn_text = QtWidgets.QLabel(self.signIn_widget)
        self.signIn_text.setGeometry(QtCore.QRect(55, 120, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.signIn_text.setFont(font)
        self.signIn_text.setStyleSheet("color:rgba(255, 255, 255, 255)")
        self.signIn_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.signIn_text.setLineWidth(1)
        self.signIn_text.setAlignment(QtCore.Qt.AlignCenter)
        self.signIn_text.setObjectName("signIn_text")

        self.password_box = QtWidgets.QLineEdit(self.signIn_widget)
        self.password_box.setGeometry(QtCore.QRect(20, 190, 171, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.password_box.setFont(font)
        self.password_box.setStyleSheet("border-radius:10px;")
        self.password_box.setMaxLength(30)
        self.password_box.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_box.setAlignment(QtCore.Qt.AlignCenter)
        self.password_box.setObjectName("password_box")

        self.rememberMe_checkBox = QtWidgets.QCheckBox(self.signIn_widget)
        self.rememberMe_checkBox.setGeometry(QtCore.QRect(20, 211, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.rememberMe_checkBox.setFont(font)
        self.rememberMe_checkBox.setStyleSheet("color:rgba(0,0,0,210)")
        self.rememberMe_checkBox.setCheckable(True)
        self.rememberMe_checkBox.setChecked(False)
        self.rememberMe_checkBox.setObjectName("rememberMe_checkBox")

        self.forgotPass_text = QtWidgets.QLabel(self.signIn_widget)
        self.forgotPass_text.setGeometry(QtCore.QRect(110, 211, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.forgotPass_text.setFont(font)
        self.forgotPass_text.setStyleSheet("color:rgba(0,0,0,210)")
        self.forgotPass_text.setAlignment(QtCore.Qt.AlignCenter)
        self.forgotPass_text.setOpenExternalLinks(True)
        self.forgotPass_text.setObjectName("forgotPass_text")

        self.header_text_py = QtWidgets.QLabel(self.main_widget_login)
        self.header_text_py.setGeometry(QtCore.QRect(280, 60, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(16)
        self.header_text_py.setFont(font)
        self.header_text_py.setStyleSheet("color:rgba(255, 255, 255, 255)")
        self.header_text_py.setObjectName("header_text_py")

        self.header_line = QtWidgets.QLabel(self.main_widget_login)
        self.header_line.setGeometry(QtCore.QRect(190, 50, 241, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.header_line.setFont(font)
        self.header_line.setStyleSheet("color:rgba(255, 255, 255, 255)\n"
                                       "")
        self.header_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.header_line.setText("")
        self.header_line.setAlignment(QtCore.Qt.AlignCenter)
        self.header_line.setObjectName("header_line")

        self.header_text_flora = QtWidgets.QLabel(self.main_widget_login)
        self.header_text_flora.setGeometry(QtCore.QRect(310, 62, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(16)
        self.header_text_flora.setFont(font)
        self.header_text_flora.setStyleSheet("color:rgba(255, 255, 255, 255)")
        self.header_text_flora.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.header_text_flora.setObjectName("header_text_flora")

        self.signUp_arrow = QtWidgets.QPushButton(self.main_widget_login)
        self.signUp_arrow.setGeometry(QtCore.QRect(410, 100, 30, 30))
        self.signUp_arrow.setMaximumSize(QtCore.QSize(30, 30))
        self.signUp_arrow.setStyleSheet("QPushButton#signUp_arrow{\n"
                                        "    background-color: rgba(0,0,0,0);\n"
                                        "    color:rgba(100, 160, 160, 219);\n"
                                        "    border-radius:10px;\n"
                                        "}\n"
                                        "QPushButton#signUp_arrow:hover{\n"
                                        "    color: rgba(100, 160, 160, 255);\n"
                                        "}\n"
                                        "QPushButton#signUp_arrow:pressed{\n"
                                        "    padding-left:5px;\n"
                                        "    padding-top:5px;\n"
                                        "    color:rgba(120, 120, 255, 240)\n"
                                        "}")
        self.signUp_arrow.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/arrow-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signUp_arrow.setIcon(icon)
        self.signUp_arrow.setCheckable(True)
        self.signUp_arrow.setObjectName("signUp_arrow")

        self.signUp_widget = QtWidgets.QWidget(self.main_widget_login)
        self.signUp_widget.setGeometry(QtCore.QRect(280, 60, 211, 361))
        self.signUp_widget.setObjectName("signUp_widget")

        self.signUp_text = QtWidgets.QLabel(self.signUp_widget)
        self.signUp_text.setGeometry(QtCore.QRect(60, 80, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.signUp_text.setFont(font)
        self.signUp_text.setStyleSheet("color:rgba(255, 255, 255, 255)")
        self.signUp_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.signUp_text.setLineWidth(1)
        self.signUp_text.setAlignment(QtCore.Qt.AlignCenter)
        self.signUp_text.setObjectName("signUp_text")

        self.signup_bttn = QtWidgets.QPushButton(self.signUp_widget)
        self.signup_bttn.setGeometry(QtCore.QRect(70, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.signup_bttn.setFont(font)
        self.signup_bttn.setStyleSheet("QPushButton#signup_bttn{\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(100, 160, 160, 219), stop:1 rgba(167, 167, 255, 226));\n"
                                       "    color:rgba(255,255,255,210);\n"
                                       "    border-radius:10px;\n"
                                       "}\n"
                                       "QPushButton#signup_bttn:hover{\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(100, 160, 160, 255), stop:1 rgba(167, 167, 255, 255));\n"
                                       "}\n"
                                       "QPushButton#signup_bttn:pressed{\n"
                                       "    padding-left:5px;\n"
                                       "    padding-top:5px;\n"
                                       "    background-color:rgba(120, 120, 255, 240)\n"
                                       "}")
        self.signup_bttn.setObjectName("signup_bttn")

        self.signIn_text_signup = QtWidgets.QLabel(self.signUp_widget)
        self.signIn_text_signup.setGeometry(QtCore.QRect(160, 47, 61, 16))
        self.signIn_text_signup.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.signIn_text_signup.setFont(font)
        self.signIn_text_signup.setObjectName("signIn_text_signup")

        self.username_box_signup = QtWidgets.QLineEdit(self.signUp_widget)
        self.username_box_signup.setGeometry(QtCore.QRect(20, 130, 171, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.username_box_signup.setFont(font)
        self.username_box_signup.setStyleSheet("border-radius:10px;")
        self.username_box_signup.setMaxLength(30)
        self.username_box_signup.setAlignment(QtCore.Qt.AlignCenter)
        self.username_box_signup.setClearButtonEnabled(False)
        self.username_box_signup.setObjectName("username_box_signup")

        self.email_box_signup = QtWidgets.QLineEdit(self.signUp_widget)
        self.email_box_signup.setGeometry(QtCore.QRect(20, 160, 171, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.email_box_signup.setFont(font)
        self.email_box_signup.setStyleSheet("border-radius:10px;")
        self.email_box_signup.setText("")
        self.email_box_signup.setMaxLength(30)
        self.email_box_signup.setAlignment(QtCore.Qt.AlignCenter)
        self.email_box_signup.setClearButtonEnabled(False)
        self.email_box_signup.setObjectName("email_box_signup")

        self.password_box_signup = QtWidgets.QLineEdit(self.signUp_widget)
        self.password_box_signup.setGeometry(QtCore.QRect(20, 190, 171, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.password_box_signup.setFont(font)
        self.password_box_signup.setStyleSheet("border-radius:10px;")
        self.password_box_signup.setMaxLength(30)
        self.password_box_signup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_box_signup.setAlignment(QtCore.Qt.AlignCenter)
        self.password_box_signup.setObjectName("password_box_signup")

        self.confirm_password_box_signup = QtWidgets.QLineEdit(self.signUp_widget)
        self.confirm_password_box_signup.setGeometry(QtCore.QRect(20, 220, 171, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.confirm_password_box_signup.setFont(font)
        self.confirm_password_box_signup.setStyleSheet("border-radius:10px;")
        self.confirm_password_box_signup.setText("")
        self.confirm_password_box_signup.setMaxLength(30)
        self.confirm_password_box_signup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_box_signup.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_password_box_signup.setObjectName("confirm_password_box_signup")

        self.exit_bttn = QtWidgets.QPushButton(self.main_widget_login)
        self.exit_bttn.setGeometry(QtCore.QRect(459, 50, 30, 30))
        font = QtGui.QFont()
        self.exit_bttn.setCheckable(True)
        font.setFamily("Microsoft JhengHei UI Light")
        self.exit_bttn.setFont(font)
        self.exit_bttn.setStyleSheet("QPushButton#exit_bttn{\n"
                                     "    background-color: rgba(0,0,0,0);\n"
                                     "    color:rgba(0, 160, 160, 219);\n"
                                     "    border-radius:10px;\n"
                                     "}\n"
                                     "QPushButton#exit_bttn:hover{\n"
                                     "    color: rgba(100, 160, 160, 255);\n"
                                     "}\n"
                                     "QPushButton#exit_bttn:pressed{\n"
                                     "    padding-left:5px;\n"
                                     "    padding-top:5px;\n"
                                     "    color:rgba(120, 120, 255, 240)\n"
                                     "}")
        self.exit_bttn.setObjectName("exit_bttn")

        self.login_bg_left.raise_()
        self.login_bg_leftDarken.raise_()
        self.login_bg_right.raise_()

        self.header_text_py.raise_()
        self.header_line.raise_()
        self.header_text_flora.raise_()

        self.signIn_widget.raise_()

        self.signUp_widget.raise_()
        self.signUp_arrow.raise_()

        self.exit_bttn.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.signUp_text_2.setText(_translate("MainWindow", "SIGN UP"))
        self.facebook_bttn.setText(_translate("MainWindow", "f"))
        self.github_bttn.setText(_translate("MainWindow", "<"))
        self.google_bttn.setText(_translate("MainWindow", "g"))
        self.username_box.setPlaceholderText(_translate("MainWindow", "Username"))
        self.login_bttn.setText(_translate("MainWindow", "LOGIN"))
        self.signIn_text.setText(_translate("MainWindow", "- SIGN IN -"))
        self.password_box.setPlaceholderText(_translate("MainWindow", "Password"))
        self.rememberMe_checkBox.setText(_translate("MainWindow", "Remember me"))
        self.forgotPass_text.setText(_translate("MainWindow", "Forgot password?"))
        self.header_text_py.setText(_translate("MainWindow", "PY"))
        self.header_text_flora.setText(_translate("MainWindow", "FLORA"))
        self.signUp_text.setText(_translate("MainWindow", "- SIGN UP -"))
        self.signup_bttn.setText(_translate("MainWindow", "SIGN-UP"))
        self.signIn_text_signup.setText(_translate("MainWindow", "SIGN IN"))
        self.username_box_signup.setPlaceholderText(_translate("MainWindow", "Username"))
        self.email_box_signup.setPlaceholderText(_translate("MainWindow", "E-mail"))
        self.password_box_signup.setPlaceholderText(_translate("MainWindow", "Password"))
        self.confirm_password_box_signup.setPlaceholderText(_translate("MainWindow", "Confirm password"))
        self.exit_bttn.setText(_translate("MainWindow", "X"))
