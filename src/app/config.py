"""App > Config.

Global Settings
"""

from fastapi.templating import Jinja2Templates

# Development -> True
# Production -> False
DEBUG: bool = True

# Uvicorn
UVICORN_APP: str = "app.main:app"
UVICORN_HOST: str = "127.0.0.1"
UVICORN_PORT: int = 8000
UVICORN_RELOAD: bool = DEBUG
UVICORN_LOG_LEVEL: str = "info"

# MongoDB
MONGO_HOST: str = "127.0.0.1"
MONGO_PORT: int = 27017
MONGO_USERNAME: str | None = None
MONGO_PASSWORD: str | None = None
MONGO_DATABASE: str = "stamp_db"

# Jinja2
TEMPLATES = Jinja2Templates(directory="templates")
STATIC_URL = "/static"
STATIC_DIR = "public/static"
MEDIA_URL = "/media"
MEDIA_DIR = "public/media"
