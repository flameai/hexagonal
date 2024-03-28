import redis.asyncio as redis

from common.db.redis.settings import (
    REDIS_DB,
    REDIS_HOST,
    REDIS_POOL_MAX_CONNECTIONS,
    REDIS_PORT,
)

pool = redis.ConnectionPool.from_url(
    f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}",
    max_connections=REDIS_POOL_MAX_CONNECTIONS,
)
redis = redis.Redis(connection_pool=pool)
