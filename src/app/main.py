"""Run application.

src > app > main
"""

__all__ = ("app",)

import logging

from ramifice import translations

from app import config
from app.fast_app import app
from app.models import *

logging.basicConfig(
    level=config.LOGGING_LEVEL,
    datefmt=config.LOGGING_DATE_FORMAT,
    format=config.LOGGING_DEFAULT_FORMAT,
)

translations.add_languages(
    default_locale=config.I18N_DEFAULT_LOCALE,
    languages=config.I18N_LANGUAGES,
)
