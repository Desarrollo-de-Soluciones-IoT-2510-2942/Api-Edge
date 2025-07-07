"""Domain services for the Readings-bounded context."""
from datetime import datetime, timezone

from dateutil.parser import parse

from readings.domain.entities import SensorReading


class SensorReadingService:
    """Service for managing sensor readings."""

    def __init__(self):
        """Initialize the SensorReadingService.
        """

    @staticmethod
    def create_reading(sensor_id: int, timestamp: str | None, value: float, created_user: int,
                      ip_address: str = None, action: str = None, additional_info: str = None) -> SensorReading:
        """Create a new sensor reading.

        Args:
            sensor_id (int): Sensor identifier.
            timestamp (str): ISO 8601 timestamp (e.g., '2025-06-04T18:23:00-05:00').
            value (float): Sensor value.
            created_user (int): User who created the record.
            ip_address (str, optional): IP address of the request.
            action (str, optional): Action performed.
            additional_info (str, optional): Additional information.

        Returns:
            SensorReading: The created sensor reading entity.

        Raises:
            ValueError: If sensor_id or created_user are invalid or timestamp is malformed.
        """
        try:
            sensor_id = int(sensor_id)
            created_user = int(created_user)
            value = float(value)
            
            if sensor_id <= 0:
                raise ValueError("Invalid sensor_id value")
            if created_user <= 0:
                raise ValueError("Invalid created_user value")
                
            if timestamp:
                parsed_timestamp = parse(timestamp).astimezone(timezone.utc)
            else:
                parsed_timestamp = datetime.now(timezone.utc)
        except (ValueError, TypeError):
            raise ValueError("Invalid data format")

        return SensorReading(
            sensor_id=sensor_id,
            timestamp=parsed_timestamp,
            value=value,
            created_user=created_user,
            ip_address=ip_address,
            action=action,
            additional_info=additional_info
        )
