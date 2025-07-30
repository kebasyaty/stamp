"""Global Settings.

src > app > config
"""

import logging
from multiprocessing import cpu_count
from typing import Any

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
MIDDLEWARE_GZIP_CONFIG: dict[str, Any] = {
    "minimum_size": 1000,
    "compresslevel": 5,
}
# Session
MIDDLEWARE_SESSION_CONFIG: dict[str, Any] = {
    "secret_key": get_session_secret_key(
        dotenv_path=".env",
        length=64,
    ),
    "session_cookie": "session",
    "max_age": None,
    "same_site": "lax",
    "path": "/",
    "https_only": not DEBUG,
    "domain": None,
}
# CORS
MIDDLEWARE_CORS_CONFIG: dict[str, Any] = {
    "allow_origins": (
        [
            f"https://{HOST_NAME}",
        ]
        if not DEBUG
        else [
            f"http://{HOST_NAME}:{PORT_NUMBER}",
        ]
    ),
    "allow_methods": ["GET"],
    "allow_headers": [
        "Accept",
        "Accept-Language",
        "Content-Language",
        "Content-Type",
    ],
    "allow_credentials": True,
    "expose_headers": [],
    "max_age": 600,
}

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
