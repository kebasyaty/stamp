"""Model of Site Parameters."""

from __future__ import annotations

__all__ = ("SiteParameters",)


from ramifice import (
    Model,
    Translator,
    fields,
    meta,
    to_human_size,
)

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELD


@meta(
    service_name="Admin",
    fixture_name="SiteParameters",
    is_create_doc=False,
    is_delete_doc=False,
)
class SiteParameters(Model):
    """Model of Site Parameters."""

    title = fields.TextField(
        label=_("Title"),
        placeholder=_("Enter Title"),
        is_multilingual=True,
        max_length=60,
        is_require=True,
        is_readonly=True,
        warning=[
            _("It is recommended not to change this Title."),
        ],
    )
    banner = fields.ImageField(
        label=_("Banner"),
        placeholder=_("Upload image"),
        default="public/media/default/no_banner.jpg",
        # Directory for images inside media directory.
        target_dir="parameters/banners",
        # Available 4 sizes from lg to xs or None.
        # Hint: By default = None
        thumbnails={"lg": 3840, "md": 1920, "sm": 960, "xs": 480},
        # The maximum size of the original image in bytes.
        # Hint: By default = 2 MB
        max_size=1048576,  # 1 MB = 1024 KB = 1048576 Bytes (in binary)
        warning=[
            _("Banner for site design."),
            _("It is recommended to optimize the image, 100 KB or less (if possible)."),
            _("Maximum size: {}").format(to_human_size(1048576)),
        ],
    )
    contact_email = fields.EmailField(
        label=_("Feedback Email"),
        placeholder=_("Enter a public email"),
    )
    contact_phone = fields.PhoneField(
        label=_("Feedback Phone"),
        placeholder=_("Enter a public phone number"),
    )
    is_active = fields.BooleanField(
        label=_("Site in the repair?"),
        warning=[
            _("Set the site activity."),
        ],
    )
