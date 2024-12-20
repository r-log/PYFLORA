# Get absolute path to res directory
from res import res_rc_rc
import os
import sys
from PyQt6 import QtCore, QtGui, QtWidgets

res_path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__)))), 'res')
sys.path.append(res_path)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1171, 614)
        self.main_widget = QtWidgets.QWidget(parent=MainWindow)
        self.main_widget.setStyleSheet("QWidget#main_widget {\n"
                                       "           border-image: url(\":Images/Images/Background_plant.png\") 0 0 0 0         stretch stretch;\n"
                                       "    border-radius:10px;\n"
                                       "}")
        self.main_widget.setObjectName("main_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 50)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.header_widget = QtWidgets.QWidget(parent=self.main_widget)
        self.header_widget.setMinimumSize(QtCore.QSize(0, 70))
        self.header_widget.setMaximumSize(QtCore.QSize(16777215, 70))
        self.header_widget.setStyleSheet("background-color:transparent;")
        self.header_widget.setObjectName("header_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.logo_widget_mainwindow = QtWidgets.QWidget(
            parent=self.header_widget)
        self.logo_widget_mainwindow.setMinimumSize(QtCore.QSize(180, 70))
        self.logo_widget_mainwindow.setMaximumSize(QtCore.QSize(180, 70))
        self.logo_widget_mainwindow.setStyleSheet(
            "background-color:transparent;")
        self.logo_widget_mainwindow.setObjectName("logo_widget_mainwindow")
        self.log_reg_py_text_label = QtWidgets.QLabel(
            parent=self.logo_widget_mainwindow)
        self.log_reg_py_text_label.setGeometry(QtCore.QRect(1, 1, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setKerning(True)
        self.log_reg_py_text_label.setFont(font)
        self.log_reg_py_text_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                 "font: 250 30pt \"Poppins\";\n"
                                                 "")
        self.log_reg_py_text_label.setFrameShadow(
            QtWidgets.QFrame.Shadow.Plain)
        self.log_reg_py_text_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.log_reg_py_text_label.setObjectName("log_reg_py_text_label")
        self.logo_line_label = QtWidgets.QFrame(
            parent=self.logo_widget_mainwindow)
        self.logo_line_label.setGeometry(QtCore.QRect(0, 0, 51, 41))
        self.logo_line_label.setStyleSheet("border: 0.5px solid white;\n"
                                           "border-style: inset;")
        self.logo_line_label.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.logo_line_label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.logo_line_label.setObjectName("logo_line_label")
        self.log_reg_flora_text_label = QtWidgets.QLabel(
            parent=self.logo_widget_mainwindow)
        self.log_reg_flora_text_label.setGeometry(
            QtCore.QRect(34, 19, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setKerning(True)
        self.log_reg_flora_text_label.setFont(font)
        self.log_reg_flora_text_label.setStyleSheet("font: 250 30pt \"Poppins\";\n"
                                                    "color: rgb(255, 255, 255);")
        self.log_reg_flora_text_label.setFrameShadow(
            QtWidgets.QFrame.Shadow.Plain)
        self.log_reg_flora_text_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.log_reg_flora_text_label.setObjectName("log_reg_flora_text_label")
        self.horizontalLayout_4.addWidget(self.logo_widget_mainwindow)
        spacerItem = QtWidgets.QSpacerItem(
            108, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.header_widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(166, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(266, 16777215))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border:none;\n"
                                    "border-style: outset;\n"
                                    "border-width: 1px;\n"
                                    "border-radius: 10px;\n"
                                    "border-color: rgb(0, 0, 0);\n"
                                    "min-width: 10em;\n"
                                    "padding: 2px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.search_button = QtWidgets.QPushButton(parent=self.header_widget)
        self.search_button.setMinimumSize(QtCore.QSize(31, 31))
        self.search_button.setMaximumSize(QtCore.QSize(31, 31))
        self.search_button.setStyleSheet("QPushButton#search_button{\n"
                                         "    background-color: rgb(18, 88, 83);\n"
                                         "    border-radius:15px;\n"
                                         "}\n"
                                         "QPushButton#search_button:hover{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255));\n"
                                         "}\n"
                                         "QPushButton#search_button:pressed{\n"
                                         "    background-color:rgba(18, 88, 83, 240)\n"
                                         "}")
        self.search_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/magnifying-glass-thin.svg"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search_button.setIcon(icon)
        self.search_button.setCheckable(True)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_4.addWidget(self.search_button)
        spacerItem1 = QtWidgets.QSpacerItem(
            107, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.widget_5 = QtWidgets.QWidget(parent=self.header_widget)
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_5.setStyleSheet("background-color: rgb(18, 88, 83);\n"
                                    "border-radius:15px;")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 6, 6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.notification_button = QtWidgets.QPushButton(parent=self.widget_5)
        self.notification_button.setMinimumSize(QtCore.QSize(31, 31))
        self.notification_button.setMaximumSize(QtCore.QSize(31, 31))
        self.notification_button.setStyleSheet("background-color: rgb(18, 88, 83);\n"
                                               "border-radius:15px;")
        self.notification_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons/bell-thin.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons/bell-slash-thin.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.notification_button.setIcon(icon1)
        self.notification_button.setCheckable(True)
        self.notification_button.setObjectName("notification_button")
        self.horizontalLayout_2.addWidget(self.notification_button)
        self.dropdown_notification_button = QtWidgets.QPushButton(
            parent=self.widget_5)
        self.dropdown_notification_button.setMinimumSize(QtCore.QSize(31, 31))
        self.dropdown_notification_button.setMaximumSize(QtCore.QSize(31, 31))
        self.dropdown_notification_button.setStyleSheet("background-color: rgb(18, 88, 83);\n"
                                                        "border-radius:15px;")
        self.dropdown_notification_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/Icons/angle-down-thin.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.dropdown_notification_button.setIcon(icon2)
        self.dropdown_notification_button.setCheckable(True)
        self.dropdown_notification_button.setObjectName(
            "dropdown_notification_button")
        self.horizontalLayout_2.addWidget(self.dropdown_notification_button)
        self.notifications_info_label = QtWidgets.QLabel(parent=self.widget_5)
        self.notifications_info_label.setMinimumSize(QtCore.QSize(0, 31))
        self.notifications_info_label.setMaximumSize(
            QtCore.QSize(16777215, 31))
        self.notifications_info_label.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.notifications_info_label.setStyleSheet(
            "background-color: rgb(18, 88, 83);")
        self.notifications_info_label.setTextFormat(
            QtCore.Qt.TextFormat.RichText)
        self.notifications_info_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.notifications_info_label.setIndent(0)
        self.notifications_info_label.setObjectName("notifications_info_label")
        self.horizontalLayout_2.addWidget(self.notifications_info_label)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addWidget(self.widget_5)
        spacerItem2 = QtWidgets.QSpacerItem(
            108, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.minimize_button = QtWidgets.QPushButton(parent=self.header_widget)
        self.minimize_button.setMinimumSize(QtCore.QSize(31, 31))
        self.minimize_button.setMaximumSize(QtCore.QSize(31, 31))
        self.minimize_button.setStyleSheet("background-color: rgb(18, 88, 83);\n"
                                           "border-radius:15px;")
        self.minimize_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/Icons/Minus.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.minimize_button.setIcon(icon3)
        self.minimize_button.setCheckable(True)
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_4.addWidget(self.minimize_button)
        self.maximize_button = QtWidgets.QPushButton(parent=self.header_widget)
        self.maximize_button.setMinimumSize(QtCore.QSize(31, 31))
        self.maximize_button.setMaximumSize(QtCore.QSize(31, 31))
        self.maximize_button.setStyleSheet("background-color: rgb(18, 88, 83);\n"
                                           "border-radius:15px;")
        self.maximize_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/Icons/maximize-2.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon4.addPixmap(QtGui.QPixmap(":/Icons/Icons/minimize-2.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.maximize_button.setIcon(icon4)
        self.maximize_button.setCheckable(True)
        self.maximize_button.setObjectName("maximize_button")
        self.horizontalLayout_4.addWidget(self.maximize_button)
        self.exit_button = QtWidgets.QPushButton(parent=self.header_widget)
        self.exit_button.setMinimumSize(QtCore.QSize(31, 31))
        self.exit_button.setMaximumSize(QtCore.QSize(31, 31))
        self.exit_button.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.exit_button.setStyleSheet("background-color: rgb(18, 88, 83);\n"
                                       "border-radius:15px;")
        self.exit_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/Icons/x.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exit_button.setIcon(icon5)
        self.exit_button.setCheckable(True)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_4.addWidget(self.exit_button)
        self.gridLayout.addWidget(self.header_widget, 0, 0, 1, 1)
        self.body_widget = QtWidgets.QHBoxLayout()
        self.body_widget.setSpacing(10)
        self.body_widget.setObjectName("body_widget")
        self.sidemenu_closed_widget = QtWidgets.QWidget(
            parent=self.main_widget)
        self.sidemenu_closed_widget.setMaximumSize(QtCore.QSize(81, 16777215))
        self.sidemenu_closed_widget.setStyleSheet(
            "background-color: transparent;")
        self.sidemenu_closed_widget.setObjectName("sidemenu_closed_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.sidemenu_closed_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(21, 10, 0, -1)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.account_button_closed_menu = QtWidgets.QPushButton(
            parent=self.sidemenu_closed_widget)
        self.account_button_closed_menu.setMinimumSize(QtCore.QSize(40, 40))
        self.account_button_closed_menu.setMaximumSize(QtCore.QSize(40, 40))
        self.account_button_closed_menu.setStyleSheet("QPushButton#account_button_closed_menu{\n"
                                                      "    background-color: rgb(18, 88, 83);\n"
                                                      "    border-radius:20px;\n"
                                                      "}\n"
                                                      "QPushButton#account_button_closed_menu:hover{\n"
                                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255));\n"
                                                      "}\n"
                                                      "QPushButton#account_button_closed_menu:pressed{\n"
                                                      "    background-color:rgba(18, 88, 83, 240)\n"
                                                      "}\n"
                                                      "QPushButton#account_button_closed_menu:checked { \n"
                                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255)); \n"
                                                      "}")
        self.account_button_closed_menu.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/Icons/circle-info-thin.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.account_button_closed_menu.setIcon(icon6)
        self.account_button_closed_menu.setCheckable(True)
        self.account_button_closed_menu.setAutoExclusive(True)
        self.account_button_closed_menu.setObjectName(
            "account_button_closed_menu")
        self.verticalLayout.addWidget(self.account_button_closed_menu)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 100, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.home_button_closed_menu = QtWidgets.QPushButton(
            parent=self.sidemenu_closed_widget)
        self.home_button_closed_menu.setMinimumSize(QtCore.QSize(40, 40))
        self.home_button_closed_menu.setMaximumSize(QtCore.QSize(40, 40))
        self.home_button_closed_menu.setStyleSheet("QPushButton#home_button_closed_menu{\n"
                                                   "    background-color: rgb(18, 88, 83);\n"
                                                   "    border-radius:20px;\n"
                                                   "}\n"
                                                   "QPushButton#home_button_closed_menu:hover{\n"
                                                   "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255));\n"
                                                   "}\n"
                                                   "QPushButton#home_button_closed_menu:pressed{\n"
                                                   "    background-color:rgba(18, 88, 83, 240)\n"
                                                   "}\n"
                                                   "QPushButton#home_button_closed_menu:checked { \n"
                                                   "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255)); \n"
                                                   "}")
        self.home_button_closed_menu.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Icons/Icons/house-thin.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.home_button_closed_menu.setIcon(icon7)
        self.home_button_closed_menu.setCheckable(True)
        self.home_button_closed_menu.setAutoExclusive(True)
        self.home_button_closed_menu.setObjectName("home_button_closed_menu")
        self.verticalLayout.addWidget(self.home_button_closed_menu)
        self.plants_button_closed_menu = QtWidgets.QPushButton(
            parent=self.sidemenu_closed_widget)
        self.plants_button_closed_menu.setMinimumSize(QtCore.QSize(40, 40))
        self.plants_button_closed_menu.setMaximumSize(QtCore.QSize(40, 40))
        self.plants_button_closed_menu.setStyleSheet("QPushButton#plants_button_closed_menu{\n"
                                                     "    background-color: rgb(18, 88, 83);\n"
                                                     "    border-radius:20px;\n"
                                                     "}\n"
                                                     "QPushButton#plants_button_closed_menu:hover{\n"
                                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255));\n"
                                                     "}\n"
                                                     "QPushButton#plants_button_closed_menu:pressed{\n"
                                                     "    background-color:rgba(18, 88, 83, 240)\n"
                                                     "}\n"
                                                     "QPushButton#plants_button_closed_menu:checked { \n"
                                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255)); \n"
                                                     "}")
        self.plants_button_closed_menu.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Icons/Icons/seedling-thin.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.plants_button_closed_menu.setIcon(icon8)
        self.plants_button_closed_menu.setCheckable(True)
        self.plants_button_closed_menu.setAutoExclusive(True)
        self.plants_button_closed_menu.setObjectName(
            "plants_button_closed_menu")
        self.verticalLayout.addWidget(self.plants_button_closed_menu)
        self.livefeed_button_closed_menu = QtWidgets.QPushButton(
            parent=self.sidemenu_closed_widget)
        self.livefeed_button_closed_menu.setMinimumSize(QtCore.QSize(40, 40))
        self.livefeed_button_closed_menu.setMaximumSize(QtCore.QSize(40, 40))
        self.livefeed_button_closed_menu.setStyleSheet("QPushButton#livefeed_button_closed_menu{\n"
                                                       "    background-color: rgb(18, 88, 83);\n"
                                                       "    border-radius:20px;\n"
                                                       "}\n"
                                                       "QPushButton#livefeed_button_closed_menu:hover{\n"
                                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255));\n"
                                                       "}\n"
                                                       "QPushButton#livefeed_button_closed_menu:pressed{\n"
                                                       "    background-color:rgba(18, 88, 83, 240)\n"
                                                       "}\n"
                                                       "QPushButton#livefeed_button_closed_menu:checked { \n"
                                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255)); \n"
                                                       "}")
        self.livefeed_button_closed_menu.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Icons/Icons/video-thin.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.livefeed_button_closed_menu.setIcon(icon9)
        self.livefeed_button_closed_menu.setCheckable(True)
        self.livefeed_button_closed_menu.setAutoExclusive(True)
        self.livefeed_button_closed_menu.setObjectName(
            "livefeed_button_closed_menu")
        self.verticalLayout.addWidget(self.livefeed_button_closed_menu)
        self.analytics_button_closed_menu = QtWidgets.QPushButton(
            parent=self.sidemenu_closed_widget)
        self.analytics_button_closed_menu.setMinimumSize(QtCore.QSize(40, 40))
        self.analytics_button_closed_menu.setMaximumSize(QtCore.QSize(40, 40))
        self.analytics_button_closed_menu.setStyleSheet("QPushButton#analytics_button_closed_menu{\n"
                                                        "    background-color: rgb(18, 88, 83);\n"
                                                        "    border-radius:20px;\n"
                                                        "}\n"
                                                        "QPushButton#analytics_button_closed_menu:hover{\n"
                                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255));\n"
                                                        "}\n"
                                                        "QPushButton#analytics_button_closed_menu:pressed{\n"
                                                        "    background-color:rgba(18, 88, 83, 240)\n"
                                                        "}\n"
                                                        "QPushButton#analytics_button_closed_menu:checked { \n"
                                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255)); \n"
                                                        "}")
        self.analytics_button_closed_menu.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Icons/Icons/chart-simple-thin.svg"),
                         QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.analytics_button_closed_menu.setIcon(icon10)
        self.analytics_button_closed_menu.setCheckable(True)
        self.analytics_button_closed_menu.setAutoExclusive(True)
        self.analytics_button_closed_menu.setObjectName(
            "analytics_button_closed_menu")
        self.verticalLayout.addWidget(self.analytics_button_closed_menu)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 120, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.logout_button_closed_menu = QtWidgets.QPushButton(
            parent=self.sidemenu_closed_widget)
        self.logout_button_closed_menu.setMinimumSize(QtCore.QSize(40, 40))
        self.logout_button_closed_menu.setMaximumSize(QtCore.QSize(40, 40))
        self.logout_button_closed_menu.setStyleSheet("QPushButton#logout_button_closed_menu{\n"
                                                     "    background-color: rgb(18, 88, 83);\n"
                                                     "    border-radius:20px;\n"
                                                     "}\n"
                                                     "QPushButton#logout_button_closed_menu:hover{\n"
                                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255));\n"
                                                     "}\n"
                                                     "QPushButton#logout_button_closed_menu:pressed{\n"
                                                     "    background-color:rgba(18, 88, 83, 240)\n"
                                                     "}\n"
                                                     "QPushButton#logout_button_closed_menu:checked { \n"
                                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255)); \n"
                                                     "}")
        self.logout_button_closed_menu.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Icons/Icons/arrow-right-from-bracket-thin.svg"),
                         QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.logout_button_closed_menu.setIcon(icon11)
        self.logout_button_closed_menu.setCheckable(True)
        self.logout_button_closed_menu.setAutoExclusive(True)
        self.logout_button_closed_menu.setObjectName(
            "logout_button_closed_menu")
        self.verticalLayout.addWidget(self.logout_button_closed_menu)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.body_widget.addWidget(self.sidemenu_closed_widget)
        self.sidemenu_opened_widget = QtWidgets.QWidget(
            parent=self.main_widget)
        self.sidemenu_opened_widget.setMinimumSize(QtCore.QSize(150, 0))
        self.sidemenu_opened_widget.setMaximumSize(QtCore.QSize(130, 16777215))
        self.sidemenu_opened_widget.setStyleSheet(
            "background-color: transparent;")
        self.sidemenu_opened_widget.setObjectName("sidemenu_opened_widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.sidemenu_opened_widget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(3)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(21, 10, 0, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.account_button_opened_menu = QtWidgets.QPushButton(
            parent=self.sidemenu_opened_widget)
        self.account_button_opened_menu.setMinimumSize(QtCore.QSize(100, 40))
        self.account_button_opened_menu.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.account_button_opened_menu.setFont(font)
        self.account_button_opened_menu.setContextMenuPolicy(
            QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.account_button_opened_menu.setStyleSheet("QPushButton#account_button_opened_menu{\n"
                                                      "    background-color: rgb(18, 88, 83);\n"
                                                      "    border-radius:15px;\n"
                                                      "}\n"
                                                      "QPushButton#account_button_opened_menu:hover{\n"
                                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255));\n"
                                                      "}\n"
                                                      "QPushButton#account_button_opened_menu:pressed{\n"
                                                      "    background-color:rgba(18, 88, 83, 240)\n"
                                                      "}\n"
                                                      "QPushButton#account_button_opened_menu:checked { \n"
                                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255)); \n"
                                                      "}")
        self.account_button_opened_menu.setIcon(icon6)
        self.account_button_opened_menu.setCheckable(True)
        self.account_button_opened_menu.setAutoExclusive(True)
        self.account_button_opened_menu.setObjectName(
            "account_button_opened_menu")
        self.gridLayout_3.addWidget(
            self.account_button_opened_menu, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 100, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plants_button_opened_menu = QtWidgets.QPushButton(
            parent=self.sidemenu_opened_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.plants_button_opened_menu.sizePolicy().hasHeightForWidth())
        self.plants_button_opened_menu.setSizePolicy(sizePolicy)
        self.plants_button_opened_menu.setMinimumSize(QtCore.QSize(100, 40))
        self.plants_button_opened_menu.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.plants_button_opened_menu.setFont(font)
        self.plants_button_opened_menu.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.plants_button_opened_menu.setStyleSheet("QPushButton#plants_button_opened_menu{\n"
                                                     "    background-color: rgb(18, 88, 83);\n"
                                                     "    border-radius:15px;\n"
                                                     "}\n"
                                                     "QPushButton#plants_button_opened_menu:hover{\n"
                                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255));\n"
                                                     "}\n"
                                                     "QPushButton#plants_button_opened_menu:pressed{\n"
                                                     "    background-color:rgba(18, 88, 83, 240)\n"
                                                     "}\n"
                                                     "QPushButton#plants_button_opened_menu:checked { \n"
                                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255)); \n"
                                                     "}")
        self.plants_button_opened_menu.setIcon(icon8)
        self.plants_button_opened_menu.setCheckable(True)
        self.plants_button_opened_menu.setAutoExclusive(True)
        self.plants_button_opened_menu.setObjectName(
            "plants_button_opened_menu")
        self.gridLayout_4.addWidget(self.plants_button_opened_menu, 1, 0, 1, 1)
        self.home_button_opened_menu = QtWidgets.QPushButton(
            parent=self.sidemenu_opened_widget)
        self.home_button_opened_menu.setMinimumSize(QtCore.QSize(100, 40))
        self.home_button_opened_menu.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.home_button_opened_menu.setFont(font)
        self.home_button_opened_menu.setStyleSheet("QPushButton#home_button_opened_menu{\n"
                                                   "    background-color: rgb(18, 88, 83);\n"
                                                   "    border-radius:15px;\n"
                                                   "}\n"
                                                   "QPushButton#home_button_opened_menu:hover{\n"
                                                   "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255));\n"
                                                   "}\n"
                                                   "QPushButton#home_button_opened_menu:pressed{\n"
                                                   "    background-color:rgba(18, 88, 83, 240)\n"
                                                   "}\n"
                                                   "QPushButton#home_button_opened_menu:checked { \n"
                                                   "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255)); \n"
                                                   "}")
        self.home_button_opened_menu.setIcon(icon7)
        self.home_button_opened_menu.setCheckable(True)
        self.home_button_opened_menu.setAutoExclusive(True)
        self.home_button_opened_menu.setObjectName("home_button_opened_menu")
        self.gridLayout_4.addWidget(self.home_button_opened_menu, 0, 0, 1, 1)
        self.analytics_button_opened_menu = QtWidgets.QPushButton(
            parent=self.sidemenu_opened_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.analytics_button_opened_menu.sizePolicy().hasHeightForWidth())
        self.analytics_button_opened_menu.setSizePolicy(sizePolicy)
        self.analytics_button_opened_menu.setMinimumSize(QtCore.QSize(100, 40))
        self.analytics_button_opened_menu.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.analytics_button_opened_menu.setFont(font)
        self.analytics_button_opened_menu.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.analytics_button_opened_menu.setStyleSheet("QPushButton#analytics_button_opened_menu{\n"
                                                        "    background-color: rgb(18, 88, 83);\n"
                                                        "    border-radius:15px;\n"
                                                        "}\n"
                                                        "QPushButton#analytics_button_opened_menu:hover{\n"
                                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255));\n"
                                                        "}\n"
                                                        "QPushButton#analytics_button_opened_menu:pressed{\n"
                                                        "    background-color:rgba(18, 88, 83, 240)\n"
                                                        "}\n"
                                                        "QPushButton#analytics_button_opened_menu:checked { \n"
                                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255)); \n"
                                                        "}")
        self.analytics_button_opened_menu.setIcon(icon10)
        self.analytics_button_opened_menu.setCheckable(True)
        self.analytics_button_opened_menu.setAutoExclusive(True)
        self.analytics_button_opened_menu.setObjectName(
            "analytics_button_opened_menu")
        self.gridLayout_4.addWidget(
            self.analytics_button_opened_menu, 3, 0, 1, 1)
        self.livefeed_button_opened_menu = QtWidgets.QPushButton(
            parent=self.sidemenu_opened_widget)
        self.livefeed_button_opened_menu.setMinimumSize(QtCore.QSize(100, 40))
        self.livefeed_button_opened_menu.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.livefeed_button_opened_menu.setFont(font)
        self.livefeed_button_opened_menu.setStyleSheet("QPushButton#livefeed_button_opened_menu{\n"
                                                       "    background-color: rgb(18, 88, 83);\n"
                                                       "    border-radius:15px;\n"
                                                       "}\n"
                                                       "QPushButton#livefeed_button_opened_menu:hover{\n"
                                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255));\n"
                                                       "}\n"
                                                       "QPushButton#livefeed_button_opened_menu:pressed{\n"
                                                       "    background-color:rgba(18, 88, 83, 240)\n"
                                                       "}\n"
                                                       "QPushButton#livefeed_button_opened_menu:checked { \n"
                                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255)); \n"
                                                       "}")
        self.livefeed_button_opened_menu.setIcon(icon9)
        self.livefeed_button_opened_menu.setCheckable(True)
        self.livefeed_button_opened_menu.setAutoExclusive(True)
        self.livefeed_button_opened_menu.setAutoDefault(False)
        self.livefeed_button_opened_menu.setObjectName(
            "livefeed_button_opened_menu")
        self.gridLayout_4.addWidget(
            self.livefeed_button_opened_menu, 2, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 120, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem6)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.logout_button_opened_menu = QtWidgets.QPushButton(
            parent=self.sidemenu_opened_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.logout_button_opened_menu.sizePolicy().hasHeightForWidth())
        self.logout_button_opened_menu.setSizePolicy(sizePolicy)
        self.logout_button_opened_menu.setMinimumSize(QtCore.QSize(100, 40))
        self.logout_button_opened_menu.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.logout_button_opened_menu.setFont(font)
        self.logout_button_opened_menu.setStyleSheet("QPushButton#logout_button_opened_menu{\n"
                                                     "    background-color: rgb(18, 88, 83);\n"
                                                     "    border-radius:15px;\n"
                                                     "}\n"
                                                     "QPushButton#logout_button_opened_menu:hover{\n"
                                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255));\n"
                                                     "}\n"
                                                     "QPushButton#logout_button_opened_menu:pressed{\n"
                                                     "    background-color:rgba(18, 88, 83, 240)\n"
                                                     "}\n"
                                                     "QPushButton#logout_button_opened_menu:checked { \n"
                                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(18, 88, 83, 255), stop:1 rgba(6, 125, 97, 255)); \n"
                                                     "}")
        self.logout_button_opened_menu.setIcon(icon11)
        self.logout_button_opened_menu.setCheckable(True)
        self.logout_button_opened_menu.setAutoExclusive(True)
        self.logout_button_opened_menu.setObjectName(
            "logout_button_opened_menu")
        self.gridLayout_5.addWidget(self.logout_button_opened_menu, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.body_widget.addWidget(self.sidemenu_opened_widget)
        self.open_menu_button = QtWidgets.QPushButton(parent=self.main_widget)
        self.open_menu_button.setMinimumSize(QtCore.QSize(30, 30))
        self.open_menu_button.setMaximumSize(QtCore.QSize(30, 30))
        self.open_menu_button.setStyleSheet("background-color: rgb(18, 88, 83);\n"
                                            "border-radius:15;\n"
                                            "\n"
                                            "")
        self.open_menu_button.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Icons/Icons/chevron-right.svg"),
                         QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon12.addPixmap(QtGui.QPixmap(":/Icons/Icons/chevron-left.svg"),
                         QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.open_menu_button.setIcon(icon12)
        self.open_menu_button.setCheckable(True)
        self.open_menu_button.setObjectName("open_menu_button")
        self.body_widget.addWidget(self.open_menu_button)
        self.content_stacked_widget = QtWidgets.QStackedWidget(
            parent=self.main_widget)
        self.content_stacked_widget.setStyleSheet("background-color: rgb(13, 37, 34);\n"
                                                  "border-top-left-radius:50px;\n"
                                                  "border-bottom-left-radius:50px;")
        self.content_stacked_widget.setObjectName("content_stacked_widget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.home_page_label = QtWidgets.QLabel(parent=self.Home)
        self.home_page_label.setGeometry(QtCore.QRect(380, 210, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        self.home_page_label.setFont(font)
        self.home_page_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.home_page_label.setObjectName("home_page_label")
        self.content_stacked_widget.addWidget(self.Home)
        self.Plants = QtWidgets.QWidget()
        self.Plants.setObjectName("Plants")
        self.content_stacked_widget.addWidget(self.Plants)
        self.Livefeed = QtWidgets.QWidget()
        self.Livefeed.setObjectName("Livefeed")
        self.livefeed_page_label = QtWidgets.QLabel(parent=self.Livefeed)
        self.livefeed_page_label.setGeometry(QtCore.QRect(370, 210, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        self.livefeed_page_label.setFont(font)
        self.livefeed_page_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.livefeed_page_label.setObjectName("livefeed_page_label")
        self.content_stacked_widget.addWidget(self.Livefeed)
        self.Analytics = QtWidgets.QWidget()
        self.Analytics.setObjectName("Analytics")
        self.analytics_page_label = QtWidgets.QLabel(parent=self.Analytics)
        self.analytics_page_label.setGeometry(QtCore.QRect(360, 210, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        self.analytics_page_label.setFont(font)
        self.analytics_page_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.analytics_page_label.setObjectName("analytics_page_label")
        self.content_stacked_widget.addWidget(self.Analytics)
        self.Account = QtWidgets.QWidget()
        self.Account.setObjectName("Account")
        account_layout = QtWidgets.QVBoxLayout(self.Account)
        account_layout.setContentsMargins(0, 0, 0, 0)
        account_layout.setSpacing(0)
        self.account_placeholder = QtWidgets.QWidget()
        account_layout.addWidget(self.account_placeholder)
        self.content_stacked_widget.addWidget(self.Account)
        self.body_widget.addWidget(self.content_stacked_widget)
        self.gridLayout.addLayout(self.body_widget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)
        self.content_stacked_widget.setCurrentIndex(1)
        self.exit_button.clicked.connect(MainWindow.close)
        self.maximize_button.clicked['bool'].connect(MainWindow.showMaximized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.log_reg_py_text_label.setText(_translate("MainWindow", "PY"))
        self.log_reg_flora_text_label.setText(
            _translate("MainWindow", "FLORA"))
        self.notifications_info_label.setText(
            _translate("MainWindow", "New notfications!"))
        self.account_button_opened_menu.setText(
            _translate("MainWindow", "Account"))
        self.plants_button_opened_menu.setText(
            _translate("MainWindow", "Plants"))
        self.home_button_opened_menu.setText(_translate("MainWindow", "Home"))
        self.analytics_button_opened_menu.setText(
            _translate("MainWindow", "Analytics"))
        self.livefeed_button_opened_menu.setText(
            _translate("MainWindow", "Livefeed"))
        self.logout_button_opened_menu.setText(
            _translate("MainWindow", "Log-out"))
        self.home_page_label.setText(_translate("MainWindow", "HOME"))
        self.livefeed_page_label.setText(_translate("MainWindow", "LIVEFEED"))
        self.analytics_page_label.setText(
            _translate("MainWindow", "ANALYTICS"))

        # Remove the automatic menu toggle connections
        # self.open_menu_button.toggled['bool'].connect(self.sidemenu_closed_widget.setVisible)
        # self.open_menu_button.toggled['bool'].connect(self.sidemenu_opened_widget.setHidden)

        # Keep other necessary connections
        self.account_button_closed_menu.toggled['bool'].connect(
            self.account_button_opened_menu.setChecked)
        self.account_button_opened_menu.toggled['bool'].connect(
            self.account_button_closed_menu.setChecked)
        self.home_button_closed_menu.toggled['bool'].connect(
            self.home_button_opened_menu.setChecked)
        self.home_button_opened_menu.toggled['bool'].connect(
            self.home_button_closed_menu.setChecked)
        self.plants_button_closed_menu.toggled['bool'].connect(
            self.plants_button_opened_menu.setChecked)
        self.plants_button_opened_menu.toggled['bool'].connect(
            self.plants_button_closed_menu.setChecked)
        self.livefeed_button_closed_menu.toggled['bool'].connect(
            self.livefeed_button_opened_menu.setChecked)
        self.livefeed_button_opened_menu.toggled['bool'].connect(
            self.livefeed_button_closed_menu.setChecked)
        self.analytics_button_closed_menu.toggled['bool'].connect(
            self.analytics_button_opened_menu.setChecked)
        self.analytics_button_opened_menu.toggled['bool'].connect(
            self.analytics_button_closed_menu.setChecked)
        self.logout_button_closed_menu.toggled['bool'].connect(
            self.logout_button_opened_menu.setChecked)
        self.logout_button_opened_menu.toggled['bool'].connect(
            self.logout_button_closed_menu.setChecked)
        self.exit_button.clicked.connect(MainWindow.close)
        self.maximize_button.clicked['bool'].connect(MainWindow.showMaximized)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
