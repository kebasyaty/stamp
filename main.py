"""Run Application."""

from __future__ import annotations

__all__ = ("run_server",)

import asyncio
import logging

import uvicorn
from app import config
from app.config import UVICORN_CONFIG
from ramifice import translations

logging.basicConfig(**config.LOGGING_CONFIG)

translations.add_languages(
    default_locale=config.I18N_DEFAULT_LOCALE,
    languages=config.I18N_LANGUAGES,
)


async def run_server() -> None:
    """Run Uvicorn Server."""
    config_server = uvicorn.Config(**UVICORN_CONFIG)
    server = uvicorn.Server(config_server)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(run_server())
