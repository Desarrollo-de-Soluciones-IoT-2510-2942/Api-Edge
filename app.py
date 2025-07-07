"""Flask application entry point for the Smart Band Edge Service."""

from flask import Flask

import iam.application.services
from readings.interfaces.services import readings_api
from iam.interfaces.services import iam_api
from shared.infrastructure.database import init_db

app = Flask(__name__)
app.register_blueprint(iam_api)
app.register_blueprint(readings_api)

first_request = True

@app.before_request
def setup():
    """Initialize the database connection before the first request."""
    global first_request
    if first_request:
        first_request = False
        # Solo verificar conexión, no crear tablas
        from shared.infrastructure.database import db
        try:
            db.connect()
            db.close()
        except Exception as e:
            print(f"Error conectando a la base de datos: {e}")
        
        auth_application_service = iam.application.services.AuthApplicationService()
        auth_application_service.get_or_create_test_device()

if __name__ == "__main__":
    app.run(debug=True)
