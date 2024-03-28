from dotenv import load_dotenv
from pydantic import PositiveInt

from common.environ.settings_class import EnvironSettings

load_dotenv()


class RedisSettings(EnvironSettings):
    REDIS_HOST: str = "redis"
    REDIS_DB: PositiveInt = 1
    REDIS_POOL_MAX_CONNECTIONS: PositiveInt = 10
    REDIS_PORT: PositiveInt = 6379


redis_settings = RedisSettings()

REDIS_HOST = redis_settings.REDIS_HOST
REDIS_DB = redis_settings.REDIS_DB
REDIS_POOL_MAX_CONNECTIONS = redis_settings.REDIS_POOL_MAX_CONNECTIONS
REDIS_PORT = redis_settings.REDIS_PORT
