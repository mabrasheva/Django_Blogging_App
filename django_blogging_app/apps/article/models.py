from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

UserModel = get_user_model()


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
    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    # ToDo
    # author = models.OneToOneField()
    # category
    # tags
    # slug

    class Meta:
        ordering = ['created_on']

    def get_absolute_url(self):
        return reverse('article_details', args=[str(self.pk)])
