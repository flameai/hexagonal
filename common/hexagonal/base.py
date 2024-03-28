from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

from hexagonal.registry import CategoryComponent, ComponentCategoryEnum

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine


class RDB(CategoryComponent, ABC):
    category = ComponentCategoryEnum.RelationalDB

    @abstractmethod
    def get_session(self) -> AsyncSession: ...
    @abstractmethod
    def get_engine(self) -> AsyncEngine: ...
