"""Local Hub of routers.

app > services > accounts > router
"""

__all__ = ("router",)

from fastapi import APIRouter

router = APIRouter(tags=["accounts"])
