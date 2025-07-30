"""Config FastAPI.

src > app > config > fastapi
"""

from typing import Any

from fastapi.responses import ORJSONResponse

from app.config.base import DEBUG

FASTAPI_CONFIG: dict[str, Any] = {
    "debug": DEBUG,
    "default_response_class": ORJSONResponse,
}
