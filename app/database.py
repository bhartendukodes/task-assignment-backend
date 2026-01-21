from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# For compatibility, check if using PostgreSQL or SQLite
database_url = settings.database_url

# For PostgreSQL, ensure asyncpg driver for Python 3.13 compatibility
if database_url.startswith("postgresql") and "+asyncpg" not in database_url and "+psycopg2" not in database_url:
    database_url = database_url.replace("postgresql://", "postgresql+asyncpg://")

# Create SQLAlchemy engine with appropriate configuration
if database_url.startswith("sqlite"):
    # SQLite configuration
    # Ensure directory exists for SQLite file
    import os
    db_path = database_url.replace("sqlite:///", "").replace("sqlite:////", "/")
    if db_path and not db_path.startswith(":memory:"):
        db_dir = os.path.dirname(db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir, exist_ok=True)
    
    engine = create_engine(
        database_url,
        pool_pre_ping=True,
        echo=settings.debug,
        connect_args={"check_same_thread": False}
    )
else:
    # PostgreSQL configuration
    engine = create_engine(
        database_url,
        pool_pre_ping=True,
        echo=settings.debug
    )

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()


def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()