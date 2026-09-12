"""Custom Exceptions."""

from __future__ import annotations


class RootCustomException(Exception):
    """Root Custom Exception."""

    def __init__(self, *args, **kwargs) -> None:
        """Init RootCustomException."""
        super().__init__(*args, **kwargs)


class NoSessionSecretKeyError(RootCustomException):
    """Exception is raised if Session Secret Key is not available.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = "Session Secret Key is not available!") -> None:
        """Init NoSessionSecretKeyError."""
        self.message = message
        super().__init__(self.message)
