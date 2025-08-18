"""Local Hub of routes.

src > app > services > auth > router
"""

from __future__ import annotations

__all__ = ("router",)

from fastapi import APIRouter

router = APIRouter(tags=["auth"])
