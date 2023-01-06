
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Docper"
    APP_VERSION: str = "0.0.1"
    POSTGRESQL_HOSTNAME: str = "localhost"
    POSTGRESQL_USERNAME: str = "postgres_user"
    POSTGRESQL_PASSWORD: str = "postgres_password"
    POSTGRESQL_DATABASE: str = "postgresql"


settings = Settings()
