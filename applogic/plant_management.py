import sqlite3
import multiprocessing
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QFileDialog, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from applogic.crypto_manager import CryptoManager
import os

plants_data = []
crypto_manager = CryptoManager()


class PlantDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Plant Details")
        self.layout = QVBoxLayout(self)

        self.plantNameEdit = QLineEdit()
        self.datePlantedEdit = QLineEdit()
        self.infoEdit = QLineEdit()

        self.layout.addWidget(QLabel("Name:"))
        self.layout.addWidget(self.plantNameEdit)
        self.layout.addWidget(QLabel("Date of Planting:"))
        self.layout.addWidget(self.datePlantedEdit)
        self.layout.addWidget(QLabel("Additional Info:"))
        self.layout.addWidget(self.infoEdit)

        self.imageLabel = QLabel("No image selected")
        self.selectImageButton = QPushButton("Select Image")
        self.selectImageButton.clicked.connect(self.select_image)

        self.layout.addWidget(self.imageLabel)
        self.layout.addWidget(self.selectImageButton)

        self.addButton = QPushButton("Add")
        self.addButton.clicked.connect(self.accept)

        self.layout.addWidget(self.addButton)

    def select_image(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if filename:
            self.imageLabel.setText(filename)  # Or set pixmap for a preview
            self.imagePath = filename  # Store the image path

    def getDetails(self):
        return self.plantNameEdit.text(), self.datePlantedEdit.text(), self.infoEdit.text(), self.imagePath if hasattr(self, 'imagePath') else None


def add_plant(grid_layout, user_id, add_button):
    dialog = PlantDialog()
    if dialog.exec() == QDialog.DialogCode.Accepted:
        plant_name, date_planted, info, image_path = dialog.getDetails()
        plant_details = {
            "name": plant_name,
            "date": date_planted,
            "info": info,
            "imagePath": image_path
        }

        add_plant_to_db(user_id, plant_name, date_planted, info, image_path)
        plants_data.append(plant_details)

        create_plant_widget(grid_layout, plant_details, add_button)


def add_plant_to_db(user_id, name, date_planted, info, image_path):
    connection = sqlite3.connect('my_app.db')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO plants (user_id, plant_name, date_planted, info, image_path, last_watered)
        VALUES (?, ?, ?, ?, ?, datetime('now'))
    ''', (user_id, name, date_planted, info, image_path))
    connection.commit()
    connection.close()


def load_plants_from_db(user_id):
    connection = sqlite3.connect('my_app.db')
    cursor = connection.cursor()
    cursor.execute('''
        SELECT plant_name, date_planted, info, image_path
        FROM plants
        WHERE user_id = ?
    ''', (user_id,))
    plants = cursor.fetchall()
    connection.close()
    return plants


def load_plants_with_multiprocessing(user_id):
    with multiprocessing.Pool() as pool:
        result = pool.apply_async(load_plants_from_db, (user_id,))
        plants = result.get()  # This will block until the result is available
    return plants


def decrypt_and_populate_plants(grid_layout, user_id, add_button):
    try:
        plants_from_db = load_plants_with_multiprocessing(user_id)

        for plant in plants_from_db:
            plant_details = {
                "name": plant[0],
                "date": plant[1],
                "info": plant[2],
                "imagePath": plant[3]
            }
            plants_data.append(plant_details)
            create_plant_widget(grid_layout, plant_details, add_button)

        print("Local data populated:", plants_data)

    except Exception as e:
        print("Error loading or populating data:", e)


def create_plant_widget(grid_layout, plant_details, add_button):
    plant_widget = QWidget()
    plant_widget.setFixedSize(300, 300)
    plant_widget.setStyleSheet("""
        QWidget {
            background-color: rgb(18, 88, 83);
            border-radius: 20px;
        }
    """)
    plant_layout = QHBoxLayout(plant_widget)

    image_label = QLabel()
    if plant_details["imagePath"] and os.path.exists(plant_details["imagePath"]):
        pixmap = QPixmap(plant_details["imagePath"])
        if not pixmap.isNull():  # Check if the pixmap is loaded properly
            image_label.setPixmap(pixmap.scaled(
                100, 100, Qt.AspectRatioMode.KeepAspectRatio))
        else:
            image_label.setText("Invalid Image")
    else:
        image_label.setText("No Image")

    image_label.setFixedSize(100, 100)
    plant_layout.addWidget(image_label)

    text_layout = QVBoxLayout()
    text_layout.addWidget(QLabel(f"Name: {plant_details['name']}"))
    text_layout.addWidget(QLabel(f"Date of Planting: {plant_details['date']}"))
    text_layout.addWidget(QLabel(f"Additional Info: {plant_details['info']}"))
    plant_layout.addLayout(text_layout)

    plant_layout.setSpacing(20)

    position = grid_layout.count() - 1  # Positions before adding a new widget.
    row, column = calculate_button_position(position)

    grid_layout.addWidget(plant_widget, row, column)

    # Calculate new position for the add button (next position)
    new_button_row, new_button_column = calculate_button_position(position + 1)
    reposition_add_button(grid_layout, add_button,
                          new_button_row, new_button_column)


def calculate_button_position(position):
    row = position // 3
    column = position % 3
    return row, column


def reposition_add_button(grid_layout, add_button, row, column):
    grid_layout.addWidget(add_button, row, column)
