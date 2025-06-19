# NutriControl Api Edge

NutriControl Api Edge es una **API** desarrollada con **FastAPI** y **SQLAlchemy** para la gestión y monitoreo de datos nutricionales y sensores en entornos agrícolas.

## Características principales

- Gestión de **dispositivos** y **sensores**.
- Registro y consulta de **lecturas de sensores** (temperatura, humedad, luz, pH, nutrientes, etc).
- Arquitectura modular y escalable.
- Conexión a base de datos MySQL.

## Estructura del proyecto

```
main.py                # Punto de entrada de la API
app/
  iam/                 # Módulo de gestión de dispositivos
    models.py          # Modelos SQLAlchemy para dispositivos
    crud.py            # Operaciones CRUD para dispositivos
    routes.py          # Endpoints de la API para dispositivos
    schemas.py         # Esquemas Pydantic para validación
  sensors/             # Módulo de gestión de sensores y lecturas
    models.py          # Modelos SQLAlchemy para sensores y lecturas
    crud.py            # Operaciones CRUD para sensores y lecturas
    routes.py          # Endpoints de la API para sensores y lecturas
    schemas.py         # Esquemas Pydantic para validación
  shared/              # Recursos compartidos
    database.py        # Configuración de la base de datos
    enums.py           # Enumeraciones para tipos de sensores
requirements.txt       # Dependencias del proyecto
README.md              # Este archivo
```

## Endpoints principales

- `/devices` - Alta y consulta de dispositivos
- `/sensors` - Alta y consulta de sensores
- `/sensor-readings` - Registro y consulta de lecturas de sensores

## Requisitos

- Python 3.8 o superior
- pip

## Instalación en Windows

1. **Clona el repositorio:**
   ```sh
   git clone https://github.com/tu_usuario/nutricontroledge.git
   cd nutricontroledge
   ```

2. **Crea un entorno virtual e instala dependencias:**
   ```sh
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Inicia la aplicación:**
   ```sh
   uvicorn main:app --reload
   ```

La API estará disponible en `http://localhost:8000` o en la IP local mostrada en consola.

## Notas
- La configuración de la base de datos se encuentra en `app/shared/database.py`.
