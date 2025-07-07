
# NutriControl Sensor API Service

## Overview

NutriControl Sensor API Service is a Python-based application for processing and analyzing sensor data from smart devices. It provides real-time data collection, device authentication, and RESTful APIs for sensor readings and monitoring.

## Features

- Real-time sensor data ingestion
- Device authentication and management
- RESTful API for sensor data access and control
- Edge processing and analytics
- MySQL database integration (freedb_NutriControlDB)
- Easy integration with cloud or local systems

## Dependencies

- Python 3.12 or higher
- Flask (web framework)
- Peewee (ORM for MySQL)
- PyMySQL (MySQL driver)
- python-dateutil (date and time handling)

## Domain-Driven Design (DDD) Structure

The project follows a Domain-Driven Design (DDD) approach, distributing the features in two main bounded contexts:
- **Sensor Monitoring**: Manages sensor readings from smart devices, including various sensor data measurements.
- **Identity and Access Management**: Handles device authentication.

Inside each bounded context, code is organized into distinct layers:
- **Domain**: Contains core business logic and domain models.
- **Application**: Contains application services and use cases.
- **Infrastructure**: Contains data access, external service integrations, and configurations.
- **Interfaces**: Contains API controllers and user interfaces.

## Database Configuration

The application connects to a MySQL database with the following configuration:
- **Host**: sql.freedb.tech
- **Port**: 3306
- **Database**: freedb_NutriControlDB
- **Table**: SensorReading

## Usage

### Start the Service

```bash
python app.py
```

The service will connect to the MySQL database and verify the connection on startup.

### API Endpoints

- `POST /api/v1/sensor-readings` — Submit sensor data readings

### Example API Usage

**Submit a sensor reading:**
```bash
curl -X POST http://localhost:5000/api/v1/sensor-readings \
  -H "Content-Type: application/json" \
  -d '{
    "sensor_id": 1,
    "value": 36.5,
    "created_user": 1,
    "action": "TEMPERATURE_READING",
    "additional_info": "Body temperature sensor"
  }'
```

**Required fields:**
- `sensor_id` (int): Identifier of the sensor
- `value` (double): Sensor reading value
- `created_user` (int): User who created the record

**Optional fields:**
- `timestamp` (datetime): When the reading was taken (defaults to current time)
- `ip_address` (string): IP address (defaults to request IP)
- `action` (string): Action description
- `additional_info` (string): Additional information

**Response example:**
```json
{
  "id": 1,
  "sensor_id": 1,
  "timestamp": "2025-07-06T12:30:00Z",
  "value": 36.5,
  "created_user": 1,
  "create_date": "2025-07-06T12:30:00Z",
  "is_active": true,
  "ip_address": "127.0.0.1",
  "action": "TEMPERATURE_READING",
  "additional_info": "Body temperature sensor"
}
```

## Database Schema

The `SensorReading` table structure:
- `Id` (int, AUTO_INCREMENT, PRIMARY KEY)
- `SensorId` (int, NOT NULL)
- `Timestamp` (datetime(6), NOT NULL)
- `Value` (double, NOT NULL)
- `CreatedUser` (int, NOT NULL)
- `UpdatedUser` (int, NULL)
- `CreateDate` (datetime(6), NOT NULL, DEFAULT CURRENT_TIMESTAMP)
- `UpdatedDate` (datetime(6), NULL)
- `IsActive` (tinyint(1), NOT NULL, DEFAULT 1)
- `IpAddress` (longtext, NULL)
- `Action` (longtext, NULL)
- `AdditionalInfo` (longtext, NULL)

## NutriControl Project

This service is part of the NutriControl ecosystem for nutritional monitoring and sensor data management.

Refer to the code-level documentation for full details.

