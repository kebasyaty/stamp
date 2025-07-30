"""Middleware.

src > app > middleware
"""

__all__ = ("add_middleware",)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.config import (
    DEBUG,
    MIDDLEWARE_ALLOWED_HOSTS,
    MIDDLEWARE_CORS_CONFIG,
    MIDDLEWARE_GZIP_CONFIG,
    MIDDLEWARE_SESSION_CONFIG,
)


def add_middleware(app: FastAPI) -> None:
    """Add middleware to app."""
    app.add_middleware(SessionMiddleware, **MIDDLEWARE_SESSION_CONFIG)
    app.add_middleware(GZipMiddleware, **MIDDLEWARE_GZIP_CONFIG)
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=MIDDLEWARE_ALLOWED_HOSTS,
    )
    if not DEBUG:
        app.add_middleware(HTTPSRedirectMiddleware)
    app.add_middleware(CORSMiddleware, **MIDDLEWARE_CORS_CONFIG)
