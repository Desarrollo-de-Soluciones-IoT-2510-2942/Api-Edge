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

@router.post("/devices", response_model=schemas.Device)
def create_device(device: schemas.DeviceIn, db: Session = Depends(get_db)):
    return crud.create_device(db, device)

@router.get("/devices", response_model=List[schemas.Device])
def list_devices(db: Session = Depends(get_db)):
    return crud.get_devices(db)
