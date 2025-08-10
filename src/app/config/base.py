"""Base Config.

src > app > config > base
"""

__all__ = (
    "MEDIA_ROOT",
    "MEDIA_URL",
    "STATIC_ROOT",
    "STATIC_URL",
    "DEBUG",
    "I18N_DEFAULT_LOCALE",
    "I18N_LANGUAGES",
    "HOST_NAME",
    "PORT_NUMBER",
    "TEMPLATES",
    "LOGIN_URL",
    "LOGOUT_REDIRECT_URL",
)

from fastapi.templating import Jinja2Templates
from ramifice.utils.constants import (
    # Absolute filesystem path to the
    # directory that will hold user-uploaded files.
    # Hint: "public/media"  # noqa: ERA001
    MEDIA_ROOT,
    # URL that handles the media served from MEDIA_ROOT,
    # used for managing stored files.
    # Hinr: "/media"  # noqa: ERA001
    MEDIA_URL,
    # The absolute path to the
    # directory where static files are located.
    # Hint: "public/static"  # noqa: ERA001
    STATIC_ROOT,
    # URL to use when referring to
    # static files located in STATIC_ROOT.
    # Hint: "/static"  # noqa: ERA001
    STATIC_URL,
)

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
