"""Run FastAPI Application."""

from __future__ import annotations

__all__ = ("app",)

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pymongo import AsyncMongoClient
from ramifice import Migration

from app.config import Config
from app.middleware import add_middleware
from app.models import *  # ruff: ignore[undefined-local-with-import-star]
from app.router import global_router

client: AsyncMongoClient = AsyncMongoClient(**Config.MONGO_CONFIG)


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:  # ruff: ignore[unused-function-argument]
    """The lifespan context manager."""
    # STARTUP
    # Migration of models to database.
    await Migration(
        database_name=Config.MONGO_DATABASE_NAME,
        mongo_client=client,
    ).migrate()
    yield  # ruff: ignore[fallible-context-manager]
    # SHUTDOWN
    await client.close()


app = FastAPI(
    **Config.FASTAPI_CONFIG,
    lifespan=lifespan,
)

add_middleware(app)

app.mount(
    path=Config.STATIC_URL,
    app=StaticFiles(directory=Config.STATIC_ROOT),
    name="static",
)
app.mount(
    path=Config.MEDIA_URL,
    app=StaticFiles(directory=Config.MEDIA_ROOT),
    name="media",
)

app.include_router(global_router)
