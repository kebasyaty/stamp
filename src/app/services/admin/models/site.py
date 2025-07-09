"""App > Services > Admin > Models > Site Parameters."""

from ramifice import model, translations
from ramifice.fields import (
    BooleanField,
    EmailField,
    ImageField,
    PhoneField,
    TextField,
)
from ramifice.utils.tools import to_human_size


@model(
    service_name="Admin",
    fixture_name="SiteParameters",
    is_create_doc=False,
    is_delete_doc=False,
)
class SiteParameters:
    """Model of Site Parameters."""

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
            warning=[
                gettext("It is recommended not to change this Title."),
            ],
        )
        self.banner = ImageField(
            label=gettext("Banner"),
            placeholder=gettext("Upload image"),
            default="public/media/default/building_site.jpg",
            # Directory for images inside media directory.
            target_dir="parameters/banners",
            # Available 4 sizes from lg to xs or None.
            # Hint: By default = None
            thumbnails={"lg": 3840, "md": 1920, "sm": 960, "xs": 480},
            # The maximum size of the original image in bytes.
            # Hint: By default = 2 MB
            max_size=1048576,  # 1 MB = 1024 KB = 1048576 Bytes (in binary)
            warning=[
                gettext("Banner for site design."),
                gettext("It is recommended to optimize the image, 100 KB or less (if possible)."),
                gettext("Maximum size: %s") % to_human_size(1048576),
            ],
        )
        self.contact_email = EmailField(
            label=gettext("Feedback Email"),
            placeholder=gettext("Enter a public email"),
        )
        self.contact_phone = PhoneField(
            label=gettext("Feedback Phone"),
            placeholder=gettext("Enter a public phone number"),
        )
        self.is_active = BooleanField(
            label=gettext("Site in the repair?"),
            warning=[
                gettext("Set the site activity."),
            ],
        )
