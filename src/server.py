"""Run Uvicorn Server.

src > server
"""

__all__ = ("run_server",)

from multiprocessing import cpu_count

import anyio
import uvicorn

from app.config import (
    DEBUG,
    HOST_NAME,
    LOGGING_LEVEL,
)
from app.main import app


async def run_server() -> None:
    """Run Server."""
    config_server = uvicorn.Config(
        app,
        host=HOST_NAME,
        port=8000,
        reload=DEBUG,
        log_level=LOGGING_LEVEL,
        workers=cpu_count() if not DEBUG else None,
    )
    server = uvicorn.Server(config_server)
    await server.serve()


if __name__ == "__main__":
    anyio.run(run_server)
