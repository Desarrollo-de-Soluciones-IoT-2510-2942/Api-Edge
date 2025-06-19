from sqlalchemy.orm import Session
from . import models, schemas

def create_device(db: Session, device: schemas.DeviceIn):
    db_device = models.Device(
        Name=device.Name,
        CropId=device.CropId,
        CreatedUser=device.CreatedUser
        # Otros campos opcionales si los tienes
    )
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

def get_devices(db: Session):
    return db.query(models.Device).all()
