from pydantic import BaseModel
from datetime import datetime

class DeviceIn(BaseModel):
    name: str
    created_user: int

class Device(BaseModel):
    id: int
    crop_id: int
    name: str
    created_user: int
    created_date: datetime
    is_active: bool = True
    class Config:
        orm_mode = True
