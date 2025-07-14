"""Run Server."""

import anyio
import uvicorn

from app import config
from app.utils import get_secret_key


async def run_server() -> None:
    """Run Server."""
    # Get secret key
    config.SECRET_KEY = await get_secret_key(
        dotenv_path=".env",
        length=64,
    )
    # Init server
    config_server = uvicorn.Config(
        app=config.UVICORN_APP,
        host=config.UVICORN_HOST,
        port=config.UVICORN_PORT,
        reload=config.UVICORN_RELOAD,
        log_level=config.UVICORN_LOG_LEVEL,
    )
    server = uvicorn.Server(config_server)
    await server.serve()


if __name__ == "__main__":
    anyio.run(run_server)
