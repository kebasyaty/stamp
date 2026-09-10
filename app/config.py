"""Global configuration."""

from __future__ import annotations

__all__ = ("Config",)

import logging
from multiprocessing import cpu_count
from typing import Any, ClassVar

from fastapi.responses import ORJSONResponse
from fastapi.templating import Jinja2Templates
from ramifice.config import Config as RamificeConfig

from app.utils import get_session_secret_key


class Config:
    """Global configuration."""

    # Development -> True
    # Production -> False
    DEBUG: ClassVar[bool] = True

    # Language by default.
    I18N_DEFAULT_LOCALE: ClassVar[str] = "en"
    # List of supported languages.
    I18N_LANGUAGES: ClassVar[frozenset[str]] = frozenset(("en", "ru"))

    # Host name
    HOST_NAME: ClassVar[str] = "www.example.com" if not DEBUG else "127.0.0.1"
    # Port number
    PORT_NUMBER: ClassVar[int] = 8000

    # Absolute filesystem path to
    # the directory that will hold templates.
    TEMPLATES: ClassVar[Jinja2Templates] = Jinja2Templates(directory="templates")

    # The URL, where requests are redirected for login.
    LOGIN_URL: ClassVar[str] = "/accounts/login/"
    # The URL, where requests are redirected for login.
    LOGOUT_REDIRECT_URL: ClassVar[str] = "/"

    # Absolute filesystem path to the
    # directory that will hold user-uploaded files.
    # Hint: `public/media`
    MEDIA_ROOT: ClassVar[str] = RamificeConfig.MEDIA_ROOT
    # URL that handles the media served from MEDIA_ROOT,
    # used for managing stored files.
    # Hinr: `/media
    MEDIA_URL: ClassVar[str] = RamificeConfig.MEDIA_URL
    # The absolute path to the
    # directory where static files are located.
    # Hint: `public/static`
    STATIC_ROOT: ClassVar[str] = RamificeConfig.STATIC_ROOT
    # URL to use when referring to
    # static files located in STATIC_ROOT.
    # Hint: `/static`
    STATIC_URL: ClassVar[str] = RamificeConfig.STATIC_URL

    # FastAPI
    # ----------------------------------------------------------------------------------------------
    # See: https://fastapi.tiangolo.com/reference/fastapi/
    FASTAPI_CONFIG: ClassVar[dict[str, Any]] = {
        "debug": DEBUG,
        "default_response_class": ORJSONResponse,
    }

    # Logging
    # ----------------------------------------------------------------------------------------------
    # See: https://docs.python.org/3/library/logging.html#logging.basicConfig
    LOGGING_CONFIG: ClassVar[dict[str, Any]] = {
        "level": logging.CRITICAL if not DEBUG else logging.INFO,
        "datefmt": "%Y-%m-%d %H:%M:%S",
        "format": "%(levelname)s  %(name)s:%(filename)s:%(lineno)s %(message)s",
    }

    # MongoDB
    # ----------------------------------------------------------------------------------------------
    # See: https://pymongo.readthedocs.io/en/stable/async-tutorial.html#making-a-connection-with-asyncmongoclient
    # See: https://pymongo.readthedocs.io/en/latest/api/pymongo/client_options.html#pymongo.client_options.ClientOptions
    MONGO_CONFIG: ClassVar[dict[str, Any]] = {
        "host": "mongodb+srv://kebasyaty:pV89ZXdJ9V7mhobD@cluster0.fc2sa1h.mongodb.net/?appName=Cluster0",
        # "host": "127.0.0.1",  # ruff: ignore[commented-out-code]
        # "port": 27017,  # ruff: ignore[commented-out-code]
        # "username": None,  # ruff: ignore[commented-out-code]
        # "password": None,  # ruff: ignore[commented-out-code]
    }
    MONGO_DATABASE_NAME: ClassVar[str] = "stamp_db"

    # Uvicorn
    # ----------------------------------------------------------------------------------------------
    # See: https://www.uvicorn.org/settings/
    UVICORN_CONFIG: ClassVar[dict[str, Any]] = {
        "app": "app:run",
        "host": HOST_NAME,
        "port": PORT_NUMBER,
        "reload": DEBUG,
        "log_level": LOGGING_CONFIG["level"],
        "workers": cpu_count() if not DEBUG else None,
    }

    # Middleware
    # ----------------------------------------------------------------------------------------------
    # Trusted Host
    # See: https://fastapi.tiangolo.com/advanced/middleware/#trustedhostmiddleware
    MIDDLEWARE_ALLOWED_HOSTS: ClassVar[list[str]] = [HOST_NAME]
    # GZip
    # See: https://fastapi.tiangolo.com/advanced/middleware/#gzipmiddleware
    MIDDLEWARE_GZIP_CONFIG: ClassVar[dict[str, Any]] = {
        "minimum_size": 1000,
        "compresslevel": 5,
    }
    # Session
    # See: https://www.starlette.io/middleware/#sessionmiddleware
    MIDDLEWARE_SESSION_CONFIG: ClassVar[dict[str, Any]] = {
        "secret_key": get_session_secret_key(
            dotenv_path=".env",
            length=64,
        ),
        "session_cookie": "session",
        "max_age": 1209600 if not DEBUG else None,  # by default = 2 week = 1209600 seconds
        "same_site": "lax",
        "path": "/",
        "https_only": not DEBUG,
        "domain": None,
    }
    # CORS
    # See: https://fastapi.tiangolo.com/tutorial/cors/
    MIDDLEWARE_CORS_CONFIG: ClassVar[dict[str, Any]] = {
        "allow_origins": (
            [
                f"https://{HOST_NAME}",
            ]
            if not DEBUG
            else [
                f"http://{HOST_NAME}:{PORT_NUMBER}",
            ]
        ),
        "allow_methods": ["GET"],
        "allow_headers": [
            "Accept",
            "Accept-Language",
            "Content-Language",
            "Content-Type",
        ],
        "allow_credentials": True,
        "expose_headers": [],
        "max_age": 600,
    }
    # SecWeb
    # See: https://github.com/tmotagam/Secweb
    # See: https://github.com/tmotagam/Secweb#secweb-class
    SECWEB_OPTIONS: ClassVar[dict[str, Any]] = {
        # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy
        # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy-Report-Only
        "csp": {
            "default-src": ["'self'"],
            "form-action": ["'self'"],
            "base-uri": ["'self'"],
            "object-src": ["'none'"],
            "frame-ancestors": ["'none'"],
            "upgrade-insecure-requests": True,
        },
        # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
        "referrer": ["no-referrer"],
        # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-DNS-Prefetch-Control
        "xdns": "on",
        # See: https://owasp.org/www-project-secure-headers/#x-permitted-cross-domain-policies
        "xcdp": "none",
        # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
        "hsts": {"max-age": 31536000, "includeSubDomains": True},
        # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
        "wshsts": {"max-age": 31536000, "includeSubDomains": True},
        # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
        "xframe": "deny",
        # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Embedder-Policy
        "coep": "require-corp",
        # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Resource-Policy
        "coop": "same-origin",
        # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Resource-Policy
        "corp": "same-origin",
        # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data
        "clearSiteData": {"cache": True, "cookies": True, "storage": True},
        # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control
        "cacheControl": {"no-store": True, "max-age": 0},
        # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection
        "xss": False,
    }
    # See: https://github.com/tmotagam/Secweb?tab=readme-ov-file#clear-site-data
    SECWEB_ROUTES: ClassVar[list[str]] = ["/login", "/logout/{id:string}"]
