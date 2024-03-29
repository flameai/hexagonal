from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

from hexagonal.registry import CategoryAdapter, AdapterCategoryEnum

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine


class RDB(CategoryAdapter, ABC):
    category = AdapterCategoryEnum.RelationalDB

    @abstractmethod
    def get_session(self) -> AsyncSession: ...
    @abstractmethod
    def get_engine(self) -> AsyncEngine: ...
