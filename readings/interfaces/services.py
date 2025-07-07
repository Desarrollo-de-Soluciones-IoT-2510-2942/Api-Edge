"""Interface services for the Readings-bounded context."""
from flask import Blueprint, request, jsonify

from readings.application.services import SensorReadingApplicationService

readings_api = Blueprint("readings_api", __name__)

# Initialize dependencies
sensor_reading_service = SensorReadingApplicationService()

@readings_api.route("/api/v1/sensor-readings", methods=["POST"])
def create_sensor_reading():
    """Handle POST requests to create a sensor reading.

    Expects JSON with sensor_id, value, created_user, and optional timestamp.

    Returns:
        tuple: (JSON response, status code).
    """
    data = request.json
    try:
        sensor_id = data["sensor_id"]
        value = data["value"]
        created_user = data["created_user"]
        timestamp = data.get("timestamp")
        ip_address = data.get("ip_address", request.remote_addr)
        action = data.get("action", "CREATE")
        additional_info = data.get("additional_info")
        
        reading = sensor_reading_service.create_sensor_reading(
            sensor_id, timestamp, value, created_user, ip_address, action, additional_info
        )
        return jsonify({
            "id": reading.id,
            "sensor_id": reading.sensor_id,
            "timestamp": reading.timestamp.isoformat() + "Z",
            "value": reading.value,
            "created_user": reading.created_user,
            "create_date": reading.create_date.isoformat() + "Z",
            "is_active": reading.is_active,
            "ip_address": reading.ip_address,
            "action": reading.action,
            "additional_info": reading.additional_info
        }), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400