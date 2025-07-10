"""
Database initialization for the Smart Band Edge Service.

Sets up the MySQL database and creates required tables for devices and SensorReading.
"""
from peewee import MySQLDatabase
import logging
import time

logger = logging.getLogger(__name__)

# Initialize MySQL database with retry and reconnection settings
db = MySQLDatabase(
    'freedb_NutriControlDB',
    user='freedb_Farmeer',
    password='&FgtPgwszGz#45$',
    host='sql.freedb.tech',
    port=3306,
    # Configuraciones compatibles para Azure
    autocommit=True,
    charset='utf8mb4',
    # Configuraciones de timeout
    connect_timeout=60,
    read_timeout=60,
    write_timeout=60
)

def safe_db_connection():
    """
    Función helper para manejar conexiones de base de datos con retry automático.
    """
    max_retries = 3
    retry_delay = 0.5  # Reducido para ser más rápido
    
    for attempt in range(max_retries):
        try:
            if db.is_closed():
                logger.info(f"Conectando a la base de datos (intento {attempt + 1})")
                db.connect()
            # Test the connection with a simple query
            db.execute_sql('SELECT 1')
            logger.info("Conexión a base de datos verificada exitosamente")
            return True
        except Exception as e:
            logger.warning(f"Intento {attempt + 1} de conexión falló: {e}")
            if not db.is_closed():
                try:
                    db.close()
                except:
                    pass
            
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                retry_delay *= 1.5  # Backoff más suave
            else:
                logger.error(f"No se pudo conectar a la base de datos después de {max_retries} intentos")
                raise e
    return False

def ensure_connection():
    """
    Asegura que la conexión a la base de datos esté activa antes de cualquier operación.
    """
    try:
        if db.is_closed():
            logger.info("Base de datos cerrada, reconectando...")
            safe_db_connection()
        else:
            # Verificar si la conexión está realmente activa
            try:
                db.execute_sql('SELECT 1')
            except Exception as e:
                logger.warning(f"Conexión inactiva detectada: {e}")
                raise e
    except Exception as e:
        logger.warning(f"Conexión perdida, reconectando: {e}")
        if not db.is_closed():
            try:
                db.close()
            except:
                pass
        safe_db_connection()

def init_db() -> None:
    """
    Initialize the database and create tables for Device and SensorReading models.
    """
    ensure_connection()
    from iam.infrastructure.models import Device
    from readings.infrastructure.models import SensorReading
    db.create_tables([Device, SensorReading], safe=True)
    if not db.is_closed():
        db.close()

def with_db_connection(func):
    """
    Decorador para manejar automáticamente las conexiones de base de datos.
    Reconecta automáticamente si la conexión se pierde.
    """
    def wrapper(*args, **kwargs):
        max_retries = 2  # Reducido para ser más rápido
        last_exception = None
        
        for attempt in range(max_retries):
            try:
                ensure_connection()
                return func(*args, **kwargs)
            except Exception as e:
                last_exception = e
                error_msg = str(e).lower()
                logger.warning(f"Error en operación de BD (intento {attempt + 1}): {e}")
                
                # Si es un error de conexión, intentar reconectar
                if any(keyword in error_msg for keyword in [
                    'interfaceerror', 'operationalerror', 'connection', 
                    'lost connection', 'gone away', 'timeout'
                ]):
                    logger.info("Detectado error de conexión, cerrando conexión actual")
                    if not db.is_closed():
                        try:
                            db.close()
                        except:
                            pass
                    
                    if attempt < max_retries - 1:
                        time.sleep(0.5 * (attempt + 1))  # Backoff más rápido
                        continue
                else:
                    # Si no es error de conexión, no reintentar
                    logger.error(f"Error no relacionado con conexión: {e}")
                    raise e
        
        # Si llegamos aquí, todos los intentos fallaron
        logger.error(f"Operación falló después de {max_retries} intentos")
        raise last_exception
    
    return wrapper

def test_connection():
    """
    Función simple para probar la conexión a la base de datos.
    """
    try:
        ensure_connection()
        return True, "Conexión exitosa"
    except Exception as e:
        return False, f"Error de conexión: {e}"

