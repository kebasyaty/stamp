"""Custom Exceptions.

src > app > errors
"""

from __future__ import annotations


class RootCustomException(Exception):
    """Root Custom Exception."""

    def __init__(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]# noqa: D107
        super().__init__(*args, **kwargs)


class NoSessionSecretKeyError(RootCustomException):
    """Exception is raised if Session Secret Key is not available.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = "Session Secret Key is not available!") -> None:  # noqa: D107
        self.message = message
        super().__init__(self.message)
