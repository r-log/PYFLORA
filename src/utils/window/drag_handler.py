from PyQt6.QtCore import QPoint, Qt
from PyQt6.QtWidgets import QMainWindow
from typing import Optional


class DragHandler:
    """
    Handles window dragging functionality for frameless windows.
    Allows moving windows by clicking and dragging anywhere on them.
    """

    def __init__(self, window: QMainWindow):
        """
        Initialize the DragHandler.

        Args:
            window (QMainWindow): The window to enable dragging for
        """
        self._window = window
        self._dragging = False
        self._drag_position = QPoint()
        self._drag_enabled = True  # Flag to enable/disable dragging

    def mousePressEvent(self, event) -> None:
        """
        Handle mouse press events to initiate dragging.

        Args:
            event: The mouse press event
        """
        if not self._drag_enabled:
            return

        if event.button() == Qt.MouseButton.LeftButton:
            self._dragging = True
            self._drag_position = event.globalPosition().toPoint()
            event.accept()

    def mouseMoveEvent(self, event) -> None:
        """
        Handle mouse move events to move the window.

        Args:
            event: The mouse move event
        """
        if not self._drag_enabled or not self._dragging:
            return

        if event.buttons() == Qt.MouseButton.LeftButton:
            # Calculate new position
            new_pos = self._window.pos() + event.globalPosition().toPoint() - \
                self._drag_position

            # Optional: Add bounds checking to keep window on screen
            self._window.move(new_pos)
            self._drag_position = event.globalPosition().toPoint()
            event.accept()

    def mouseReleaseEvent(self, event) -> None:
        """
        Handle mouse release events to end dragging.

        Args:
            event: The mouse release event
        """
        self._dragging = False
        self._drag_position = QPoint()
        event.accept()

    def enable_dragging(self) -> None:
        """Enable window dragging."""
        self._drag_enabled = True

    def disable_dragging(self) -> None:
        """Disable window dragging."""
        self._drag_enabled = False

    @property
    def is_dragging(self) -> bool:
        """
        Check if the window is currently being dragged.

        Returns:
            bool: True if the window is being dragged, False otherwise
        """
        return self._dragging

    def get_drag_position(self) -> QPoint:
        """
        Get the current drag position.

        Returns:
            QPoint: The current drag position
        """
        return self._drag_position
