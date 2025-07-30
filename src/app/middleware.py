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
    CORS_ALLOW_CREDENTIALS,
    CORS_ALLOW_HEADERS,
    CORS_ALLOW_METHODS,
    CORS_ALLOW_ORIGINS,
    CORS_EXPOSE_HEADERS,
    CORS_MAX_AGE,
    DEBUG,
    MIDDLEWARE_ALLOWED_HOSTS,
    MIDDLEWARE_GZIP_COMPRESS_LEVEL,
    MIDDLEWARE_GZIP_MINIMUM_SIZE,
    SESSION_CONFIG,
)


def add_middleware(app: FastAPI) -> None:
    """Add middleware to app."""
    app.add_middleware(SessionMiddleware, **SESSION_CONFIG)
    app.add_middleware(
        GZipMiddleware,
        minimum_size=MIDDLEWARE_GZIP_MINIMUM_SIZE,
        compresslevel=MIDDLEWARE_GZIP_COMPRESS_LEVEL,
    )
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=MIDDLEWARE_ALLOWED_HOSTS,
    )
    if not DEBUG:
        app.add_middleware(HTTPSRedirectMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ALLOW_ORIGINS,
        allow_methods=CORS_ALLOW_METHODS,
        allow_headers=CORS_ALLOW_HEADERS,
        allow_credentials=CORS_ALLOW_CREDENTIALS,
        expose_headers=CORS_EXPOSE_HEADERS,
        max_age=CORS_MAX_AGE,
    )
