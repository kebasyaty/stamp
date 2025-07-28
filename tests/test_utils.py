"""Testing a utils module.

src > app > utils
"""

import pytest
from src.app.utils import generate_token


class TestUtilsClass:
    """Testing utils module."""

    def test_generate_token(self):
        """Testing a generate_token method."""
        token = generate_token(16)
        assert len(token) == 16
