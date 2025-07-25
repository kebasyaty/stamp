"""FastAPI Application.

app > main
"""

__all__ = ("app",)

import logging
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.staticfiles import StaticFiles
from pymongo import AsyncMongoClient
from ramifice import Migration, translations

import config
from models import *
from router import global_router

logging.basicConfig(
    level=logging.INFO,
    datefmt=config.LOGGING_DATE_FORMAT,
    format=config.LOGGING_DEFAULT_FORMAT,
)

translations.DEFAULT_LOCALE = config.DEFAULT_LOCALE
translations.LANGUAGES = config.LANGUAGES


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


app = FastAPI(
    debug=config.DEBUG,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
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
