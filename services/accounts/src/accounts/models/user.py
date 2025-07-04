"""User."""

import re

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


@model(service_name="Accounts")
class User:
    """Model of User."""

    def fields(self) -> None:
        """For adding fields."""
        # For custom translations.
        gettext = translations.gettext
        # ngettext = translations.ngettext
        self.avatar = ImageField(
            label=gettext("Avatar"),
            placeholder=gettext("Upload your photo"),
            default="public/media/default/no-photo.png",
            # Directory for images inside media directory.
            target_dir="users/avatars",
            # Available 4 sizes from lg to xs or None.
            # Hint: By default = None
            thumbnails={"lg": 512, "md": 256, "sm": 128, "xs": 64},
            # True - high quality and low performance for thumbnails.
            # Hint: By default = False
            high_quality=True,
            # The maximum size of the original image in bytes.
            # Hint: By default = 2 MB
            max_size=524288,  # 512 KB = 0.5 MB = 524288 Bytes (in binary)
            warning=[
                gettext("Maximum size: %s") % to_human_size(524288),
            ],
        )
        self.username = TextField(
            label=gettext("Username"),
            placeholder=gettext("Enter your username"),
            maxlength=150,
            required=True,
            unique=True,
            warning=[
                gettext("Allowed chars: %s") % "a-z A-Z 0-9 _",
            ],
        )
        self.first_name = TextField(
            label=gettext("First name"),
            placeholder=gettext("Enter your First name"),
            multi_language=True,  # Support for several language.
            maxlength=150,
            required=True,
        )
        self.last_name = TextField(
            label=gettext("Last name"),
            placeholder=gettext("Enter your Last name"),
            multi_language=True,  # Support for several language.
            maxlength=150,
            required=True,
        )
        self.email = EmailField(
            label=gettext("Email"),
            placeholder=gettext("Enter your email"),
            required=True,
            unique=True,
        )
        self.phone = PhoneField(
            label=gettext("Phone number"),
            placeholder=gettext("Enter your phone number"),
            unique=True,
        )
        self.birthday = DateField(
            label=gettext("Birthday"),
            placeholder=gettext("Enter your date of birth"),
        )
        self.password = PasswordField(
            label=gettext("Password"),
            placeholder=gettext("Enter your password"),
        )
        self.сonfirm_password = PasswordField(
            label=gettext("Confirm password"),
            placeholder=gettext("Repeat your password"),
            # If true, the value of this field is not saved in the database.
            ignored=True,
        )
        self.is_admin = BooleanField(
            label=gettext("Is Administrator?"),
            warning=[
                gettext("Can this user access the admin panel?"),
            ],
        )
        self.is_active = BooleanField(
            label=gettext("Is active?"),
            warning=[
                gettext("Is this an active account?"),
            ],
        )
        self.slug = SlugField(
            label=gettext("Slug"),
            slug_sources=["username"],
            disabled=True,
            hide=True,
        )
        self.last_login = DateTimeField(
            label=gettext("Last login"),
            disabled=True,
            hide=True,
            warning=[
                gettext("Date and time of user last login."),
            ],
        )

    # Optional method.
    async def add_validation(self) -> dict[str, str]:
        """Additional validation of fields."""
        gettext = translations.gettext
        error_map: dict[str, str] = {}

        # Get clean data.
        id = self.id.value
        username = self.username.value
        password = self.password.value
        сonfirm_password = self.сonfirm_password.value

        if re.match(r"^[a-zA-Z0-9_]+$", username) is None:  # type: ignore[arg-type]
            error_map["username"] = gettext("Allowed chars: %s") % "a-z A-Z 0-9 _"

        if id is None and (password != сonfirm_password):
            error_map["password"] = gettext("Passwords do not match!")
        return error_map
