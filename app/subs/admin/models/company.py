"""Model of Company Parameters."""

from __future__ import annotations

__all__ = ("CompanyParameters",)


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
    fixture_name="CompanyParameters",
    is_create_doc=False,
    is_delete_doc=False,
)
class CompanyParameters(Model):
    """Model of Company Parameters."""

    title = fields.TextField(
        label=_("Title"),
        placeholder=_("Enter Title"),
        is_multilingual=True,  # Support for several language.
        max_length=60,
        is_require=True,
        is_readonly=True,
        warning=[
            _("It is recommended not to change this Title."),
        ],
    )
    logo = fields.ImageField(
        label=_("Logo"),
        placeholder=_("Upload Logo"),
        default="public/media/default/logo.png",
        # Directory for images inside media directory.
        target_dir="parameters/logos",
        # Available 4 sizes from lg to xs or None.
        # Hint: By default = None
        thumbnails={"lg": 512, "md": 256, "sm": 128, "xs": 64},
        # The maximum size of the original image in bytes.
        # Hint: By default = 2 MB
        max_size=524288,  # 0.5 MB = 512 KB = 524288 Bytes (in binary)
        warning=[
            _("Maximum size: {}").format(to_human_size(524288)),
        ],
    )
    brand = fields.TextField(
        label=_("Brand"),
        placeholder=_("Enter your Company Name"),
        warning=[
            _("To apply the change, after saving, restart the browser tab."),
        ],
    )
    slogan = fields.TextField(
        label=_("Slogan"),
        placeholder=_("Enter your company slogan"),
        is_multilingual=True,  # Support for several language.
        warning=[
            _("To apply the change, after saving, restart the browser tab."),
        ],
    )
