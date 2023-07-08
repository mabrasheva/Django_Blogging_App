from django.db import models


class Article(models.Model):
    title = models.CharField(
        blank=False,
        null=False,
    )
    text = models.TextField(
        blank=False,
        null=False,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )
    # ToDo
    # author = models.OneToOneField()
