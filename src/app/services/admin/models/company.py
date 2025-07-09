"""App > Services > Admin > Models > Company Parameters."""

from ramifice import model, translations
from ramifice.fields import (
    ImageField,
    TextField,
)
from ramifice.utils.tools import to_human_size


@model(
    service_name="Admin",
    fixture_name="CompanyParameters",
    is_create_doc=False,
    is_delete_doc=False,
)
class CompanyParameters:
    """Model of Company Parameters."""

    def fields(self) -> None:
        """For adding fields."""
        # For custom translations.
        gettext = translations.gettext
        # ngettext = translations.ngettext
        self.title = TextField(
            label=gettext("Title"),
            placeholder=gettext("Enter Title"),
            multi_language=True,  # Support for several language.
            maxlength=60,
            required=True,
            readonly=True,
            unique=True,
            warning=[
                gettext("It is recommended not to change this Title."),
            ],
        )
        self.logo = ImageField(
            label=gettext("Logo"),
            placeholder=gettext("Upload Logo"),
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
                gettext("Maximum size: %s") % to_human_size(524288),
            ],
        )
        self.brand = TextField(
            label=gettext("Brand"),
            placeholder=gettext("Enter your Company Name"),
            warning=[
                gettext("To apply the change, after saving, restart the browser tab."),
            ],
        )
        self.slogan = TextField(
            label=gettext("Slogan"),
            placeholder=gettext("Enter your company slogan"),
            multi_language=True,  # Support for several language.
            warning=[
                gettext("To apply the change, after saving, restart the browser tab."),
            ],
        )
