"""Custom Exceptions.

src > app > errors
"""


class StampException(Exception):
    """Root Exception for Stamp."""

    def __init__(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]# noqa: D107
        super().__init__(*args, **kwargs)


class NotAvailableSessionSecretKeyError(StampException):
    """Ramifice - Exception is raised if Session Secret Key is not available.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = "Session Secret Key is not available!") -> None:  # noqa: D107
        self.message = message
        super().__init__(self.message)
