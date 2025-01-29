from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncSession

from sqlalchemy.orm import sessionmaker

from dotenv import dotenv_values
#config = dotenv_values("../../set.env")


#DATABASE_URL ="postgresql+asyncpg://postgres:postgres@localhost:5432/TestDg"
DATABASE_URL ="postgresql+asyncpg://root:ugostyUSER@postgres_ugosty:5432/databaseugosty"

#DATABASE_URL =f"postgresql+asyncpg://{config.get("DATABASE_USER")}:{config.get("DATABASE_PASS")}@{config.get("DATABASE_HOST")}:5432/{config.get("DATABASE_NAME")}"

engine = create_async_engine(DATABASE_URL, echo=True, pool_pre_ping=True) # Проверяет соединение перед выполнением запросов)

async_session = sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False)
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session



