from src.config import Settings, get_config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

settings: Settings = get_config()
engine = create_async_engine(settings.database_url, future=True, echo=True)
ScopedSession = sessionmaker(bind=engine, class_=AsyncSession)
