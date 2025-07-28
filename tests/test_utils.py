"""Testing a utils module.

src > app > utils
"""

from src.app.utils import generate_token


class TestUtilsClass:
    """Testing utils module."""

    def test_generate_token(self) -> None:
        """Testing a generate_token method."""
        token = generate_token(64)
        assert len(token) == 86
