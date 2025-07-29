"""Testing a utils module.

src > app > utils
"""

from app.utils import (
    generate_token,
    get_session_secret_key,
)


def test_generate_token() -> None:
    """Testing a generate_token method."""
    token = generate_token(64)
    assert len(token) == 86  # secrets.token_urlsafe(64) -> 86


def test_get_session_secret_key() -> None:
    """Testing a get_session_secret_key method."""
    token = get_session_secret_key(
        dotenv_path=".env",
        length=64,
    )
    assert token is not None
    assert len(token) == 86  # secrets.token_urlsafe(64) -> 86
