"""Database configuration."""

import logging

from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.infrastructure.config.settings import Settings

engine = create_engine(Settings.DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

logger = logging.getLogger(__name__)


def get_pg_db():
    """Get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


__client = AsyncIOMotorClient(Settings.MONGO_URL)
mongo_client = __client[Settings.MONGO_DB]
