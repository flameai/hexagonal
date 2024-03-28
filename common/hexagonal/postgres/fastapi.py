from common.fastapi.base import AppBaseComponent
from common.fastapi.registry import ComponentCategoryEnum
from common.db.postgres.async_session import Session, engine


class Postgres(AppBaseComponent):
    CATEGORY = ComponentCategoryEnum.RelationalDB

    session = Session

    async def shutdown(self) -> None:
        await engine.dispose()
