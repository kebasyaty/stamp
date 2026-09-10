"""Middleware."""

from __future__ import annotations

__all__ = ("add_middleware",)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from Secweb import SecWeb
from starlette.middleware.sessions import SessionMiddleware

from app.config import Config


def add_middleware(app: FastAPI) -> None:
    """Add middleware to app."""
    if not Config.DEBUG:
        app.add_middleware(HTTPSRedirectMiddleware)
        SecWeb(
            app=app,
            # pyrefly: ignore [bad-argument-type]
            options=Config.SECWEB_OPTIONS,
        )
    app.add_middleware(SessionMiddleware, **Config.MIDDLEWARE_SESSION_CONFIG)
    app.add_middleware(GZipMiddleware, **Config.MIDDLEWARE_GZIP_CONFIG)
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=Config.MIDDLEWARE_ALLOWED_HOSTS,
    )
    app.add_middleware(CORSMiddleware, **Config.MIDDLEWARE_CORS_CONFIG)
