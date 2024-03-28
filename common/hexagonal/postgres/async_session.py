from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker

from common.db.postgres.settings import POSTGRES_DSN

engine = create_async_engine(POSTGRES_DSN)

Session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
