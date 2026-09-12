"""Run Server."""

from __future__ import annotations

import asyncio
import logging

import uvicorn
from app.config import Config
from ramifice import Translator
from ramifice.config import Config as RamificeConfig

RamificeConfig.DEBUG = Config.DEBUG
logging.basicConfig(**Config.LOGGING_CONFIG)
Translator.add_new_languages(Config.I18N_LANGUAGES)


async def run_server() -> None:
    """Run Uvicorn Server."""
    config_server = uvicorn.Config(**Config.UVICORN_CONFIG)
    server = uvicorn.Server(config_server)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(run_server())
