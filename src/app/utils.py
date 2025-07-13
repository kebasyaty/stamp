"""Global Utils.

App > Utils
"""

import secrets

import aiofiles
from dotenv import dotenv_values


async def get_secret_key(
    dotenv_path: str = ".env",
    length: int = 64,
) -> str:
    """Get secret key from .env ."""
    кey: str = "SECRET_KEY"
    token: str | None = ""
    if await aiofiles.os.path.exists(dotenv_path):
        config: dict[str, str | None] = dotenv_values(dotenv_path)
        token = config.get(кey)
        if token is None:
            async with aiofiles.open(dotenv_path, "a+") as file_env:
                token = secrets.token_urlsafe(length)
                content = f"\n{кey}={token}"
                await file_env.write(content)
    else:
        async with aiofiles.open(dotenv_path, "w") as new_env:
            token = secrets.token_urlsafe(length)
            content = f"{кey}={token}"
            await new_env.write(content)
    return str(token)
