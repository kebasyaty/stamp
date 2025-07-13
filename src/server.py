"""Run Server."""

import asyncio

import uvicorn

from app.config import (
    UVICORN_APP,
    UVICORN_HOST,
    UVICORN_LOG_LEVEL,
    UVICORN_PORT,
    UVICORN_RELOAD,
)


async def run_server() -> None:
    """Run Server."""
    config = uvicorn.Config(
        app=UVICORN_APP,
        host=UVICORN_HOST,
        port=UVICORN_PORT,
        reload=UVICORN_RELOAD,
        log_level=UVICORN_LOG_LEVEL,
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(run_server())
