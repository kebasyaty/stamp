"""Local Hub of routers.

app > services > accounts > router
"""

from fastapi import APIRouter

router = APIRouter(tags=["accounts"])
