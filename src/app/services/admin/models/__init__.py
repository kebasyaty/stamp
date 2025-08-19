"""Local Hub of models.

src > app > services > admin > models
"""

from __future__ import annotations

__all__ = (
    "AdminPanelParameters",
    "CompanyParameters",
    "SiteParameters",
)

from app.services.admin.models.admin_panel import AdminPanelParameters
from app.services.admin.models.company import CompanyParameters
from app.services.admin.models.site import SiteParameters
