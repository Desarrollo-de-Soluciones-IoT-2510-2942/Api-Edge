"""
Database initialization for the Smart Band Edge Service.

Sets up the MySQL database and creates required tables for devices and SensorReading.
"""
from peewee import MySQLDatabase

# Initialize MySQL database
db = MySQLDatabase(
    'freedb_NutriControlDB',
    user='freedb_Farmeer',
    password='&FgtPgwszGz#45$',
    host='sql.freedb.tech',
    port=3306
)

def init_db() -> None:
    """
    Initialize the database and create tables for Device and SensorReading models.
    """
    db.connect()
    from iam.infrastructure.models import Device
    from health.infrastructure.models import SensorReading
    db.create_tables([Device, SensorReading], safe=True)
    db.close()

