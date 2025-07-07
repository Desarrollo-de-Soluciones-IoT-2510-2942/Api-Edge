"""Application services for the Readings-bounded context."""

from readings.domain.entities import SensorReading
from readings.domain.services import SensorReadingService
from readings.infrastructure.repositories import SensorReadingRepository

class SensorReadingApplicationService:
    """Application service for creating sensor readings."""

    def __init__(self):
        """Initialize the SensorReadingApplicationService."""
        self.sensor_reading_repository = SensorReadingRepository()
        self.sensor_reading_service = SensorReadingService()

    def create_sensor_reading(self, sensor_id: int, timestamp: str, value: float, 
                            created_user: int, ip_address: str = None, 
                            action: str = None, additional_info: str = None) -> SensorReading:
        """Create a sensor reading without device validation.

        Args:
            sensor_id (int): Sensor identifier.
            timestamp (str): ISO 8601 timestamp.
            value (float): Sensor value.
            created_user (int): User who created the record.
            ip_address (str, optional): IP address of the request.
            action (str, optional): Action performed.
            additional_info (str, optional): Additional information.

        Returns:
            SensorReading: The created sensor reading.
        """
        reading = self.sensor_reading_service.create_reading(
            sensor_id, timestamp, value, created_user, ip_address, action, additional_info
        )
        return self.sensor_reading_repository.save(reading)