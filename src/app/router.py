"""App > Router."""

from fastapi import APIRouter

from app.services.accounts.router import router as accounts_router

global_router = APIRouter()
global_router.include_router(accounts_router)
