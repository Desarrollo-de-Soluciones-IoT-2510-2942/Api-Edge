"""
Repository for sensor reading persistence.

Handles saving sensor readings to the database using Peewee ORM models.
"""
from readings.domain.entities import SensorReading
from readings.infrastructure.models import SensorReading as SensorReadingModel
from shared.infrastructure.database import with_db_connection
import logging

logger = logging.getLogger(__name__)


class SensorReadingRepository:
    """
    Repository for managing SensorReading persistence.
    """
    
    @staticmethod
    @with_db_connection
    def save(sensor_reading) -> SensorReading:
        """
        Save a SensorReading entity to the database.
        Args:
            sensor_reading (SensorReading): The sensor reading to save.
        Returns:
            SensorReading: The saved sensor reading with assigned ID.
        """
        try:
            logger.info(f"Guardando sensor reading para sensor_id: {sensor_reading.sensor_id}")
            
            record = SensorReadingModel.create(
                SensorId=sensor_reading.sensor_id,
                Timestamp=sensor_reading.timestamp,
                Value=sensor_reading.value,
                CreatedUser=sensor_reading.created_user,
                UpdatedUser=sensor_reading.updated_user,
                CreateDate=sensor_reading.create_date,
                UpdatedDate=sensor_reading.updated_date,
                IsActive=sensor_reading.is_active,
                IpAddress=sensor_reading.ip_address,
                Action=sensor_reading.action,
                AdditionalInfo=sensor_reading.additional_info
            )
            
            logger.info(f"Sensor reading guardado exitosamente con ID: {record.Id}")
            
            return SensorReading(
                sensor_id=sensor_reading.sensor_id,
                timestamp=sensor_reading.timestamp,
                value=sensor_reading.value,
                created_user=sensor_reading.created_user,
                id=record.Id,
                updated_user=sensor_reading.updated_user,
                create_date=sensor_reading.create_date,
                updated_date=sensor_reading.updated_date,
                is_active=sensor_reading.is_active,
                ip_address=sensor_reading.ip_address,
                action=sensor_reading.action,
                additional_info=sensor_reading.additional_info
            )
        except Exception as e:
            logger.error(f"Error guardando sensor reading: {e}")
            raise

