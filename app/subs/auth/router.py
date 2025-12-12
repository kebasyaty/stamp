"""Local Hub of routes.

app > subs > auth > router
"""

from __future__ import annotations

__all__ = ("router",)

from fastapi import APIRouter

router = APIRouter(tags=["auth"])
