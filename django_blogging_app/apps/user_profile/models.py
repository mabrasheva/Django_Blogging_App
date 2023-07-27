from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from django_blogging_app.apps.user_profile.validators import validate_only_letters


class BlogUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(MinLengthValidator(FIRST_NAME_MIN_LEN), validate_only_letters,),
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(MinLengthValidator(LAST_NAME_MIN_LEN), validate_only_letters,),
        blank=True,
        null=True,
    )
    email = models.EmailField(
        unique=True,
    )
    profile_image = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return f"{self.first_name}"
        elif self.last_name:
            return f"{self.last_name}"
        else:
            return ""
