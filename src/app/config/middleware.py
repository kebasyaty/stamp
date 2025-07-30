"""Config Middleware.

src > app > config > middleware
"""

__all__ = (
    "MIDDLEWARE_ALLOWED_HOSTS",
    "MIDDLEWARE_GZIP_CONFIG",
    "MIDDLEWARE_SESSION_CONFIG",
    "MIDDLEWARE_CORS_CONFIG",
    "SECWEB_OPTION",
    "SECWEB_ROUTES",
)

from typing import Any

from app.config.base import (
    DEBUG,
    HOST_NAME,
    PORT_NUMBER,
)
from app.utils import get_session_secret_key

# Trusted Host
# See: https://fastapi.tiangolo.com/advanced/middleware/#trustedhostmiddleware
MIDDLEWARE_ALLOWED_HOSTS: list[str] = [HOST_NAME]
# GZip
# See: https://fastapi.tiangolo.com/advanced/middleware/#gzipmiddleware
MIDDLEWARE_GZIP_CONFIG: dict[str, Any] = {
    "minimum_size": 1000,
    "compresslevel": 5,
}
# Session
# See: https://www.starlette.io/middleware/#sessionmiddleware
MIDDLEWARE_SESSION_CONFIG: dict[str, Any] = {
    "secret_key": get_session_secret_key(
        dotenv_path=".env",
        length=64,
    ),
    "session_cookie": "session",
    "max_age": None,
    "same_site": "lax",
    "path": "/",
    "https_only": not DEBUG,
    "domain": None,
}
# CORS
# See: https://fastapi.tiangolo.com/tutorial/cors/
MIDDLEWARE_CORS_CONFIG: dict[str, Any] = {
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
SECWEB_OPTION: dict[str, Any] = {
    # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy
    # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy-Report-Only
    "csp": {"default-src": ["'self'"]},
    # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
    "referrer": ["no-referrer"],
    # See: https://github.com/tmotagam/Secweb?tab=readme-ov-file#x-dns-prefetch-control
    "xdns": "on",
    # See: https://github.com/tmotagam/Secweb?tab=readme-ov-file#x-permitted-cross-domain-policies
    "xcdp": "all",
    # See: https://github.com/tmotagam/Secweb?tab=readme-ov-file#http-strict-transport-security-hsts
    "hsts": {"max-age": 4, "preload": True},
    # See: https://github.com/tmotagam/Secweb?tab=readme-ov-file#http-strict-transport-security-hsts-for-websockets
    "wshsts": {"max-age": 10, "preload": True},
    # See: https://github.com/tmotagam/Secweb?tab=readme-ov-file#x-frame
    "xframe": "SAMEORIGIN",
    # See: https://github.com/tmotagam/Secweb?tab=readme-ov-file#cross-origin-embedder-policy
    "coep": "require-corp",
    # See: https://github.com/tmotagam/Secweb?tab=readme-ov-file#cross-origin-opener-policy
    "coop": "same-origin-allow-popups",
    # See: https://github.com/tmotagam/Secweb?tab=readme-ov-file#cross-origin-resource-policy
    "corp": "same-site",
    # See: https://github.com/tmotagam/Secweb?tab=readme-ov-file#clear-site-data
    "clearSiteData": {"cache": True, "storage": True},
    # See: https://github.com/tmotagam/Secweb?tab=readme-ov-file#cache-control
    "cacheControl": {"public": True, "s-maxage": 600},
    # See: https://github.com/tmotagam/Secweb?tab=readme-ov-file#x-xss-protection
    "xss": False,
}
# See: https://github.com/tmotagam/Secweb?tab=readme-ov-file#clear-site-data
SECWEB_ROUTES: list[str] = ["/login", "/logout/{id:string}"]
