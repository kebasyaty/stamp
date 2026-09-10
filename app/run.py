"""Run FastAPI Application."""

from __future__ import annotations

__all__ = ("app",)

import logging
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

logger = logging.getLogger(__name__)

logger.info("Connecting to the database.")
client: AsyncMongoClient = AsyncMongoClient(**Config.MONGO_CONFIG)


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:  # ruff: ignore[unused-function-argument]
    """The lifespan context manager."""
    # --- STARTUP PHASE ---
    try:
        logger.info("Run migration of models to database...")
        await Migration(
            database_name=Config.MONGO_DATABASE_NAME,
            mongo_client=client,
        ).migrate()
        # Hand control over to FastAPI to handle web requests
        yield
        # SHUTDOWN
        logger.info("Closing database connection...")
        await client.close()
    except Exception as err:
        # This catches errors during STARTUP only
        err_msg = f"Application failed to start! Error: {err}"
        logger.critical(err_msg)
        raise err  # Re-raise so the server stops running entirely
    finally:
        # --- SHUTDOWN PHASE ---
        # This ALWAYS runs when the server stops, even if startup failed halfway through
        logger.info("Closing database connection...")
        try:
            await client.close()
        except Exception as shutdown_error:  # ruff: ignore[blind-except]
            err_msg = f"Error during shutdown: {shutdown_error}"
            logger.error(err_msg)


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
