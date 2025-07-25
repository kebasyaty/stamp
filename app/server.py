"""Uvicorn Server.

app > server
"""

__all__ = ("run_server",)

import anyio
import uvicorn

from config import (
    UVICORN_APP,
    UVICORN_HOST,
    UVICORN_LOG_LEVEL,
    UVICORN_PORT,
    UVICORN_RELOAD,
    UVICORN_WORKERS,
)


async def run_server() -> None:
    """Run Server."""
    config_server = uvicorn.Config(
        app=UVICORN_APP,
        host=UVICORN_HOST,
        port=UVICORN_PORT,
        reload=UVICORN_RELOAD,
        log_level=UVICORN_LOG_LEVEL,
        workers=UVICORN_WORKERS,
    )
    server = uvicorn.Server(config_server)
    await server.serve()


if __name__ == "__main__":
    anyio.run(run_server)
