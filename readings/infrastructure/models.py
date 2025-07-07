"""
Peewee ORM model for sensor readings.

Defines the SensorReading database table structure for storing sensor data.
"""
from peewee import Model, AutoField, IntegerField, DateTimeField, DoubleField, BooleanField, TextField
from datetime import datetime

from shared.infrastructure.database import db


class SensorReading(Model):
    """
    ORM model for the SensorReading table.
    Represents a sensor reading entry in the database.
    """
    Id = AutoField(primary_key=True)
    SensorId = IntegerField()
    Timestamp = DateTimeField()
    Value = DoubleField()
    CreatedUser = IntegerField()
    UpdatedUser = IntegerField(null=True)
    CreateDate = DateTimeField(default=datetime.now)
    UpdatedDate = DateTimeField(null=True)
    IsActive = BooleanField(default=True)
    IpAddress = TextField(null=True)
    Action = TextField(null=True)
    AdditionalInfo = TextField(null=True)

    class Meta:
        database = db
        table_name = 'SensorReading'

