"""Run App."""

from typing import Any

from fastapi import FastAPI

from app.services.accounts.models import User

app = FastAPI()
