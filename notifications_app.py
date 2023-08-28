import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import mysql.connector
from temperature_monitor import TemperatureMonitor

class NotificationDialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui_notification.ui", self)  # Load the UI file
        self.setWindowTitle("Temperature Notification")

        self.send_button.clicked.connect(self.send_notification)

        self.temperature_monitor = TemperatureMonitor()

    def send_notification(self, title, message):
        try:
            db_connection = mysql.connector.connect(
                host="your_host",
                user="your_user",
                password="your_password",
                database="your_database"
            )

            cursor = db_connection.cursor()
            query = "INSERT INTO notifications (title, message) VALUES (%s, %s)"
            values = (title, message)
            cursor.execute(query, values)
            db_connection.commit()

            cursor.close()
            db_connection.close()

            self.status_label.setText("Notification sent successfully!")
        except Exception as e:
            self.status_label.setText("Error sending notification: " + str(e))

    def check_temperature_change(self):
        temperature_changed, current_temperature, temperature_difference = self.temperature_monitor.check_temperature_change()

        if temperature_changed:
            notification_title = "Temperature Change Alert"
            notification_message = f"Temperature has changed by {temperature_difference:.2f} degrees (Current: {current_temperature:.2f}°C)."
            self.send_notification(notification_title, notification_message)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = NotificationDialog()
    main_window.show()

    timer = QtCore.QTimer()
    timer.timeout.connect(main_window.check_temperature_change)
    timer.start(5000)  # Check temperature every 5 seconds

    sys.exit(app.exec_())
