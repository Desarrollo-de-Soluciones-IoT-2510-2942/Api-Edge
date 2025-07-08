"""Flask application entry point for the Smart Band Edge Service."""

from flask import Flask, jsonify
import traceback
import logging

import iam.application.services
from readings.interfaces.services import readings_api
from iam.interfaces.services import iam_api
from shared.infrastructure.database import init_db

# Configurar logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['DEBUG'] = True  # Habilitar modo debug
app.register_blueprint(iam_api)
app.register_blueprint(readings_api)

first_request = True

@app.before_request
def setup():
    """Initialize the database connection before the first request."""
    global first_request
    if first_request:
        first_request = False
        try:
            # Solo verificar conexión, no crear tablas
            from shared.infrastructure.database import db
            db.connect()
            db.close()
            logger.info("Conexión a base de datos exitosa")
        except Exception as e:
            logger.error(f"Error conectando a la base de datos: {e}")
            logger.error(traceback.format_exc())
        
        try:
            auth_application_service = iam.application.services.AuthApplicationService()
            auth_application_service.get_or_create_test_device()
            logger.info("Dispositivo de prueba creado exitosamente")
        except Exception as e:
            logger.error(f"Error creando dispositivo de prueba: {e}")
            logger.error(traceback.format_exc())

# Manejadores de errores personalizados
@app.errorhandler(500)
def internal_error(error):
    """Manejar errores internos del servidor con información detallada."""
    logger.error(f"Error interno del servidor: {error}")
    logger.error(traceback.format_exc())
    
    return jsonify({
        'error': 'Internal Server Error',
        'message': str(error),
        'traceback': traceback.format_exc() if app.config['DEBUG'] else None
    }), 500

@app.errorhandler(Exception)
def handle_exception(e):
    """Manejar todas las excepciones no capturadas."""
    logger.error(f"Excepción no manejada: {e}")
    logger.error(traceback.format_exc())
    
    return jsonify({
        'error': 'Unhandled Exception',
        'message': str(e),
        'traceback': traceback.format_exc() if app.config['DEBUG'] else None
    }), 500

@app.route('/health')
def health_check():
    """Endpoint para verificar el estado de la aplicación."""
    try:
        # Verificar conexión a base de datos
        from shared.infrastructure.database import db
        db.connect()
        db.close()
        return jsonify({'status': 'healthy', 'database': 'connected'}), 200
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return jsonify({
            'status': 'unhealthy', 
            'database': 'disconnected',
            'error': str(e)
        }), 500

if __name__ == "__main__":
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        logger.error(f"Error iniciando la aplicación: {e}")
        logger.error(traceback.format_exc())
