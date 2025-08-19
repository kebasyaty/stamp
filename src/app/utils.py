"""Global Utils.

src > app > utils
"""

from __future__ import annotations

__all__ = (
    "get_session_secret_key",
    "generate_token",
)

import logging
import secrets
from pathlib import Path

from dotenv import dotenv_values

from app.errors import NoSessionSecretKeyError

logger = logging.getLogger(__name__)


def generate_token(length: int) -> str:
    """Generator of tokens."""
    token: str = ""
    try:
        token = secrets.token_urlsafe(length)
    except Exception as err:
        logger.critical(err)
        raise err
    return token


def get_session_secret_key(
    dotenv_path: str = ".env",
    length: int = 64,
) -> str | None:
    """Get secret key from dotenv file.

    If the key is absent, generate it.
    """
    key: str = "SESSION_SECRET_KEY"
    token: str | None = None
    try:
        if Path(dotenv_path).exists():
            config: dict[str, str | None] = dotenv_values(dotenv_path)
            token = config.get(key)
            if token is None:
                with Path(dotenv_path).open("a+", encoding="utf-8") as env_file:
                    token = generate_token(length)
                    content = f"\n{key}={token}"
                    env_file.write(content)
        else:
            token = generate_token(length)
            content = f"{key}={token}"
            Path(dotenv_path).write_text(data=content, encoding="utf-8")
    except Exception as err:
        logger.critical(err)
        raise err

    if token is None:
        logger.critical("Session Secret Key is not available!")
        raise NoSessionSecretKeyError()

    return token
