import time
import math


class TemperatureMonitor:
    def __init__(self):
        self.temperature = 20.0

    def update_temperature(self):
        # Simulate changing temperature values using a sine wave pattern
        time_elapsed = time.time()
        self.temperature = 20.0 + 10.0 * math.sin(time_elapsed)

    def get_temperature(self):
        return self.temperature
