from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    """Application settings"""
    
    # Database (SQLite fallback for easy testing)
    database_url: str = "sqlite:///./task_assignment.db"  # Fallback to SQLite for easy testing
    # For PostgreSQL use: postgresql+asyncpg://username:password@localhost:5432/task_assignment
    
    # JWT
    secret_key: str = "your-secret-key-here-should-be-random-and-secure"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30
    
    # Redis (Optional)
    redis_url: Optional[str] = None
    
    # App
    debug: bool = True
    
    class Config:
        env_file = ".env"


settings = Settings()

# Override database URL from environment if provided (for hosting platforms)
if "DATABASE_URL" in os.environ:
    settings.database_url = os.environ["DATABASE_URL"]