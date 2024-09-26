"""Global settings for the project."""

import os


class Settings:
    """Global settings for the project."""

    PROJECT_NAME = "FastAPI Clean Architecture"
    PROJECT_DESCRIPTION = "FastAPI Clean Architecture"
    PROJECT_VERSION = "0.1.0"
    API_PREFIX = "/api/v1"
    DEBUG: bool = True
    LOG_FORMAT = "[%(levelname)s] %(asctime)s %(name)s: %(message)s"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    DB_URL = os.getenv("DB_URL")
    MONGO_DB = os.getenv("MONGO_DB")
    MONGO_URL = os.getenv("MONGO_URL")
