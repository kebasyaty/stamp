"""Global Settings.

src > app > config
"""

import logging
from multiprocessing import cpu_count
from typing import Any, Literal

from fastapi.templating import Jinja2Templates
from ramifice.utils.constants import (
    # Absolute filesystem path to the
    # directory that will hold user-uploaded files.
    # Hint: "public/media"
    MEDIA_ROOT,
    # URL that handles the media served from MEDIA_ROOT,
    # used for managing stored files.
    # Hinr: "/media"
    MEDIA_URL,
    # The absolute path to the
    # directory where static files are located.
    # Hint: "public/static"
    STATIC_ROOT,
    # URL to use when referring to
    # static files located in STATIC_ROOT.
    # Hint: "/static"
    STATIC_URL,
)

from app.utils import get_session_secret_key

# Development -> True
# Production -> False
DEBUG: bool = True

# Language by default.
I18N_DEFAULT_LOCALE: str = "en"
# List of supported languages.
I18N_LANGUAGES: frozenset[str] = frozenset(("en", "ru"))

# Host name
HOST_NAME: str = "www.example.com" if not DEBUG else "127.0.0.1"
# Port number
PORT_NUMBER: int = 8000

# Absolute filesystem path to
# the directory that will hold templates.
TEMPLATES: Jinja2Templates = Jinja2Templates(directory="templates")

# The URL, where requests are redirected for login.
LOGIN_URL: str = "/accounts/login/"
# The URL, where requests are redirected for login.
LOGOUT_REDIRECT_URL: str = "/"

# MIDDLEWARE
# Trusted Host
MIDDLEWARE_ALLOWED_HOSTS: list[str] = [HOST_NAME]
# GZip
MIDDLEWARE_GZIP_MINIMUM_SIZE: int = 1000
MIDDLEWARE_GZIP_COMPRESS_LEVEL: int = 5
# Session
SESSION_COOKIE: str = "session"
SESSION_MAX_AGE: int | None = None
SESSION_SAME_SITE: Literal["lax", "strict", "none"] = "lax"
SESSION_PATH: str = "/"
SESSION_HTTPS_ONLY: bool = not DEBUG
SESSION_DOMAIN: str | None = None
SESSION_SECRET_KEY: str | None = get_session_secret_key(
    dotenv_path=".env",
    length=64,
)
# CORS
CORS_ALLOW_ORIGINS: list[str] = (
    [f"https://{HOST_NAME}"]
    if not DEBUG
    else [
        f"http://{HOST_NAME}",
        f"http://{HOST_NAME}:{PORT_NUMBER}",
    ]
)
CORS_ALLOW_METHODS: list[str] = ["GET"]
CORS_ALLOW_HEADERS: list[str] = [
    "Accept",
    "Accept-Language",
    "Content-Language",
    "Content-Type",
]
CORS_ALLOW_CREDENTIALS: bool = True
CORS_EXPOSE_HEADERS: list[str] = []
CORS_MAX_AGE: int = 600

# LOGGING
LOGGING_CONFIG: dict[str, Any] = {
    "level": logging.CRITICAL if not DEBUG else logging.INFO,
    "datefmt": "%Y-%m-%d %H:%M:%S",
    "format": "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
}

# UVICORN
UVICORN_CONFIG: dict[str, Any] = {
    "app": "app.main:app",
    "host": HOST_NAME,
    "port": PORT_NUMBER,
    "reload": DEBUG,
    "log_level": LOGGING_CONFIG["level"],
    "workers": cpu_count() if not DEBUG else None,
}

# MONGODB
MONGO_CONFIG: dict[str, Any] = {
    "host": "127.0.0.1",
    "port": 27017,
    "username": None,
    "password": None,
}
MONGO_DATABASE_NAME: str = "stamp_db"
