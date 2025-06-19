from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SensorIn(BaseModel):
    DeviceId: int = Field(..., description="ID del dispositivo al que pertenece el sensor")
    Type: int = Field(..., description="Tipo de sensor (usa el valor entero correspondiente)")
    UnitOfMeasurement: str
    Status: str
    CreatedUser: int
    UpdatedUser: Optional[int] = None
    IpAddress: Optional[str] = None
    Action: Optional[str] = None
    AdditionalInfo: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "DeviceId": 1,
                "Type": 2,
                "UnitOfMeasurement": "Celsius",
                "Status": "Active",
                "CreatedUser": 1
            }
        }

class Sensor(SensorIn):
    Id: int
    CreateDate: datetime
    UpdatedDate: Optional[datetime] = None
    IsActive: bool = True

    class Config:
        orm_mode = True

class SensorReadingIn(BaseModel):
    SensorId: int
    Timestamp: datetime
    Value: float
    CreatedUser: int
    UpdatedUser: Optional[int] = None
    IpAddress: Optional[str] = None
    Action: Optional[str] = None
    AdditionalInfo: Optional[str] = None

class SensorReading(SensorReadingIn):
    Id: int
    CreateDate: datetime
    UpdatedDate: Optional[datetime] = None
    IsActive: bool = True

    class Config:
        orm_mode = True
