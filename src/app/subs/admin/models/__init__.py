"""Local Hub of models.

src > app > subs > admin > models
"""

from __future__ import annotations

__all__ = (
    "AdminPanelParameters",
    "CompanyParameters",
    "SiteParameters",
)

from app.subs.admin.models.admin_panel import AdminPanelParameters
from app.subs.admin.models.company import CompanyParameters
from app.subs.admin.models.site import SiteParameters
