"""Local Hub of routers.

src > app > services > accounts > router
"""

__all__ = ("router",)

from fastapi import APIRouter

router = APIRouter(tags=["accounts"])
