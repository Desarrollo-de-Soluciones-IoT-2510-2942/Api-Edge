import socket
from fastapi import FastAPI
from app.iam.routes import router as iam_router
from app.sensors.routes import router as sensors_router
from sqlalchemy import text

# Intentar conexión a la base de datos al inicio
from sqlalchemy.exc import OperationalError
from app.shared.database import engine

def probar_conexion_db():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Conexión a la base de datos exitosa.")
    except OperationalError as e:
        print("❌ Error al conectar con la base de datos:", e)
        import sys
        sys.exit(1)

probar_conexion_db()

app = FastAPI()
app.include_router(iam_router)
app.include_router(sensors_router)

# Mostrar la URL de la API con la IP local al iniciar
try:
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"\nAPI Edge disponible en: http://{local_ip}:8000\n")
except Exception as e:
    print("No se pudo obtener la IP local:", e)