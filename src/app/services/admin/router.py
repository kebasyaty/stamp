"""Local Hub of routes.

src > app > services > admin > router
"""

__all__ = ("router",)

from fastapi import APIRouter

router = APIRouter(tags=["admin"])
