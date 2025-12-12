"""Local Hub of routers.

app > subs > accounts > router
"""

from __future__ import annotations

__all__ = ("router",)

from fastapi import APIRouter

router = APIRouter(tags=["accounts"])
