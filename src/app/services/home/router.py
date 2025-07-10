"""App > Services > Home > Router.

Face of Site.
"""

from fastapi import APIRouter

router = APIRouter(tags=["home"])


@router.get("/")
async def root() -> dict:
    """Home Page."""
    return {"title": "Home Page"}
