"""App > Utils.

Global Utils
"""

import secrets

import aiofiles
from dotenv import dotenv_values


async def get_secret_key(nbytes: int = 64) -> str:
    """Get secret key from .env ."""
    config_file: str = ".env"
    token: str | None = ""
    if await aiofiles.os.path.exists(config_file):
        config: dict[str, str | None] = dotenv_values(config_file)
        token = config.get("SECRET_KEY")
        if token is None:
            async with aiofiles.open(config_file, "a+") as file_env:
                token = secrets.token_urlsafe(nbytes)
                content = f"\nSECRET_KEY={token}"
                await file_env.write(content)
    else:
        async with aiofiles.open(config_file, "w") as new_env:
            token = secrets.token_urlsafe(nbytes)
            content = f"SECRET_KEY={token}"
            await new_env.write(content)
    return str(token)
