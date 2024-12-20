from PyQt6 import QtWidgets, QtCore


class BaseUI:
    """Base class for UI components with common functionality."""

    def setup_window_behavior(self, window):
        """Setup common window behaviors like frameless window and dragging."""
        window.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        window.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

    def center_on_screen(self, window):
        """Center the window on the screen."""
        center = QtWidgets.QApplication.primaryScreen().availableGeometry().center()
        geo = window.frameGeometry()
        geo.moveCenter(center)
        window.move(geo.topLeft())
