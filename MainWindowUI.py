# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res


class Ui_MainWindow(object):
    def setup_main_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 423)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu_container = QtWidgets.QFrame(self.centralwidget)
        self.side_menu_container.setMaximumSize(QtCore.QSize(200, 16777215))
        self.side_menu_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_container.setObjectName("side_menu_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.slide_menu = QtWidgets.QFrame(self.side_menu_container)
        self.slide_menu.setMinimumSize(QtCore.QSize(198, 0))
        self.slide_menu.setStyleSheet("background-image: url(:/images/images/flora_bg.png);\n"
                                      "border-top-left-radius:20px;\n"
                                      "border-bottom-left-radius:20px;")
        self.slide_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_menu.setObjectName("slide_menu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.slide_menu)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.side_menu_header = QtWidgets.QFrame(self.slide_menu)
        self.side_menu_header.setStyleSheet("background: transparent;")
        self.side_menu_header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.side_menu_header.setFrameShadow(QtWidgets.QFrame.Plain)
        self.side_menu_header.setLineWidth(0)
        self.side_menu_header.setObjectName("side_menu_header")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.side_menu_header)
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.app_name_label = QtWidgets.QLabel(self.side_menu_header)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(16)
        self.app_name_label.setFont(font)
        self.app_name_label.setStyleSheet("background: transparent;")
        self.app_name_label.setObjectName("app_name_label")
        self.verticalLayout_5.addWidget(self.app_name_label)
        self.verticalLayout_4.addWidget(self.side_menu_header, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.account_info_frame = QtWidgets.QFrame(self.slide_menu)
        self.account_info_frame.setAutoFillBackground(False)
        self.account_info_frame.setStyleSheet("\n"
                                              "background: transparent;")
        self.account_info_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.account_info_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.account_info_frame.setObjectName("account_info_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.account_info_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.profile_picture_placeholder = QtWidgets.QLabel(self.account_info_frame)
        self.profile_picture_placeholder.setAutoFillBackground(False)
        self.profile_picture_placeholder.setStyleSheet("border-radius:10px;\n"
                                                       "background: transparent;")
        self.profile_picture_placeholder.setText("")
        self.profile_picture_placeholder.setPixmap(QtGui.QPixmap(":/icons/icons/user.svg"))
        self.profile_picture_placeholder.setObjectName("profile_picture_placeholder")
        self.verticalLayout_7.addWidget(self.profile_picture_placeholder, 0,
                                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.sidemenu_username_placeholder = QtWidgets.QLabel(self.account_info_frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.sidemenu_username_placeholder.setFont(font)
        self.sidemenu_username_placeholder.setObjectName("sidemenu_username_placeholder")
        self.verticalLayout_7.addWidget(self.sidemenu_username_placeholder, 0,
                                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addWidget(self.account_info_frame, 0, QtCore.Qt.AlignTop)
        self.side_menu_body = QtWidgets.QFrame(self.slide_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_menu_body.sizePolicy().hasHeightForWidth())
        self.side_menu_body.setSizePolicy(sizePolicy)
        self.side_menu_body.setStyleSheet("background: transparent;\n"
                                          "")
        self.side_menu_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_body.setObjectName("side_menu_body")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.side_menu_body)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sidemenu_toolbox = QtWidgets.QToolBox(self.side_menu_body)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        self.sidemenu_toolbox.setFont(font)
        self.sidemenu_toolbox.setStyleSheet("background:transparent;\n"
                                            "border:none;")
        self.sidemenu_toolbox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sidemenu_toolbox.setObjectName("sidemenu_toolbox")
        self.dashboard_drop_bttn = QtWidgets.QWidget()
        self.dashboard_drop_bttn.setGeometry(QtCore.QRect(0, 0, 162, 181))
        self.dashboard_drop_bttn.setStyleSheet("")
        self.dashboard_drop_bttn.setObjectName("dashboard_drop_bttn")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.dashboard_drop_bttn)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_2 = QtWidgets.QFrame(self.dashboard_drop_bttn)
        self.frame_2.setStyleSheet("background:transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.sidemenu_livefeed_bttn = QtWidgets.QPushButton(self.frame_2)
        self.sidemenu_livefeed_bttn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sidemenu_livefeed_bttn.setStyleSheet("QPushButton#sidemenu_livefeed_bttn{\n"
                                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(100, 160, 160, 219), stop:1 rgba(167, 167, 255, 226));\n"
                                                  "    color:rgba(255,255,255,210);\n"
                                                  "    border-radius:10px;\n"
                                                  "}\n"
                                                  "QPushButton#sidemenu_livefeed_bttn:hover{\n"
                                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(100, 160, 160, 255), stop:1 rgba(167, 167, 255, 255));\n"
                                                  "}\n"
                                                  "QPushButton#sidemenu_livefeed_bttn:pressed{\n"
                                                  "    padding-left:5px;\n"
                                                  "    padding-top:5px;\n"
                                                  "    background-color:rgba(120, 120, 255, 240)\n"
                                                  "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/video.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sidemenu_livefeed_bttn.setIcon(icon)
        self.sidemenu_livefeed_bttn.setObjectName("sidemenu_livefeed_bttn")
        self.verticalLayout_9.addWidget(self.sidemenu_livefeed_bttn)
        self.sidemenu_plants_bttn = QtWidgets.QPushButton(self.frame_2)
        self.sidemenu_plants_bttn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sidemenu_plants_bttn.setStyleSheet("QPushButton#sidemenu_plants_bttn{\n"
                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(100, 160, 160, 219), stop:1 rgba(167, 167, 255, 226));\n"
                                                "    color:rgba(255,255,255,210);\n"
                                                "    border-radius:10px;\n"
                                                "}\n"
                                                "QPushButton#sidemenu_plants_bttn:hover{\n"
                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(100, 160, 160, 255), stop:1 rgba(167, 167, 255, 255));\n"
                                                "}\n"
                                                "QPushButton#sidemenu_plants_bttn:pressed{\n"
                                                "    padding-left:5px;\n"
                                                "    padding-top:5px;\n"
                                                "    background-color:rgba(120, 120, 255, 240)\n"
                                                "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/activity.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sidemenu_plants_bttn.setIcon(icon1)
        self.sidemenu_plants_bttn.setObjectName("sidemenu_plants_bttn")
        self.verticalLayout_9.addWidget(self.sidemenu_plants_bttn)
        self.sidemenu_analytics_bttn = QtWidgets.QPushButton(self.frame_2)
        self.sidemenu_analytics_bttn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sidemenu_analytics_bttn.setStyleSheet("QPushButton#sidemenu_analytics_bttn{\n"
                                                   "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(100, 160, 160, 219), stop:1 rgba(167, 167, 255, 226));\n"
                                                   "    color:rgba(255,255,255,210);\n"
                                                   "    border-radius:10px;\n"
                                                   "}\n"
                                                   "QPushButton#sidemenu_analytics_bttn:hover{\n"
                                                   "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(100, 160, 160, 255), stop:1 rgba(167, 167, 255, 255));\n"
                                                   "}\n"
                                                   "QPushButton#sidemenu_analytics_bttn:pressed{\n"
                                                   "    padding-left:5px;\n"
                                                   "    padding-top:5px;\n"
                                                   "    background-color:rgba(120, 120, 255, 240)\n"
                                                   "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/bar-chart-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sidemenu_analytics_bttn.setIcon(icon2)
        self.sidemenu_analytics_bttn.setObjectName("sidemenu_analytics_bttn")
        self.verticalLayout_9.addWidget(self.sidemenu_analytics_bttn)
        self.verticalLayout_8.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sidemenu_toolbox.addItem(self.dashboard_drop_bttn, icon3, "")
        self.account_drop_bttn = QtWidgets.QWidget()
        self.account_drop_bttn.setGeometry(QtCore.QRect(0, 0, 162, 181))
        self.account_drop_bttn.setObjectName("account_drop_bttn")
        self.sidemenu_toolbox.addItem(self.account_drop_bttn, icon3, "")
        self.verticalLayout_6.addWidget(self.sidemenu_toolbox)
        self.verticalLayout_4.addWidget(self.side_menu_body)
        self.side_menu_footer = QtWidgets.QFrame(self.slide_menu)
        self.side_menu_footer.setStyleSheet("background: transparent;")
        self.side_menu_footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_footer.setObjectName("side_menu_footer")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.side_menu_footer)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.log_out_bttn = QtWidgets.QPushButton(self.side_menu_footer)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.log_out_bttn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.log_out_bttn.setIcon(icon4)
        self.log_out_bttn.setCheckable(True)
        self.log_out_bttn.setObjectName("log_out_bttn")
        self.horizontalLayout_9.addWidget(self.log_out_bttn)
        self.log_out_bttn.setStyleSheet("QPushButton#log_out_bttn{\n"
                                        "    background-color: rgba(0,0,0,0);\n"
                                        "    color:rgba(0, 160, 160, 219);\n"
                                        "    border-radius:10px;\n"
                                        "}\n"
                                        "QPushButton#log_out_bttn:hover{\n"
                                        "    color: rgba(100, 160, 160, 255);\n"
                                        "}\n"
                                        "QPushButton#log_out_bttn:pressed{\n"
                                        "    padding-left:5px;\n"
                                        "    padding-top:5px;\n"
                                        "    color:rgba(120, 120, 255, 240)\n"
                                        "}")
        self.theme_changer_bttn_off = QtWidgets.QPushButton(self.side_menu_footer)
        self.theme_changer_bttn_off.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/toggle-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.theme_changer_bttn_off.setIcon(icon5)
        self.theme_changer_bttn_off.setObjectName("theme_changer_bttn_off")
        self.horizontalLayout_9.addWidget(self.theme_changer_bttn_off, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_4.addWidget(self.side_menu_footer, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.slide_menu)
        self.horizontalLayout.addWidget(self.side_menu_container)
        self.main_body_container = QtWidgets.QFrame(self.centralwidget)
        self.main_body_container.setStyleSheet("background-color: rgb(113, 113, 113);")
        self.main_body_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_container.setObjectName("main_body_container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_body_container)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_frame = QtWidgets.QFrame(self.main_body_container)
        self.header_frame.setStyleSheet("background-color:rgba(35, 93, 113, 255);\n"
                                        "")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.side_menu_controls = QtWidgets.QFrame(self.header_frame)
        self.side_menu_controls.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu_controls.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_controls.setObjectName("side_menu_controls")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.side_menu_controls)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.minimize_menu_bttn = QtWidgets.QPushButton(self.side_menu_controls)
        self.minimize_menu_bttn.setStyleSheet("border:none;")
        self.minimize_menu_bttn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/align-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_menu_bttn.setIcon(icon6)
        self.minimize_menu_bttn.setIconSize(QtCore.QSize(16, 16))
        self.minimize_menu_bttn.setObjectName("minimize_menu_bttn")
        self.horizontalLayout_8.addWidget(self.minimize_menu_bttn, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.side_menu_controls, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.search_frame = QtWidgets.QFrame(self.header_frame)
        self.search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_frame.setObjectName("search_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.search_frame)
        self.horizontalLayout_6.setContentsMargins(30, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.search_box = QtWidgets.QLineEdit(self.search_frame)
        self.search_box.setMinimumSize(QtCore.QSize(133, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.search_box.setFont(font)
        self.search_box.setObjectName("search_box")
        self.horizontalLayout_6.addWidget(self.search_box, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.search_bttn = QtWidgets.QPushButton(self.search_frame)
        self.search_bttn.setStyleSheet("border:none;")
        self.search_bttn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_bttn.setIcon(icon7)
        self.search_bttn.setObjectName("search_bttn")
        self.horizontalLayout_6.addWidget(self.search_bttn, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.help_bttn = QtWidgets.QPushButton(self.search_frame)
        self.help_bttn.setStyleSheet("border:none;")
        self.help_bttn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_bttn.setIcon(icon8)
        self.help_bttn.setObjectName("help_bttn")
        self.horizontalLayout_6.addWidget(self.help_bttn)
        self.horizontalLayout_2.addWidget(self.search_frame, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.notifications_frame = QtWidgets.QFrame(self.header_frame)
        self.notifications_frame.setMinimumSize(QtCore.QSize(100, 0))
        self.notifications_frame.setMaximumSize(QtCore.QSize(152, 16777215))
        self.notifications_frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.notifications_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.notifications_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notifications_frame.setObjectName("notifications_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.notifications_frame)
        self.horizontalLayout_5.setContentsMargins(30, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.new_notification_text = QtWidgets.QLabel(self.notifications_frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setBold(False)
        font.setWeight(50)
        self.new_notification_text.setFont(font)
        self.new_notification_text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.new_notification_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.new_notification_text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.new_notification_text.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextEditable | QtCore.Qt.TextSelectableByMouse)
        self.new_notification_text.setObjectName("new_notification_text")
        self.horizontalLayout_5.addWidget(self.new_notification_text, 0, QtCore.Qt.AlignVCenter)
        self.notification_bttn = QtWidgets.QPushButton(self.notifications_frame)
        self.notification_bttn.setStyleSheet("border:none;")
        self.notification_bttn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notification_bttn.setIcon(icon9)
        self.notification_bttn.setObjectName("notification_bttn")
        self.horizontalLayout_5.addWidget(self.notification_bttn)
        self.notifications_bttn = QtWidgets.QPushButton(self.notifications_frame)
        self.notifications_bttn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.notifications_bttn.setStyleSheet("border:none;")
        self.notifications_bttn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/bell.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notifications_bttn.setIcon(icon10)
        self.notifications_bttn.setObjectName("notifications_bttn")
        self.horizontalLayout_5.addWidget(self.notifications_bttn, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.notifications_frame)
        self.app_controls_frame = QtWidgets.QFrame(self.header_frame)
        self.app_controls_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.app_controls_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.app_controls_frame.setObjectName("app_controls_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.app_controls_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.minimize_bttn = QtWidgets.QPushButton(self.app_controls_frame)
        self.minimize_bttn.setStyleSheet("border:none;")
        self.minimize_bttn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/minimize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_bttn.setIcon(icon11)
        self.minimize_bttn.setObjectName("minimize_bttn")
        self.horizontalLayout_4.addWidget(self.minimize_bttn, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.maximize_bttn = QtWidgets.QPushButton(self.app_controls_frame)
        self.maximize_bttn.setStyleSheet("border:none;")
        self.maximize_bttn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/maximize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximize_bttn.setIcon(icon12)
        self.maximize_bttn.setObjectName("maximize_bttn")
        self.horizontalLayout_4.addWidget(self.maximize_bttn, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.exit_bttn_mw = QtWidgets.QPushButton(self.app_controls_frame)
        self.exit_bttn_mw.setStyleSheet("border:none;")
        self.exit_bttn_mw.setText("")
        self.exit_bttn_mw.setCheckable(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_bttn_mw.setIcon(icon13)
        self.exit_bttn_mw.setObjectName("exit_bttn_mw")
        self.exit_bttn_mw.setStyleSheet("QPushButton#exit_bttn_mw{\n"
                                        "    background-color: rgba(0,0,0,0);\n"
                                        "    color:rgba(0, 160, 160, 219);\n"
                                        "    border-radius:10px;\n"
                                        "}\n"
                                        "QPushButton#exit_bttn_mw:hover{\n"
                                        "    color: rgba(100, 160, 160, 255);\n"
                                        "}\n"
                                        "QPushButton#exit_bttn_mw:pressed{\n"
                                        "    padding-left:5px;\n"
                                        "    padding-top:5px;\n"
                                        "    color:rgba(120, 120, 255, 240)\n"
                                        "}")
        self.horizontalLayout_4.addWidget(self.exit_bttn_mw, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.app_controls_frame, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.header_frame, 0, QtCore.Qt.AlignVCenter)
        self.main_body_frame = QtWidgets.QFrame(self.main_body_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.main_body_frame.setFont(font)
        self.main_body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_frame.setObjectName("main_body_frame")
        self.verticalLayout.addWidget(self.main_body_frame)
        self.footer_frame = QtWidgets.QFrame(self.main_body_container)
        self.footer_frame.setStyleSheet("border-top:1px solid gray;")
        self.footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.info_text_frame = QtWidgets.QFrame(self.footer_frame)
        self.info_text_frame.setStyleSheet("border:none;")
        self.info_text_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_text_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_text_frame.setObjectName("info_text_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.info_text_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.info_text = QtWidgets.QLabel(self.info_text_frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        self.info_text.setFont(font)
        self.info_text.setStyleSheet("border:none;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "color: rgb(167, 167, 167);")
        self.info_text.setObjectName("info_text")
        self.verticalLayout_3.addWidget(self.info_text, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_3.addWidget(self.info_text_frame, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.socials_frame = QtWidgets.QFrame(self.footer_frame)
        self.socials_frame.setStyleSheet("border-top:none;\n"
                                         "border-left:1px solid gray;\n"
                                         "border-right:1px solid gray;")
        self.socials_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.socials_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.socials_frame.setObjectName("socials_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.socials_frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.algebra_web_bttn = QtWidgets.QPushButton(self.socials_frame)
        self.algebra_web_bttn.setStyleSheet("border:none;")
        self.algebra_web_bttn.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/icons/codesandbox.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.algebra_web_bttn.setIcon(icon14)
        self.algebra_web_bttn.setObjectName("algebra_web_bttn")
        self.horizontalLayout_7.addWidget(self.algebra_web_bttn)
        self.email_web_bttn = QtWidgets.QPushButton(self.socials_frame)
        self.email_web_bttn.setStyleSheet("border:none;")
        self.email_web_bttn.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/icons/mail.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.email_web_bttn.setIcon(icon15)
        self.email_web_bttn.setObjectName("email_web_bttn")
        self.horizontalLayout_7.addWidget(self.email_web_bttn)
        self.github_web_bttn = QtWidgets.QPushButton(self.socials_frame)
        self.github_web_bttn.setStyleSheet("border:none;\n"
                                           "background-color: rgb(124, 124, 124);")
        self.github_web_bttn.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/icons/github.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.github_web_bttn.setIcon(icon16)
        self.github_web_bttn.setObjectName("github_web_bttn")
        self.horizontalLayout_7.addWidget(self.github_web_bttn)
        self.horizontalLayout_3.addWidget(self.socials_frame)
        self.size_grip = QtWidgets.QFrame(self.footer_frame)
        self.size_grip.setMinimumSize(QtCore.QSize(10, 10))
        self.size_grip.setMaximumSize(QtCore.QSize(10, 10))
        self.size_grip.setStyleSheet("border:none;")
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.horizontalLayout_3.addWidget(self.size_grip, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.footer_frame, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.main_body_container)

        self.retranslateUi(MainWindow)
        self.sidemenu_toolbox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.app_name_label.setText(_translate("MainWindow", "PY|Flora"))
        self.sidemenu_username_placeholder.setText(_translate("MainWindow", "Username"))
        self.sidemenu_livefeed_bttn.setText(_translate("MainWindow", "Livefeed"))
        self.sidemenu_plants_bttn.setText(_translate("MainWindow", "Plants"))
        self.sidemenu_analytics_bttn.setText(_translate("MainWindow", "Analytics"))
        self.sidemenu_toolbox.setItemText(self.sidemenu_toolbox.indexOf(self.dashboard_drop_bttn),
                                          _translate("MainWindow", "Dashboard"))
        self.sidemenu_toolbox.setItemText(self.sidemenu_toolbox.indexOf(self.account_drop_bttn),
                                          _translate("MainWindow", "Account"))
        self.log_out_bttn.setText(_translate("MainWindow", "Log-out"))
        self.search_box.setPlaceholderText(_translate("MainWindow", "Search"))
        self.new_notification_text.setText(_translate("MainWindow", "New notification!"))
        self.info_text.setText(_translate("MainWindow", "Py|Flora designed by r-log 2023© v1.0.0"))