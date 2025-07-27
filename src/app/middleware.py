"""Middleware.

src > app > middleware
"""

__all__ = ("add_middleware",)

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.config import SESSION_SECRET_KEY


def add_middleware(app: FastAPI) -> None:
    """Add middleware to app."""
    app.add_middleware(
        SessionMiddleware,
        secret_key=SESSION_SECRET_KEY,
    )
