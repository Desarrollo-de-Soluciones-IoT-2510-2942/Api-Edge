from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import urllib.parse

DB_USER = "freedb_Farmeer"
DB_PASSWORD = urllib.parse.quote_plus("&FgtPgwszGz#45$")
DB_HOST = "sql.freedb.tech"
DB_PORT = "3306"
DB_NAME = "freedb_NutriControlDB"

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()