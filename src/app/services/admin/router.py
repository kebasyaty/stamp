"""Local Hub of routes.

app > services > admin > router
"""

from fastapi import APIRouter

router = APIRouter(tags=["admin"])
