from enum import Enum

class SensorType(str, Enum):
    TEMPERATURE = "Temperature"
    HUMIDITY = "Humidity"
    LIGHT = "Light"
    RAIN = "Rain"
    PH = "pH"
    NUTRIENTS = "Nutrients"
