"""App > Router.

Global Hub of routers
"""

from typing import Any

from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, PlainTextResponse

from app.config import STATIC_DIR, TEMPLATES
from app.services.accounts.router import router as accounts_router
from app.services.admin.router import router as admin_router
from app.services.auth.router import router as auth_router
from app.services.home.router import router as home_router

root_router = APIRouter(tags=["root"])
root_router.include_router(accounts_router)
root_router.include_router(admin_router)
root_router.include_router(auth_router)
root_router.include_router(home_router)


@root_router.get("/favicon.ico", include_in_schema=False)
async def get_favicon() -> Any:
    """Get favicon."""
    return FileResponse(f"{STATIC_DIR}/favicons/favicon.ico")


@root_router.get("/robots.txt", response_class=PlainTextResponse, include_in_schema=False)
async def get_robots(request: Request) -> Any:
    """Get robots."""
    context = {
        "request": request,
        "host": "???",
        "scheme": "???",
    }
    return TEMPLATES.TemplateResponse("robots.txt", context)
