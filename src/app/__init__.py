"""Init Application."""

__all__ = ("fast_app",)

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.staticfiles import StaticFiles
from pymongo import AsyncMongoClient
from ramifice import Migration

from app import config
from app.middleware import add_middleware
from app.router import global_router

client: AsyncMongoClient = AsyncMongoClient(
    host=config.MONGO_HOST,
    port=config.MONGO_PORT,
    username=config.MONGO_USERNAME,
    password=config.MONGO_PASSWORD,
)


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
    """The lifespan context manager."""
    # STARTUP
    # Migration of models to database.
    await Migration(
        database_name=config.MONGO_DATABASE,
        mongo_client=client,
    ).migrate()
    yield
    # SHUTDOWN
    await client.close()


fast_app = FastAPI(
    debug=config.DEBUG,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

add_middleware(fast_app)

fast_app.mount(
    path=config.STATIC_URL,
    app=StaticFiles(directory=config.STATIC_ROOT),
    name="static",
)
fast_app.mount(
    path=config.MEDIA_URL,
    app=StaticFiles(directory=config.MEDIA_ROOT),
    name="media",
)

fast_app.include_router(global_router)
