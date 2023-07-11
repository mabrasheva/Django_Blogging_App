from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    # user = models.OneToOneField(
    #     UserModel
    # )
