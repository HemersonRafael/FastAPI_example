from typing import Optional
from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings =  Settings(_env_file='.env', _env_file_encoding='utf-8')