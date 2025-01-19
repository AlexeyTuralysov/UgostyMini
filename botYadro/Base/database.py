from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncSession

from sqlalchemy.orm import sessionmaker


DATABASE_URL ="postgresql+asyncpg://postgres:postgres@localhost:5432/TestDg"

engine = create_async_engine(DATABASE_URL, echo=True, pool_pre_ping=True) # Проверяет соединение перед выполнением запросов)

async_session = sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False)
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session



