"""App > Router.

Global Hub of routers.
"""

from fastapi import APIRouter

from app.services.accounts.router import router as accounts_router
from app.services.admin.router import router as admin_router

root_router = APIRouter(tags=["root"])
root_router.include_router(admin_router)
root_router.include_router(accounts_router)


@root_router.get("/")
async def root() -> dict:
    """Home Page."""
    return {"message": "Hello World"}
