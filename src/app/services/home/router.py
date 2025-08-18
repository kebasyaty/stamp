"""Local Hub of routes.

src > app > services > home > router
"""

from __future__ import annotations

__all__ = ("router",)

from typing import Any

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from ramifice import translations

from app.config import TEMPLATES

router = APIRouter(tags=["home"])


@router.get("/", response_class=HTMLResponse)
async def home_page(request: Request) -> Any:
    """Home Page."""
    context = {
        "request": request,
        "lang_code": translations.CURRENT_LOCALE,
        "meta_title": "Home Page",
        "meta_description": "???",
        "message": "Hello World",
    }
    return TEMPLATES.TemplateResponse("index.html", context)
