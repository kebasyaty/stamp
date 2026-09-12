"""Local Hub of routes."""

from __future__ import annotations

__all__ = ("router",)

from typing import Any

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from ramifice import Translator

from app.config import Config

router = APIRouter(tags=["home"])


@router.get("/", response_class=HTMLResponse)
async def home_page(request: Request) -> Any:
    """Home Page."""
    context = {
        "request": request,
        "lang_code": Translator.DEFAULT_LOCALE,
        "meta_title": "Home Page",
        "meta_description": "???",
        "message": "Hello World",
    }
    return Config.TEMPLATES.TemplateResponse(request, "index.html", context)
