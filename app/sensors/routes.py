from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, crud
from app.shared.database import SessionLocal
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sensors", response_model=schemas.Sensor)
def create_sensor(sensor: schemas.SensorIn, db: Session = Depends(get_db)):
    return crud.create_sensor(db, sensor)

@router.get("/sensors", response_model=List[schemas.Sensor])
def list_sensors(db: Session = Depends(get_db)):
    return crud.get_sensors(db)

@router.post("/sensor-readings", response_model=schemas.SensorReading)
def create_sensor_reading(reading: schemas.SensorReadingIn, db: Session = Depends(get_db)):
    return crud.create_sensor_reading(db, reading)

@router.get("/sensor-readings", response_model=List[schemas.SensorReading])
def list_sensor_readings(db: Session = Depends(get_db)):
    return crud.get_sensor_readings(db)
