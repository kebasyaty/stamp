"""App > Services > Admin > Models > Parameters."""

from ramifice import model, translations
from ramifice.fields import (
    BooleanField,
    DateField,
    DateTimeField,
    EmailField,
    ImageField,
    PasswordField,
    PhoneField,
    SlugField,
    TextField,
)
from ramifice.utils.tools import to_human_size


@model(
    service_name="Admin",
    fixture_name="GeneralParameters",
    is_create_doc=False,
    is_delete_doc=False,
)
class GeneralParameters:
    """Model of General Parameters."""

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
            target_dir="site_params/logos",
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
