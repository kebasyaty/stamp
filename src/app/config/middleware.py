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
        dotenv_path="src/.env",
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
SECWEB_ROUTES: list[str] = ["/login", "/logout/{id:string}"]
