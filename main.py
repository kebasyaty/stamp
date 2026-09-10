"""Run Application."""

from __future__ import annotations

__all__ = ("run_server",)

import asyncio
import logging

import uvicorn
from app import config
from app.config import Config
from ramifice import Translator
from ramifice.config import Config as RamificeConfig

RamificeConfig.DEBUG = Config.DEBUG
logging.basicConfig(**config.LOGGING_CONFIG)
Translator.add_new_languages(config.I18N_LANGUAGES)


async def run_server() -> None:
    """Run Uvicorn Server."""
    config_server = uvicorn.Config(**Config.UVICORN_CONFIG)
    server = uvicorn.Server(config_server)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(run_server())
