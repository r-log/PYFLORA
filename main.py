from PyQt6.QtWidgets import QApplication
import sys

from applogic.ui_handler import UiHandler


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = UiHandler()  # Create an instance of UiHandler
    window.show()

    sys.exit(app.exec())
