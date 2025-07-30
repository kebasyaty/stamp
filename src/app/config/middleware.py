"""Config Middleware.

src > app > config > middleware
"""

__all__ = (
    "MIDDLEWARE_ALLOWED_HOSTS",
    "MIDDLEWARE_GZIP_CONFIG",
    "MIDDLEWARE_SESSION_CONFIG",
    "MIDDLEWARE_CORS_CONFIG",
)

from typing import Any

from app.config.base import (
    DEBUG,
    HOST_NAME,
    PORT_NUMBER,
)
from app.utils import get_session_secret_key

# Trusted Host
# See: https://fastapi.tiangolo.com/advanced/middleware/#trustedhostmiddleware
MIDDLEWARE_ALLOWED_HOSTS: list[str] = [HOST_NAME]
# GZip
# See: https://fastapi.tiangolo.com/advanced/middleware/#gzipmiddleware
MIDDLEWARE_GZIP_CONFIG: dict[str, Any] = {
    "minimum_size": 1000,
    "compresslevel": 5,
}
# Session
# See: https://www.starlette.io/middleware/#sessionmiddleware
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
# See: https://fastapi.tiangolo.com/tutorial/cors/
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
