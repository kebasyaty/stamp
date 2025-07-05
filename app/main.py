"""Run App."""

from typing import Any

from fastapi import FastAPI

from .services.accounts.models import User

app = FastAPI()


@app.get("/")
async def read_root() -> dict[str, str]:
    """???"""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None) -> dict[str, Any]:
    """???"""
    return {"item_id": item_id, "q": q}
