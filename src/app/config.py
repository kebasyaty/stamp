"""App > Config.

Global Settings
"""

from fastapi.templating import Jinja2Templates

# Development -> True
# Production -> False
DEBUG: bool = True
# URI Scheme
URI_SCHEME: str = f"http{'s' if not DEBUG else ''}"
# URI Host
URI_HOST: str = "www.your-domain-name.net" if not DEBUG else "127.0.0.1"
# URI Port
URI_PORT: int = 5000 if not DEBUG else 8000
# Application URL
APP_URL: str = f"{URI_SCHEME}://{URI_HOST}"
#
STATIC_URL = "/static"
STATIC_DIR = "public/static"
MEDIA_URL = "/media"
MEDIA_DIR = "public/media"
TEMPLATES = Jinja2Templates(directory="templates")

# Uvicorn
UVICORN_APP: str = "app.main:app"
UVICORN_HOST: str = URI_HOST
UVICORN_PORT: int = URI_PORT
UVICORN_RELOAD: bool = DEBUG
UVICORN_LOG_LEVEL: str = "info"

# MongoDB
MONGO_HOST: str = "127.0.0.1"
MONGO_PORT: int = 27017
MONGO_USERNAME: str | None = None
MONGO_PASSWORD: str | None = None
MONGO_DATABASE: str = "stamp_db"
