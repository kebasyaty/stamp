"""Global Hub of routers.

src > app > router
"""

from __future__ import annotations

__all__ = ("global_router",)

from typing import Any

from fastapi import APIRouter, Request
from fastapi.responses import (
    FileResponse,
    PlainTextResponse,
    Response,
)

from app.config import (
    STATIC_ROOT,
    TEMPLATES,
)
from app.services.accounts.router import router as accounts_router
from app.services.admin.router import router as admin_router
from app.services.auth.router import router as auth_router
from app.services.home.router import router as home_router

global_router = APIRouter(tags=["global"])
global_router.include_router(accounts_router)
global_router.include_router(admin_router)
global_router.include_router(auth_router)
global_router.include_router(home_router)


@global_router.get("/favicon.ico", include_in_schema=False)
async def get_favicon() -> Any:
    """Get favicon."""
    return FileResponse(f"{STATIC_ROOT}/favicons/favicon.ico")


@global_router.get(
    "/robots.txt",
    response_class=PlainTextResponse,
    include_in_schema=False,
)
async def get_robots(request: Request) -> Any:
    """Get robots."""
    url = request.url
    context = {
        "request": request,
        "scheme": url.scheme,
        "host": url.hostname,
    }
    return TEMPLATES.TemplateResponse("robots.txt", context)


@global_router.get(
    "/sitemap.xml",
    response_class=Response,
    include_in_schema=False,
)
async def get_sitemap(request: Request) -> Any:
    """Get sitemap."""
    items = [
        {
            "loc": "test_loc",
            "lastmod": "test_lastmod",
            "changefreq": "test_changefreq",
            "priority": 0.5,
        },
    ]
    context = {
        "request": request,
        "items": items,
    }
    return TEMPLATES.TemplateResponse(
        "sitemap.xml.j2",
        context,
        media_type="application/xml",
    )
