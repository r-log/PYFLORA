from ...utils.database import PlantData


class PlantManagementService:
    def __init__(self):
        self.plant_data = PlantData()

    def add_plant(self, user_id, plant_name, date_planted, watering_interval, watered):
        return self.plant_data.save_plant(user_id, plant_name, date_planted, watering_interval, watered)

    def get_user_plants(self, user_id):
        return self.plant_data.fetch_plants(user_id)
