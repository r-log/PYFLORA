from PyQt6 import QtWidgets, QtCore


class ClickableLabel(QtWidgets.QLabel):
    """A custom QLabel that can be clicked."""
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.clicked.emit()
