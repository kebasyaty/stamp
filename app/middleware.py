"""Middleware.

app > middleware
"""

from __future__ import annotations

__all__ = ("add_middleware",)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from Secweb import SecWeb
from starlette.middleware.sessions import SessionMiddleware

from app.config import (
    DEBUG,
    MIDDLEWARE_ALLOWED_HOSTS,
    MIDDLEWARE_CORS_CONFIG,
    MIDDLEWARE_GZIP_CONFIG,
    MIDDLEWARE_SESSION_CONFIG,
    SECWEB_OPTION,
    SECWEB_ROUTES,
)


def add_middleware(app: FastAPI) -> None:
    """Add middleware to app."""
    if not DEBUG:
        app.add_middleware(HTTPSRedirectMiddleware)
        SecWeb(
            app=app,
            Option=SECWEB_OPTION,
            Routes=SECWEB_ROUTES,
        )
    app.add_middleware(SessionMiddleware, **MIDDLEWARE_SESSION_CONFIG)
    app.add_middleware(GZipMiddleware, **MIDDLEWARE_GZIP_CONFIG)
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=MIDDLEWARE_ALLOWED_HOSTS,
    )
    app.add_middleware(CORSMiddleware, **MIDDLEWARE_CORS_CONFIG)
