from PyQt6.QtCore import QPoint, Qt
from PyQt6.QtWidgets import QMainWindow


class DragHandler:
    def __init__(self, window: QMainWindow):
        # Initialize the DragHandler with a reference to the QMainWindow
        self._window = window
        self._dragging = False  # Flag to track whether dragging is in progress
        self._drag_position = QPoint()  # Store the initial position of the drag

    def mousePressEvent(self, event):
        # Handle mouse press event
        if event.button() == Qt.MouseButton.LeftButton:
            # Left mouse button pressed, initiate dragging
            self._dragging = True
            self._drag_position = event.globalPosition().toPoint()  # Store initial position
            event.accept()

    def mouseMoveEvent(self, event):
        # Handle mouse move event
        if self._dragging and event.buttons() == Qt.MouseButton.LeftButton:
            # If dragging and left mouse button held, move the window accordingly
            self._window.move(
                self._window.pos() + event.globalPosition().toPoint() - self._drag_position)
            self._drag_position = event.globalPosition().toPoint()  # Update drag position
            event.accept()

    def mouseReleaseEvent(self, event):
        # Handle mouse release event
        self._dragging = False  # Dragging is no longer in progress
        self._drag_position = QPoint()  # Clear the drag position
