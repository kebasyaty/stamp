"""Run App."""

from fastapi import FastAPI

# from pymongo import AsyncMongoClient
# from ramifice import migration, translations

# client: AsyncMongoClient = AsyncMongoClient()

# await migration.Monitor(
#     database_name="test_basic",
#     mongo_client=client,
# ).migrate()

# await client.close()

app = FastAPI()
