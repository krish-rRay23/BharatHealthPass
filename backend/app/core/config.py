from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Bharat Health Pass (BHP)"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    DATABASE_URL: str
    REDIS_URL: str
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
