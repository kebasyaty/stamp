"""Local Hub of routes.

app > services > admin > router
"""

__all__ = ("router",)

from fastapi import APIRouter

router = APIRouter(tags=["admin"])
