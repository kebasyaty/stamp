"""Global Settings.

src > app > config
"""

import logging
from multiprocessing import cpu_count

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

# Absolute filesystem path to the
# directory that will hold templates.
TEMPLATES: Jinja2Templates = Jinja2Templates(directory="templates")

# The URL, where requests are redirected for login.
LOGIN_URL: str = "/accounts/login/"
# The URL, where requests are redirected for login.
LOGOUT_REDIRECT_URL: str = "/"

# Middleware
MIDDLEWARE_ALLOWED_HOSTS: list[str] = [HOST_NAME]
# A secret key.
# This is used to provide cryptographic signing,
# and should be set to a unique, unpredictable value.
SESSION_SECRET_KEY: str | None = get_session_secret_key(
    dotenv_path=".env",
    length=64,
)

# Logging
LOGGING_DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
LOGGING_DEFAULT_FORMAT: str = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)
LOGGING_LEVEL: str | int = logging.CRITICAL if not DEBUG else logging.INFO

# Uvicorn
UVICORN_APP: str = "app.main:app"
UVICORN_HOST: str = HOST_NAME
UVICORN_PORT: int = 8000
UVICORN_RELOAD: bool = DEBUG
UVICORN_LOG_LEVEL: str | int = LOGGING_LEVEL
UVICORN_WORKERS: int | None = cpu_count() if not UVICORN_RELOAD else None

# MongoDB
MONGO_HOST: str = "127.0.0.1"
MONGO_PORT: int = 27017
MONGO_USERNAME: str | None = None
MONGO_PASSWORD: str | None = None
MONGO_DATABASE: str = "stamp_db"
