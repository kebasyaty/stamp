"""Local Hub of routes.

app > services > auth > router
"""

from fastapi import APIRouter

router = APIRouter(tags=["auth"])
