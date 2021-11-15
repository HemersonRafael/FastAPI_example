from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_settings


Engine = create_engine(get_settings().SQLALCHEMY_DATABASE_URI)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)