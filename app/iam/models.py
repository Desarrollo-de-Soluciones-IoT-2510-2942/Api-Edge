from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.shared.database import Base

class Device(Base):
    __tablename__ = "Device"
    Id = Column(Integer, primary_key=True, autoincrement=True)
    CropId = Column(Integer, nullable=False)
    Name = Column(String(100), nullable=False)
    CreatedUser = Column(Integer, nullable=False)
    UpdatedUser = Column(Integer, nullable=True)
    CreateDate = Column(DateTime, nullable=False, default=datetime.now)
    UpdatedDate = Column(DateTime, nullable=True)
    IsActive = Column(Integer, nullable=False, default=1)
    IpAddress = Column(Text, nullable=True)
    Action = Column(Text, nullable=True)
    AdditionalInfo = Column(Text, nullable=True)
    sensors = relationship("app.sensors.models.Sensor", back_populates="device")
