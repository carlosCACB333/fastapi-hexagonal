"""Configuration for the tests."""

from typing import Any, Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from src.infrastructure.config.database import Base, get_pg_db
from src.main import app as original_app

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_pg_db():
    """Override the get_pg_db dependency to use the testing database."""
    db = SessionTesting()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="package")
def app():
    """Override the get_pg_db dependency to use the testing database."""
    original_app.dependency_overrides[get_pg_db] = override_get_pg_db
    yield original_app


@pytest.fixture(scope="module")
def client(
    app: FastAPI,
) -> Generator[TestClient, Any, None]:
    """Create a test client for the FastAPI application."""

    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Create the database tables and drop them after the tests."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
