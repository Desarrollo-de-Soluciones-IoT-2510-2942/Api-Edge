from sqlalchemy.orm import Session
from . import models, schemas

def create_sensor(db: Session, sensor: schemas.SensorIn):
    db_sensor = models.Sensor(
        DeviceId=sensor.DeviceId,
        Type=sensor.Type,
        UnitOfMeasurement=sensor.UnitOfMeasurement,
        Status=sensor.Status,
        CreatedUser=sensor.CreatedUser
        # Otros campos opcionales si los tienes
    )
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

def get_sensors(db: Session):
    return db.query(models.Sensor).all()

def create_sensor_reading(db: Session, reading: schemas.SensorReadingIn):
    db_reading = models.SensorReading(**reading.dict())
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading

def get_sensor_readings(db: Session):
    return db.query(models.SensorReading).all()
