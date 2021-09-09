from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import settings


host = settings.POSTGRES_HOST
port = settings.POSTGRES_PORT
user = settings.POSTGRES_USER
password = settings.POSTGRES_PASS
db = settings.POSTGRES_DB
dialect = settings.DATABASE_CONFIG.DIALECT
driver = settings.DATABASE_CONFIG.DRIVER


SQLALCHEMY_DATABASE_URI = f"{dialect}+{driver}://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()