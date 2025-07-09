"""App > Services > Admin > Models > Parameters of admin panel."""

from ramifice import model, translations
from ramifice.fields import (
    BooleanField,
    ChoiceTextField,
    FloatField,
    ImageField,
    TextField,
)
from ramifice.utils.tools import to_human_size


@model(
    service_name="Admin",
    fixture_name="AdminPanelParameters",
    is_create_doc=False,
    is_delete_doc=False,
)
class AdminPanelParameters:
    """Model of Admin Panel Parameters."""

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
        self.dark_theme = BooleanField(
            label=gettext("Dark theme?"),
            default=True,
            warning=[
                gettext("Dark or Light theme."),
            ],
        )
        self.color_theme = ChoiceTextField(
            label=gettext("Color Theme"),
            default="blue",
            choices=[
                ["grey", gettext("Grey")],
                ["blue", gettext("Blue")],
                ["teal", gettext("Teal")],
                ["pink", gettext("Pink")],
                ["green", gettext("Green")],
                ["purple", gettext("Purple")],
                ["orange", gettext("Orange")],
                ["brown", gettext("Brown")],
            ],
        )
        self.bg_image = ImageField(
            label=gettext("Background image"),
            placeholder=gettext("Upload image"),
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
                gettext("Background image for administrator panel."),
                gettext("To apply the change, after saving, restart the browser tab."),
                gettext("Maximum size: %s") % to_human_size(1048576),
            ],
        )
        self.bg_opacity = FloatField(
            label=gettext("Level of transparency"),
            input_type="range",  # number | range
            default=0.8,
            step=0.1,
            max_number=0.9,
            min_number=0.0,
            warning=[
                gettext("level of transparency for background image for administrator panel."),
                gettext("To apply the change, after saving, restart the browser tab."),
            ],
        )
