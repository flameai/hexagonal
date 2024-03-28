from common.fastapi.base import AppBaseComponent
from common.fastapi.registry import ComponentCategoryEnum


class Redis(AppBaseComponent):
    CATEGORY = ComponentCategoryEnum.NoSQLDB

    async def startup(self) -> None:
        pass

    async def shutdown(self) -> None:
        pass
