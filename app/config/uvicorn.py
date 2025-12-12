"""Uvicorn Config.

app > config > uvicorn
"""

from multiprocessing import cpu_count
from typing import Any

from app.config.base import (
    DEBUG,
    HOST_NAME,
    PORT_NUMBER,
)
from app.config.logging import LOGGING_CONFIG

# See: https://www.uvicorn.org/settings/
UVICORN_CONFIG: dict[str, Any] = {
    "app": "app:app",
    "host": HOST_NAME,
    "port": PORT_NUMBER,
    "reload": DEBUG,
    "log_level": LOGGING_CONFIG["level"],
    "workers": cpu_count() if not DEBUG else None,
}
