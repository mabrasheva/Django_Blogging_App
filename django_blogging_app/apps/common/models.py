from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
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


class Rating(models.Model):
    rating_value = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        blank=True,
        null=True,
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
        # Every user can rate an article only once
        unique_together = ('user', 'article',)

    def __str__(self):
        return f"Rating for {self.article} by {self.user} - {self.rating_value} stars"
