"""Domain entities for the Readings-bounded context."""
from datetime import datetime


class SensorReading:
    """Represents a sensor reading entity in the Readings context.

    Attributes:
        id (int, optional): Unique identifier for the reading.
        sensor_id (int): Identifier of the sensor that generated the reading.
        timestamp (datetime): When the reading was taken.
        value (float): The sensor value.
        created_user (int): User who created the record.
        updated_user (int, optional): User who last updated the record.
        create_date (datetime): When the record was created.
        updated_date (datetime, optional): When the record was last updated.
        is_active (bool): Whether the record is active.
        ip_address (str, optional): IP address of the request.
        action (str, optional): Action performed.
        additional_info (str, optional): Additional information.
    """

    def __init__(self, sensor_id: int, timestamp: datetime, value: float, created_user: int, 
                 id: int = None, updated_user: int = None, create_date: datetime = None, 
                 updated_date: datetime = None, is_active: bool = True, ip_address: str = None,
                 action: str = None, additional_info: str = None):
        """Initialize a SensorReading instance.

        Args:
            sensor_id (int): Sensor identifier.
            timestamp (datetime): When the reading was taken.
            value (float): The sensor value.
            created_user (int): User who created the record.
            id (int, optional): Reading identifier. Defaults to None.
            updated_user (int, optional): User who last updated the record.
            create_date (datetime, optional): When the record was created.
            updated_date (datetime, optional): When the record was last updated.
            is_active (bool): Whether the record is active. Defaults to True.
            ip_address (str, optional): IP address of the request.
            action (str, optional): Action performed.
            additional_info (str, optional): Additional information.
        """
        self.id = id
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value
        self.created_user = created_user
        self.updated_user = updated_user
        self.create_date = create_date or datetime.now()
        self.updated_date = updated_date
        self.is_active = is_active
        self.ip_address = ip_address
        self.action = action
        self.additional_info = additional_info