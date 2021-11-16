import logging
from functools import lru_cache
from pydantic import BaseSettings, PostgresDsn


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    
    SQLALCHEMY_DATABASE_URI: PostgresDsn
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()