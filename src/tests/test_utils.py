"""Testing a utils module.

src > app > utils
"""

from app.utils import generate_token


def test_generate_token() -> None:
    """Testing a generate_token method."""
    token = generate_token(64)
    assert len(token) == 86  # secrets.token_urlsafe(64) -> 86
