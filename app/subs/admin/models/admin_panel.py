"""Model of Admin Panel Parameters."""

from __future__ import annotations

__all__ = ("AdminPanelParameters",)


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
    fixture_name="AdminPanelParameters",
    is_create_doc=False,
    is_delete_doc=False,
)
class AdminPanelParameters(Model):
    """Model of Admin Panel Parameters."""

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
    dark_theme = fields.BooleanField(
        label=_("Dark theme?"),
        default=True,
        warning=[
            _("Dark or Light theme."),
        ],
    )
    color_theme = fields.ChoiceTextField(
        label=_("Color Theme"),
        default="blue",
        choices=[
            ["grey", _("Grey")],
            ["blue", _("Blue")],
            ["teal", _("Teal")],
            ["pink", _("Pink")],
            ["green", _("Green")],
            ["purple", _("Purple")],
            ["orange", _("Orange")],
            ["brown", _("Brown")],
        ],
    )
    bg_image = fields.ImageField(
        label=_("Background image"),
        placeholder=_("Upload image"),
        default="public/media/default/building_site.jpg",
        # Directory for images inside media directory.
        target_dir="parameters/background",
        # Available 4 sizes from lg to xs or None.
        # Hint: By default = None
        thumbnails={"lg": 3840, "md": 1920, "sm": 960, "xs": 480},
        # The maximum size of the original image in bytes.
        # Hint: By default = 2 MB
        max_size=1048576,  # 1 MB = 1024 KB = 1048576 Bytes (in binary)
        warning=[
            _("Background image for administrator panel."),
            _("To apply the change, after saving, restart the browser tab."),
            _("Maximum size: {}").format(to_human_size(1048576)),
        ],
    )
    bg_opacity = fields.FloatField(
        label=_("Level of transparency"),
        input_type="range",  # number | range
        default=0.8,
        step=0.1,
        max_number=0.9,
        min_number=0.0,
        warning=[
            _("level of transparency for background image for administrator panel."),
            _("To apply the change, after saving, restart the browser tab."),
        ],
    )
