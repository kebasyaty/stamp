"""App > Config.

Global Settings
"""

from fastapi.templating import Jinja2Templates

# Development -> True
# Production -> False
DEBUG: bool = True
# Language by default.
DEFAULT_LOCALE: str = "en"
# List of supported languages.
LANGUAGES: frozenset[str] = frozenset(("en", "ru"))
# URI Scheme
URI_SCHEME: str = f"http{'s' if not DEBUG else ''}"
# URI Host
URI_HOST: str = "www.your-domain-name.net" if not DEBUG else "127.0.0.1"
# URI Port
URI_PORT: int = 5000 if not DEBUG else 8000
# Application URL
APP_URL: str = f"{URI_SCHEME}://{URI_HOST}"
# Absolute filesystem path to the
# directory that will hold user-uploaded files.
MEDIA_ROOT = "public/media"
# URL that handles the media served from MEDIA_ROOT,
# used for managing stored files.
MEDIA_URL = "/media"
# The absolute path to the
# directory where static files are located.
STATIC_ROOT = "public/static"
# URL to use when referring to
# static files located in STATIC_ROOT.
STATIC_URL = "/static"
# Absolute filesystem path to the
# directory that will hold templates.
TEMPLATES = Jinja2Templates(directory="templates")
# A secret key.
# This is used to provide cryptographic signing,
# and should be set to a unique, unpredictable value.
SECRET_KEY = ""
# The URL, where requests are redirected for login.
LOGIN_URL = "/accounts/login/"
# The URL, where requests are redirected for login.
LOGOUT_REDIRECT_URL = "/"

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
