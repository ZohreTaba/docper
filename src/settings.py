
from pydantic import BaseSettings


class Settings(BaseSettings):
    DEFAULT_USER = "Admin"
    APP_NAME: str = "Docper"
    APP_VERSION: str = "0.0.1"
    POSTGRES_HOSTNAME: str = "localhost"
    POSTGRES_DATABASE: str = "postgres"
    POSTGRES_USERNAME: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_PORT: int = 5432


settings = Settings()
