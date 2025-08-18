"""Run Uvicorn Server.

src > server
"""

from __future__ import annotations

__all__ = ("run_server",)

import anyio
import uvicorn

from app.config import UVICORN_CONFIG


async def run_server() -> None:
    """Run Server."""
    config_server = uvicorn.Config(**UVICORN_CONFIG)
    server = uvicorn.Server(config_server)
    await server.serve()


if __name__ == "__main__":
    anyio.run(run_server)
