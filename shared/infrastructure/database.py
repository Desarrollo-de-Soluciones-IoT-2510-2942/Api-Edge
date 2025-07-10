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
    # Configuraciones para Azure y conexiones robustas
    autocommit=True,
    charset='utf8mb4',
    sql_mode='PIPES_AS_CONCAT',
    use_unicode=True,
    # Configuraciones de timeout y reconexión
    connect_timeout=60,
    read_timeout=60,
    write_timeout=60,
    # Pool de conexiones
    max_connections=20,
    stale_timeout=300  # 5 minutos
)

def safe_db_connection():
    """
    Función helper para manejar conexiones de base de datos con retry automático.
    """
    max_retries = 3
    retry_delay = 1  # segundo
    
    for attempt in range(max_retries):
        try:
            if db.is_closed():
                db.connect()
            # Test the connection
            db.execute_sql('SELECT 1')
            return True
        except Exception as e:
            logger.warning(f"Intento {attempt + 1} de conexión falló: {e}")
            if db and not db.is_closed():
                try:
                    db.close()
                except:
                    pass
            
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                retry_delay *= 2  # Backoff exponencial
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
            safe_db_connection()
        else:
            # Verificar si la conexión está realmente activa
            db.execute_sql('SELECT 1')
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
        max_retries = 3
        last_exception = None
        
        for attempt in range(max_retries):
            try:
                ensure_connection()
                return func(*args, **kwargs)
            except Exception as e:
                last_exception = e
                logger.warning(f"Error en operación de BD (intento {attempt + 1}): {e}")
                
                # Si es un error de conexión, intentar reconectar
                if "InterfaceError" in str(type(e)) or "OperationalError" in str(type(e)):
                    if not db.is_closed():
                        try:
                            db.close()
                        except:
                            pass
                    
                    if attempt < max_retries - 1:
                        time.sleep(1 * (attempt + 1))  # Backoff
                        continue
                else:
                    # Si no es error de conexión, no reintentar
                    raise e
        
        # Si llegamos aquí, todos los intentos fallaron
        raise last_exception
    
    return wrapper

