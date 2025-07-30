"""Logging Config.

src > app > config > logging
"""

import logging
from typing import Any

from app.config.base import DEBUG

# See: https://docs.python.org/3/library/logging.html#logging.basicConfig
LOGGING_CONFIG: dict[str, Any] = {
    "level": logging.CRITICAL if not DEBUG else logging.INFO,
    "datefmt": "%Y-%m-%d %H:%M:%S",
    "format": "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
}
