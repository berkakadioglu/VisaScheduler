"""Business logic related to user persistence and password verification."""
from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

password_context = CryptContext(schemes="bcrypt", deprecated="auto")

class UserService():
    """Service object wrapping user queries and mutations."""
    def __init__(self, model: type[User], session: AsyncSession):
        self.model: type[User] = model
        self.session: AsyncSession = session

    async def _add_user(self, data: UserCreate) -> User:
        """Create, persist, and return a new user record."""
        user_data = data.model_dump()
        user = self.model(
            **user_data,
            password_hash = password_context.hash(user_data['password'])
        )

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def _get_by_email(self, email: str) -> User | None:
        """Return a single user record for the given email address if it exists."""
        query = select(User).where(User.email == email)
        return await self.session.scalar(query)

    async def _verify_password(self, email: str, password) -> bool:
        """Validate a plaintext password against the stored hash for a user."""
        user = await self._get_by_email(email)

        if user is None:
            return False

        if password_context.verify(
            password,
            user.password_hash
        ):
            return True
        return False
