from typing import TYPE_CHECKING

from common.hexagonal.base import RDB
from sqlalchemy.ext.asyncio import create_async_engine

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncEngine


class Postgres(RDB):
    def get_engine(self) -> AsyncEngine:
        engine = create_async_engine("postgresql+asyncpg://scott:tiger@localhost:5432/mydatabase")
        return engine


