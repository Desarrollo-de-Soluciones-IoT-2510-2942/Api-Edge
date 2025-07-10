"""Repositories for the IAM bounded context."""
from typing import Optional
import logging

import peewee

from iam.domain.entities import Device
from iam.infrastructure.models import Device as DeviceModel
from shared.infrastructure.database import with_db_connection

logger = logging.getLogger(__name__)

class DeviceRepository:
    """Repository for managing Device entities."""

    @staticmethod
    @with_db_connection
    def find_by_id_and_api_key(device_id: str, api_key: str) -> Optional[Device]:
        """Find a device by its ID and API key.

        Args:
            device_id (str): Unique identifier of the device.
            api_key (str): API key for authentication.

        Returns:
            Optional[Device]: Device entity if found, None otherwise.
        """
        try:
            logger.info(f"Buscando dispositivo con ID: {device_id}")
            device = DeviceModel.get(
                (DeviceModel.device_id == device_id) & (DeviceModel.api_key == api_key)
            )
            logger.info(f"Dispositivo encontrado: {device_id}")
            return Device(device.device_id, device.api_key, device.created_at)
        except peewee.DoesNotExist:
            logger.warning(f"Dispositivo no encontrado: {device_id}")
            return None
        except Exception as e:
            logger.error(f"Error buscando dispositivo {device_id}: {e}")
            raise

    @staticmethod
    @with_db_connection
    def get_or_create_test_device() -> Device:
        """Get or create a test device for development.

        Returns:
            Device: The test device entity.
        """
        try:
            logger.info("Obteniendo o creando dispositivo de prueba")
            device, created = DeviceModel.get_or_create(
                device_id="smart-band-001",
                defaults={"api_key": "test-api-key-123", "created_at": "2025-06-04T23:23:00Z"}
            )
            if created:
                logger.info("Dispositivo de prueba creado")
            else:
                logger.info("Dispositivo de prueba ya existía")
            return Device(device.device_id, device.api_key, device.created_at)
        except Exception as e:
            logger.error(f"Error obteniendo/creando dispositivo de prueba: {e}")
            raise