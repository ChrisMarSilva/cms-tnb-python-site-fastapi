from typing import Generator
from src.database.session import SessionLocal, SessionAsync
from sqlalchemy.ext.asyncio import AsyncSession


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_db_async() -> AsyncSession:
    async with SessionAsync() as session:
        # async with session.begin():
        yield session
