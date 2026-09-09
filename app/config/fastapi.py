"""Config FastAPI.

app > config > fastapi
"""

from __future__ import annotations

from typing import Any

from fastapi.responses import ORJSONResponse

from app.config.base import DEBUG

# See: https://fastapi.tiangolo.com/reference/fastapi/
FASTAPI_CONFIG: dict[str, Any] = {
    "debug": DEBUG,
    "default_response_class": ORJSONResponse,
}
