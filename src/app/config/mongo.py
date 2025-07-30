"""Config MongoDB.

src > app > config > mongo
"""

from typing import Any

MONGO_CONFIG: dict[str, Any] = {
    "host": "127.0.0.1",
    "port": 27017,
    "username": None,
    "password": None,
}
MONGO_DATABASE_NAME: str = "stamp_db"
