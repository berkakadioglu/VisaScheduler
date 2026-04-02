"""Database models for persisted user records."""

from datetime import datetime
from pydantic import EmailStr
from sqlmodel import Column, Field, SQLModel
from uuid import uuid4, UUID
from sqlalchemy.dialects import postgresql

class User(SQLModel, table=True):
    """User table storing identity and password hash information."""
    __tablename__ : str = 'users'
    name: str
    email: EmailStr
    password_hash: str = Field(exclude=True)
    id: UUID = Field(
        sa_column= Column(
            postgresql.UUID,
            default = uuid4,
            primary_key= True,
        )
    )
    created_at: datetime = Field(
        sa_column= Column(
            postgresql.TIMESTAMP,
            default= datetime.now
        )
    )
