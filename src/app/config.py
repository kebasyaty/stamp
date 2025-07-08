"""App > Config."""

# Project status - Development or Production.
DEBUG: bool = True

# Uvicorn Settings.
UVICORN_APP: str = "app.main:app"
UVICORN_HOST: str = "127.0.0.1"
UVICORN_PORT: int = 8000
UVICORN_RELOAD: bool = DEBUG
UVICORN_LOG_LEVEL: str = "info"

# MongoDB Settings.
MONGO_DATABASE_NAME: str = "test_db"
