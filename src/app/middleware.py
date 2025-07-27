"""Middleware.

src > app > middleware
"""

__all__ = ("add_middleware",)

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.config import (
    DEBUG,
    MIDDLEWARE_ALLOWED_HOSTS,
    SESSION_SECRET_KEY,
)


def add_middleware(app: FastAPI) -> None:
    """Add middleware to app."""
    app.add_middleware(
        SessionMiddleware,
        secret_key=str(SESSION_SECRET_KEY),
    )
    app.add_middleware(
        GZipMiddleware,
        minimum_size=1000,
        compresslevel=5,
    )
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=MIDDLEWARE_ALLOWED_HOSTS,
    )
    if not DEBUG:
        app.add_middleware(HTTPSRedirectMiddleware)
