from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # Email
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    OWNER_EMAIL: str = ""

    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./bookings.db"

    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 5

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
