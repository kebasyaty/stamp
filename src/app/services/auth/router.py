"""Local Hub of routes.

App > Services > Auth > Router
"""

from fastapi import APIRouter

router = APIRouter(tags=["auth"])
