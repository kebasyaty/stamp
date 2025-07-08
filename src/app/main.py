"""Run App."""

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from pymongo import AsyncMongoClient
from ramifice import migration

from app.config import (
    MONGO_DATABASE,
    MONGO_HOST,
    MONGO_PASSWORD,
    MONGO_PORT,
    MONGO_USERNAME,
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
    """Define the lifespan context manager."""
    # Code to run during startup.
    #
    # Migration of models to database.
    await migration.Monitor(
        database_name=MONGO_DATABASE,
        mongo_client=client,
    ).migrate()
    yield  # Yield control to the application.
    # Code to run during shutdown.
    #
    await client.close()


app = FastAPI(lifespan=lifespan)
app.include_router(root_router)
