"""Database engine and session helpers."""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from app.config import db_settings

engine = create_async_engine(
    url = db_settings.POSTGRES_URL,
    echo = True
)

async def create_db_tables():
    """Create database tables for all imported SQLModel models."""
    async with engine.begin() as connection:
        from app.models.user import User
        await connection.run_sync(SQLModel.metadata.create_all)

async def get_session():
    """Yield an async SQLAlchemy session for request-scoped database work."""
    async_session = sessionmaker(
        bind=engine,
        class_= AsyncSession,
        expire_on_commit= False
    )

    async with async_session() as session:
        yield session
