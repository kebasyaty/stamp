"""Run App."""

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from pymongo import AsyncMongoClient
from ramifice import migration

from app import config, models, router

client: AsyncMongoClient = AsyncMongoClient()


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
    """Define the lifespan context manager."""
    # Code to run during startup.
    await migration.Monitor(
        database_name=config.MONGO_DATABASE_NAME,
        mongo_client=client,
    ).migrate()
    yield  # Yield control to the application.
    # Code to run during shutdown.
    await client.close()


app = FastAPI(lifespan=lifespan)
app.include_router(router.global_router)
