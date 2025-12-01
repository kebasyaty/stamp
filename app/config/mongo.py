"""Config MongoDB.

app > config > mongo
"""

from typing import Any

# See: https://pymongo.readthedocs.io/en/stable/async-tutorial.html#making-a-connection-with-asyncmongoclient
# See: https://pymongo.readthedocs.io/en/latest/api/pymongo/client_options.html#pymongo.client_options.ClientOptions
MONGO_CONFIG: dict[str, Any] = {
    "host": "127.0.0.1",
    "port": 27017,
    "username": None,
    "password": None,
}
MONGO_DATABASE_NAME: str = "stamp_db"
