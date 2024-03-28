from contextlib import asynccontextmanager


class RedisMethodsFabric:  # TODO Derive from common abstract ancestor
    def __init__(self, redis) -> None:
        self._redis = redis

    async def set_key(self, key):
        ...

    async def get_key(self, key):
        ...

    @asynccontextmanager
    async def while_key_was_not_changed(self, key):
        ...  # Make observing context manager for particular key
        yield

    async def close(self):
        pass