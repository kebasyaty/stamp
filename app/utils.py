"""Global Utils.

app > utils
"""

__all__ = ("get_session_secret_key",)

import os
import secrets

from anyio import open_file, to_thread
from dotenv import dotenv_values


async def get_session_secret_key(
    dotenv_path: str = ".env",
    length: int = 64,
) -> str | None:
    """Get secret key from dotenv file."""
    кey: str = "SESSION_SECRET_KEY"
    token: str | None = ""
    if await to_thread.run_sync(os.path.exists, dotenv_path):
        config: dict[str, str | None] = dotenv_values(dotenv_path)
        token = config.get(кey)
        if token is None:
            async with await open_file(dotenv_path, "a+") as env_file:
                token = secrets.token_urlsafe(length)
                content = f"\n{кey}={token}"
                await env_file.write(content)
    else:
        async with await open_file(dotenv_path, "w") as env_file:
            token = secrets.token_urlsafe(length)
            content = f"{кey}={token}"
            await env_file.write(content)
    return token
