"""App > Services > Home > Router.

Face of Site.
"""

from typing import Any

from fastapi import APIRouter
from ramifice import translations

from app.config import TEMPLATES

router = APIRouter(tags=["home"])


@router.get("/")
async def root() -> Any:
    """Home Page."""
    return TEMPLATES.TemplateResponse(
        name="index.html",
        context={
            "lang_code": translations.CURRENT_LOCALE,
            "meta_title": "Home Page",
            "meta_description": "???",
            "message": "Hello World",
        },
    )
