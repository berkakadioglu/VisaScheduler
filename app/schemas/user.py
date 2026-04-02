"""Pydantic schemas that define the API contract for user endpoints."""

from pydantic import BaseModel, EmailStr

class BaseUser(BaseModel):
    """Shared fields exposed by user-related payloads."""
    name: str
    email: EmailStr

class UserRead(BaseUser):
    """Schema returned to clients after reading or creating a user."""
    pass

class UserCreate(BaseUser):
    """Schema accepted when a client registers a new account."""
    password: str

class UserLogin(BaseUser):
    """Schema intended for login requests."""
    email: EmailStr
    password: str
