"""Run Application.

app > run
"""

from __future__ import annotations

__all__ = ("app",)

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pymongo import AsyncMongoClient
from ramifice import Migration

from app import config
from app.middleware import add_middleware
from app.models import *  # noqa: F403
from app.router import global_router

client: AsyncMongoClient = AsyncMongoClient(**config.MONGO_CONFIG)


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:  # noqa: ARG001
    """The lifespan context manager."""
    # STARTUP
    # Migration of models to database.
    await Migration(
        database_name=config.MONGO_DATABASE_NAME,
        mongo_client=client,
    ).migrate()
    yield
    # SHUTDOWN
    await client.close()


app = FastAPI(
    **config.FASTAPI_CONFIG,
    lifespan=lifespan,
)

add_middleware(app)

app.mount(
    path=config.STATIC_URL,
    app=StaticFiles(directory=config.STATIC_ROOT),
    name="static",
)
app.mount(
    path=config.MEDIA_URL,
    app=StaticFiles(directory=config.MEDIA_ROOT),
    name="media",
)

app.include_router(global_router)
