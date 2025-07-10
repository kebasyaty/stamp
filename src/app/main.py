"""Run App."""

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pymongo import AsyncMongoClient
from ramifice import Migration

from app.config import (
    DEBUG,
    MEDIA_DIR,
    MEDIA_URL,
    MONGO_DATABASE,
    MONGO_HOST,
    MONGO_PASSWORD,
    MONGO_PORT,
    MONGO_USERNAME,
    STATIC_DIR,
    STATIC_URL,
)
from app.models import *
from app.router import root_router

client: AsyncMongoClient = AsyncMongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
)


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
    """The lifespan context manager."""
    # Migration of models to database.
    await Migration(
        database_name=MONGO_DATABASE,
        mongo_client=client,
    ).migrate()
    yield
    await client.close()


app = FastAPI(
    debug=DEBUG,
    lifespan=lifespan,
)
app.mount(
    path=STATIC_URL,
    app=StaticFiles(directory=STATIC_DIR),
    name="static",
)
app.mount(
    path=MEDIA_URL,
    app=StaticFiles(directory=MEDIA_DIR),
    name="media",
)
app.include_router(root_router)
