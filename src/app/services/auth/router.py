"""Local Hub of routes.

src > app > services > auth > router
"""

__all__ = ("router",)

from fastapi import APIRouter

router = APIRouter(tags=["auth"])
