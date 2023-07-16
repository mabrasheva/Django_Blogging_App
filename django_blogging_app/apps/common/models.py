from django.contrib.auth import get_user_model
from django.db import models

from django_blogging_app.apps.article.models import Article

UserModel = get_user_model()


class Comment(models.Model):
    comment_text = models.TextField(
        blank=False,
        null=False,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-created_on']
