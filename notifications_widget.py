import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5 import QtCore

class NotificationWidget(QWidget):
    def __init__(self, title, message):
        super().__init__()
        self.setWindowTitle(title)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(message))

        close_button = QPushButton('Close')
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

        self.setWindowFlags(
            # Set the widget as a popup window
            QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint
        )

        # You can add styling here to make it look like a notification


if __name__ == '__main__':
    app = QApplication(sys.argv)

    title = "Notification Title"
    message = "This is a sample notification message."

    notification = NotificationWidget(title, message)
    notification.setGeometry(100, 100, 300, 100)  # Adjust position and size
    notification.show()

    sys.exit(app.exec_())
