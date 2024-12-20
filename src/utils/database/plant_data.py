import sqlite3


class PlantData:
    def __init__(self, db_name='my_app.db'):
        self.conn = sqlite3.connect(db_name)

    def save_plant(self, user_id, plant_name, date_planted, watering_interval, wathered):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO plants (user_id, plant_name, date_planted, watering_interval, wathered)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, plant_name, date_planted, watering_interval, wathered))
        self.conn.commit()

    def fetch_plants(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM plants WHERE user_id = ?', (user_id,))
        return cursor.fetchall()
