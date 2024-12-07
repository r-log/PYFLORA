from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QGridLayout, QPushButton, QScrollArea, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, pyqtSignal
from applogic.login_handler import LoginHandler
from ui import Ui_MainWindow
from applogic import plant_management
from .drag_handler import DragHandler
from .ui_event_filter import UiEventFilter
from ui import Ui_LogRegWindow


class UiHandler(QMainWindow, Ui_LogRegWindow):
    logout_signal = pyqtSignal()  # Signal to handle logout

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.drag_handler = DragHandler(self)
        self.login_handler = LoginHandler(self)
        self.ui_event_filter = UiEventFilter(self)

        self.user_id = None  # Store logged-in user ID
        self.plantsGridLayout = None
        self.addPlantButton = None

        self.initialize_ui()

    def initialize_ui(self):
        self.set_window_frameless()
        self.set_initial_focus()
        self.setup_tab_order()
        self.setup_event_filters()
        self.setup_button_connections()
        self.show_sign_in_widget()

    def set_window_frameless(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def set_initial_focus(self):
        self.sign_in_username_input.setFocus()

    def setup_tab_order(self):
        self.setTabOrder(self.sign_in_username_input,
                         self.sign_in_password_input)
        self.setTabOrder(self.sign_in_password_input, self.sign_in_button)
        self.setTabOrder(self.sign_up_username_input,
                         self.sign_up_password_input)
        self.setTabOrder(self.sign_up_password_input,
                         self.sign_up_confirm_password_input)
        self.setTabOrder(self.sign_up_confirm_password_input,
                         self.sign_up_email_input)
        self.setTabOrder(self.sign_up_email_input, self.sign_up_button)

    def setup_event_filters(self):
        self.sign_in_password_input.installEventFilter(self.ui_event_filter)
        self.sign_up_password_input.installEventFilter(self.ui_event_filter)
        self.sign_up_confirm_password_input.installEventFilter(
            self.ui_event_filter)

    def setup_button_connections(self):
        self.sign_in_password_visible.clicked.connect(lambda: self.toggle_password_visibility(
            self.sign_in_password_input, self.sign_in_password_visible))
        self.sign_up_password_visibile.clicked.connect(lambda: self.toggle_password_visibility(
            self.sign_up_password_input, self.sign_up_password_visibile))
        self.sign_up_link.clicked.connect(self.show_sign_up_widget)
        self.sign_in_link.clicked.connect(self.show_sign_in_widget)
        self.sign_up_button.clicked.connect(self.handle_signup)
        self.sign_in_button.clicked.connect(self.handle_signin)
        self.exit_button.clicked.connect(self.exit_app)
        self.logout_signal.connect(self.show_sign_in_widget)

    def show_sign_in_widget(self):
        self.sign_in_widget.setVisible(True)
        self.sign_up_widget.setVisible(False)
        # Reset login inputs if necessary
        self.sign_in_username_input.clear()
        self.sign_in_password_input.clear()
        self.show()

    def show_sign_up_widget(self):
        self.sign_in_widget.setVisible(False)
        self.sign_up_widget.setVisible(True)

    def toggle_password_visibility(self, line_edit, button):
        if line_edit.echoMode() == QLineEdit.EchoMode.Password:
            line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon(":/Icons/Icons/eye.svg"))
        else:
            line_edit.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon(":/Icons/Icons/eye-off.svg"))
        button.show()

    def exit_app(self):
        QApplication.quit()

    def handle_signup(self):
        username = self.sign_up_username_input.text()
        password = self.sign_up_password_input.text()
        confirm_password = self.sign_up_confirm_password_input.text()
        email = self.sign_up_email_input.text()
        self.login_handler.signup(username, password, confirm_password, email)

    def handle_signin(self):
        username = self.sign_in_username_input.text()
        password = self.sign_in_password_input.text()
        self.login_handler.signin(username, password)

    def initialize_plants(self):
        if self.plantsGridLayout is None or self.addPlantButton is None:
            print("Attributes missing in UiHandler. Recheck initialization methods.")
            return

        grid_layout = self.plantsGridLayout
        user_id = self.user_id
        add_button = self.addPlantButton
        plant_management.decrypt_and_populate_plants(
            grid_layout, user_id, add_button)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:
            if self.sign_in_username_input.hasFocus() or self.sign_in_password_input.hasFocus():
                self.sign_in_button.click()
            elif self.sign_up_username_input.hasFocus() or self.sign_up_password_input.hasFocus() or self.sign_up_confirm_password_input.hasFocus() or self.sign_up_email_input.hasFocus():
                self.sign_up_button.click()
        else:
            super().keyPressEvent(event)

    def open_main_window(self):
        self.main_window = MainWindow(self.user_id, self)
        self.main_window.show()
        self.close()

    def set_user_id(self, user_id):
        self.user_id = user_id


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user_id, ui_handler):
        super().__init__()
        self.user_id = user_id
        self.ui_handler = ui_handler
        self.setupUi(self)
        self.sidemenu_opened_widget.hide()
        self.content_stacked_widget.setCurrentIndex(0)
        self.home_button_opened_menu.setChecked(True)
        self.drag_handler = DragHandler(self)

        self.initialize_ui()

        # Set the layout reference.
        self.ui_handler.plantsGridLayout = self.plantsGridLayout  # Share layout reference
        self.ui_handler.addPlantButton = self.addPlantButton  # Share button reference

    def initialize_ui(self):
        self.set_window_flags()
        self.setup_button_connections()
        self.initialize_plants_page()

    def set_window_flags(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def initialize_plants_page(self):
        if hasattr(self, 'plantsPage'):
            return  # Prevent reinitialization
        self.plantsPage = self.Plants
        self.scrollArea = QScrollArea(self.plantsPage)
        self.scrollArea.setWidgetResizable(True)
        self.plantsContainer = QWidget()
        self.plantsGridLayout = QGridLayout(self.plantsContainer)
        self.plantsGridLayout.setColumnStretch(0, 1)
        self.plantsGridLayout.setColumnStretch(1, 1)
        self.plantsGridLayout.setColumnStretch(2, 1)
        self.scrollArea.setWidget(self.plantsContainer)
        self.plantsContainer.setStyleSheet(
            "background-color: rgb(13, 37, 34);border-radius:50px;")
        plants_page_layout = QVBoxLayout(self.plantsPage)
        plants_page_layout.addWidget(self.scrollArea)

        self.addPlantButton = QPushButton("Add Plant")
        self.plantsGridLayout.addWidget(
            self.addPlantButton, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        self.addPlantButton.setFixedSize(300, 300)
        self.addPlantButton.clicked.connect(lambda: plant_management.add_plant(
            self.plantsGridLayout, self.user_id, self.addPlantButton))

    def setup_button_connections(self):
        self.home_button_opened_menu.clicked.connect(
            lambda: self.change_page(0))
        self.home_button_closed_menu.clicked.connect(
            lambda: self.change_page(0))
        self.plants_button_opened_menu.clicked.connect(
            lambda: self.change_page(1))
        self.plants_button_closed_menu.clicked.connect(
            lambda: self.change_page(1))
        self.livefeed_button_opened_menu.clicked.connect(
            lambda: self.change_page(2))
        self.livefeed_button_closed_menu.clicked.connect(
            lambda: self.change_page(2))
        self.analytics_button_opened_menu.clicked.connect(
            lambda: self.change_page(3))
        self.analytics_button_closed_menu.clicked.connect(
            lambda: self.change_page(3))
        self.account_button_opened_menu.clicked.connect(
            lambda: self.change_page(4))
        self.account_button_closed_menu.clicked.connect(
            lambda: self.change_page(4))
        self.logout_button_closed_menu.clicked.connect(self.logout)
        self.logout_button_opened_menu.clicked.connect(self.logout)

    def change_page(self, pageIndex):
        self.content_stacked_widget.setCurrentIndex(pageIndex)

    def mousePressEvent(self, event):
        self.drag_handler.mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.drag_handler.mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.drag_handler.mouseReleaseEvent(event)

    def logout(self):
        self.ui_handler.logout_signal.emit()  # Emit the logout signal
        self.close()  # Close the main window
