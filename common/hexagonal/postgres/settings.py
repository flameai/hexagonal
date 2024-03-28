from dotenv import load_dotenv
from pydantic import PositiveInt


from common.environ.settings_class import EnvironSettings


load_dotenv()


class PostgresSettings(EnvironSettings):
    POSTGRES_USER: str = "user"
    POSTGRES_PASSWORD: str = "secret"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: PositiveInt = 5432
    POSTGRES_DB: str = "postgres"


postgres_settings = PostgresSettings()

POSTGRES_USER = postgres_settings.POSTGRES_USER
POSTGRES_PASSWORD = postgres_settings.POSTGRES_PASSWORD
POSTGRES_SERVER = postgres_settings.POSTGRES_SERVER
POSTGRES_PORT = postgres_settings.POSTGRES_PORT
POSTGRES_DB = postgres_settings.POSTGRES_DB

POSTGRES_DSN = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
