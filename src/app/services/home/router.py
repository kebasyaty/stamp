"""App > Services > Home > Router."""

from fastapi import APIRouter

router = APIRouter(tags=["home"])


@router.get("/")
async def root() -> dict:
    """Home Page."""
    return {"message": "Hello World"}
