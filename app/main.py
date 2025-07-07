"""Run App."""

import asyncio
from contextlib import asynccontextmanager
from typing import Any

import uvicorn
from fastapi import FastAPI
from pymongo import AsyncMongoClient
from ramifice import migration

from app.services.accounts.models import User


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
    """Define the lifespan context manager."""
    # Code to run during startup
    client: AsyncMongoClient = AsyncMongoClient()
    await migration.Monitor(
        database_name="test_basic",
        mongo_client=client,
    ).migrate()
    yield  # Yield control to the application
    # Code to run during shutdown
    await client.close()


app = FastAPI(lifespan=lifespan)


async def main() -> None:
    """Run Server."""
    config = uvicorn.Config(
        "main:app",
        port=8000,
        log_level="info",
        reload=True,
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
