from sqlalchemy import Column, Integer, String, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.shared.database import Base

class Sensor(Base):
    __tablename__ = "Sensor"
    Id = Column(Integer, primary_key=True, autoincrement=True)
    DeviceId = Column(Integer, ForeignKey("Device.Id"), nullable=False)
    Type = Column(Integer, nullable=False)
    UnitOfMeasurement = Column(String(20), nullable=False)
    Status = Column(String(20), nullable=False)
    CreatedUser = Column(Integer, nullable=False)
    UpdatedUser = Column(Integer, nullable=True)
    CreateDate = Column(DateTime, nullable=False, default=datetime.now)
    UpdatedDate = Column(DateTime, nullable=True)
    IsActive = Column(Integer, nullable=False, default=1)
    IpAddress = Column(Text, nullable=True)
    Action = Column(Text, nullable=True)
    AdditionalInfo = Column(Text, nullable=True)
    device = relationship("app.iam.models.Device", back_populates="sensors")
    readings = relationship("SensorReading", back_populates="sensor")

class SensorReading(Base):
    __tablename__ = "SensorReading"
    Id = Column(Integer, primary_key=True, autoincrement=True)
    SensorId = Column(Integer, ForeignKey("Sensor.Id"), nullable=False)
    Timestamp = Column(DateTime, nullable=False)
    Value = Column(Float, nullable=False)
    CreatedUser = Column(Integer, nullable=False)
    UpdatedUser = Column(Integer, nullable=True)
    CreateDate = Column(DateTime, nullable=False, default=datetime.now)
    UpdatedDate = Column(DateTime, nullable=True)
    IsActive = Column(Integer, nullable=False, default=1)
    IpAddress = Column(Text, nullable=True)
    Action = Column(Text, nullable=True)
    AdditionalInfo = Column(Text, nullable=True)
    sensor = relationship("Sensor", back_populates="readings")
