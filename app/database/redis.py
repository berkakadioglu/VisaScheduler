"""Redis connections used by the application."""

from redis.asyncio import Redis
from app.config import db_settings

_token_blacklist = Redis(
    host = db_settings.REDIS_HOST,
    port = db_settings.REDIS_PORT,
    db = 0
)
