"""Application settings loaded from environment variables."""

from pydantic_settings import BaseSettings, SettingsConfigDict

_base_config = SettingsConfigDict(
    env_file= '.env',
    env_ignore_empty= True,
    extra= 'ignore'
)

class DatabaseSettings(BaseSettings):
    """Database and cache connection settings."""
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_URL : str

    REDIS_HOST: str
    REDIS_PORT: int

    model_config = _base_config

class SecuritySettings(BaseSettings):
    """Authentication-related configuration."""
    JWT_SECRET: str
    JWT_ALGORITHM: str

    model_config = _base_config

db_settings = DatabaseSettings()
security_settings = SecuritySettings()
