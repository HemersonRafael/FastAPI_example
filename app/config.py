from pydantic import BaseSettings, BaseModel


class DatabaseConfig (BaseModel):
    DIALECT: str = "postgresql"
    DRIVER: str = "psycopg2"

class Settings(BaseSettings):
    
    DATABASE_CONFIG : DatabaseConfig = DatabaseConfig()
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASS: str
    POSTGRES_DB: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings =  Settings(_env_file='.env', _env_file_encoding='utf-8')