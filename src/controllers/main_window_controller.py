from PyQt6.QtWidgets import (
    QMainWindow,
    QScrollArea,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QPushButton
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from ..views.ui.main_window import Ui_MainWindow
from ..services.plant import PlantManagementService
from ..utils.window import DragHandler
from ..controllers.account_controller import AccountController


class MainWindowController(QMainWindow, Ui_MainWindow):
    def __init__(self, auth_service):
        super().__init__()
        self.auth_service = auth_service
        self.setupUi(self)

        # Initialize controllers
        self.account_controller = AccountController(self.auth_service)

        # Replace placeholder with actual account controller
        account_layout = self.Account.layout()
        account_layout.replaceWidget(
            self.account_placeholder, self.account_controller)
        self.account_placeholder.deleteLater()

        self.drag_handler = DragHandler(self)
        self.plant_service = PlantManagementService()

        # Set window opacity for fade-in effect
        self.setWindowOpacity(0.0)

        # Initialize UI state
        self.content_stacked_widget.setCurrentIndex(0)
        self.home_button_opened_menu.setChecked(True)

        # Set initial menu state
        self.sidemenu_opened_widget.hide()
        self.sidemenu_closed_widget.show()
        self.sidemenu_closed_widget.setFixedWidth(81)
        self.sidemenu_opened_widget.setFixedWidth(150)

        # Connect menu button
        self.open_menu_button.clicked.connect(self.toggle_menu)
        self.initialize_ui()

        # Setup and start fade-in animation
        self.fade_in_animation = QPropertyAnimation(self, b"windowOpacity")
        self.fade_in_animation.setDuration(500)
        self.fade_in_animation.setStartValue(0.0)
        self.fade_in_animation.setEndValue(1.0)
        self.fade_in_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.fade_in_animation.start()

    def toggle_menu(self):
        """Simple toggle between menu states."""
        if self.open_menu_button.isChecked():
            self.sidemenu_closed_widget.hide()
            self.sidemenu_opened_widget.show()
        else:
            self.sidemenu_opened_widget.hide()
            self.sidemenu_closed_widget.show()

    def initialize_ui(self):
        """Initialize the UI components."""
        self.set_window_flags()
        self.setup_button_connections()
        self.initialize_plants_page()

    def set_window_flags(self):
        """Set window flags for frameless window."""
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def initialize_plants_page(self):
        """Initialize the plants page with grid layout."""
        if hasattr(self, 'plantsPage'):
            return  # Prevent reinitialization

        if not hasattr(self, 'Plants'):
            return

        self._setup_plants_layout()
        self._setup_add_plant_button()

    def _setup_plants_layout(self):
        """Set up the plants page layout."""
        self.plantsPage = self.Plants
        self.scrollArea = QScrollArea(self.plantsPage)
        self.scrollArea.setWidgetResizable(True)

        self.plantsContainer = QWidget()
        self.plantsGridLayout = QGridLayout(self.plantsContainer)

        # Set column stretches
        for i in range(3):
            self.plantsGridLayout.setColumnStretch(i, 1)

        self.scrollArea.setWidget(self.plantsContainer)
        self.plantsContainer.setStyleSheet(
            "background-color: rgb(13, 37, 34);border-radius:50px;")

        plants_page_layout = QVBoxLayout(self.plantsPage)
        plants_page_layout.addWidget(self.scrollArea)

    def _setup_add_plant_button(self):
        """Set up the add plant button."""
        self.addPlantButton = QPushButton("Add Plant")
        self.plantsGridLayout.addWidget(
            self.addPlantButton, 0, 0,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.addPlantButton.setFixedSize(300, 300)
        self.addPlantButton.clicked.connect(self._handle_add_plant)

    def _handle_add_plant(self):
        """Handle add plant button click."""
        self.plant_service.add_plant(
            self.plantsGridLayout,
            self.user_id,
            self.addPlantButton
        )

    def setup_button_connections(self):
        """Set up button connections for navigation."""
        # Navigation buttons
        buttons = [
            (self.home_button_opened_menu, self.home_button_closed_menu, 0),
            (self.plants_button_opened_menu, self.plants_button_closed_menu, 1),
            (self.livefeed_button_opened_menu, self.livefeed_button_closed_menu, 2),
            (self.analytics_button_opened_menu,
             self.analytics_button_closed_menu, 3),
            (self.account_button_opened_menu, self.account_button_closed_menu, 4),
        ]

        for opened, closed, index in buttons:
            opened.clicked.connect(lambda x, i=index: self.change_page(i))
            closed.clicked.connect(lambda x, i=index: self.change_page(i))

        # Logout buttons
        self.logout_button_closed_menu.clicked.connect(self.logout)
        self.logout_button_opened_menu.clicked.connect(self.logout)

        # Connect account button
        self.account_button_closed_menu.clicked.connect(
            self._show_account_page)
        self.account_button_opened_menu.clicked.connect(
            self._show_account_page)

    def change_page(self, pageIndex):
        """Change the current page."""
        self.content_stacked_widget.setCurrentIndex(pageIndex)

    # Mouse event handlers for window dragging
    def mousePressEvent(self, event):
        self.drag_handler.mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.drag_handler.mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.drag_handler.mouseReleaseEvent(event)

    def logout(self):
        """Handle logout action."""
        self.close()

    def _show_account_page(self):
        """Switch to account page"""
        self.content_stacked_widget.setCurrentWidget(self.account_controller)
